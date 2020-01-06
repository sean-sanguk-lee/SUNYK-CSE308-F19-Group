# Generate an SQL file depends on the user input of desired category

import glob
import re

DEFAULT = "DROP DATABASE if exists REDBOOK;\n" \
          "CREATE DATABASE REDBOOK;\n" \
          "GRANT ALL PRIVILEGES ON REDBOOK.* to root@localhost IDENTIFIED BY 'root';\n" \
          "use REDBOOK;\n\n"

Users = "CREATE TABLE USERS (\n" \
        "   userid VARCHAR(254) NOT NULL,\n" \
        "   password VARCHAR(254) NOT NULL,\n" \
        "   userType VARCHAR(254) NOT NULL,\n" \
        "   PRIMARY KEY (userid)\n" \
        ");\n\n"
Students = "CREATE TABLE STUDENTS (\n" \
           "   sid VARCHAR(254) NOT NULL,\n" \
           "   fname VARCHAR(254) NOT NULL,\n" \
           "   lname VARCHAR(254) NOT NULL,\n" \
           "   email VARCHAR(254) NOT NULL UNIQUE,\n" \
           "   averageRating INT DEFAULT NULL,\n" \
           "   PRIMARY KEY (sid),\n" \
           "   FOREIGN KEY (sid) REFERENCES USERS(userid)\n" \
           ")ENGINE=InnoDB;\n\n"
Teachers = "CREATE TABLE TEACHERS (\n" \
           "    tid VARCHAR(254) NOT NULL,\n" \
           "    fname VARCHAR(254) NOT NULL,\n" \
           "    lname VARCHAR(254) NOT NULL,\n" \
           "    teacherCode VARCHAR(254) NOT NULL,\n" \
           "    email VARCHAR(254) NOT NULL UNIQUE,\n" \
           "    PRIMARY KEY (tid),\n" \
           "    FOREIGN KEY (tid) REFERENCES USERS(userid)\n" \
           ")ENGINE=InnoDB;\n\n"
FlashCards = "CREATE TABLE FLASHCARDS (\n" \
             "   fid INTEGER NOT NULL AUTO_INCREMENT,\n" \
             "   tid VARCHAR(254) NOT NULL,\n" \
             "   name VARCHAR(254) NOT NULL,\n" \
             "   image VARCHAR(254) NOT NULL,\n" \
             "   sound VARCHAR(254) NOT NULL,\n" \
             "   category VARCHAR(254) NOT NULL,\n" \
             "   averageRating INTEGER DEFAULT NULL,\n" \
             "   PRIMARY KEY (fid),\n" \
             "   FOREIGN KEY (tid) REFERENCES TEACHERS(tid)\n" \
             ")ENGINE=InnoDB;\n\n"
Game = "CREATE TABLE GAME (\n" \
       "    gameID INTEGER NOT NULL,\n" \
       "    cardID INTEGER NOT NULL,\n" \
       "    FOREIGN KEY (cardID) REFERENCES FLASHCARDS(fid)\n" \
       "    ON DELETE CASCADE\n" \
       ");\n\n"
TeachersCodes = "CREATE TABLE TEACHERCODES (\n" \
                "   teacherCode VARCHAR(254) NOT NULL,\n" \
                "   PRIMARY KEY (teacherCode)\n" \
                ");\n\n"

DEFAULT_TABLES = [Users, Students, Teachers, FlashCards, Game, TeachersCodes]
INIT = [DEFAULT] + DEFAULT_TABLES + ["\n\n"]
query_template = 'INSERT INTO FlashCards (tid, name, image, sound, category) values '
DEFAULT_TID = '0'


def main():
    categories = ['animals-1', 'animals-2', 'emotions', 'foods', 'fruits', 'nature']

    with open("./REDBOOK.sql", 'w') as wf:
        for startQuery in INIT:
            wf.write(startQuery)
        userQuery = f"INSERT INTO USERS (userid, password, userType) " \
                    f"VALUES ('{DEFAULT_TID}', 'ADMIN', 'TEACHER');\n"
        teacherQuery = f"INSERT INTO TEACHERS (tid, fname, lname, teacherCode, email) " \
                       f"VALUES ('{DEFAULT_TID}', 'DEFAULT', 'DEFAULTO', 'DEFAULTCODE', 'default@default.com');\n"
        wf.write(userQuery + teacherQuery)

        for category in categories:
            img_links = get_img_links_for_category(category)
            sound_dirs = get_sound_dirs()
            sound_dirs.sort()
            contents = get_img_title_for_category(category)
            contents.sort()

            if len(contents) == len(img_links) == len(sound_dirs):
                for i in range(len(contents)):
                    # WRITE QUERY to REDBOOK.sql
                    QUERY = query_template + f"('{DEFAULT_TID}', '{contents[i]}', '{img_links[i]}', '{sound_dirs[i]}', '{category}');"
                    wf.write(QUERY + "\n")
        wf.close()


def get_img_links_for_category(category):
    link_files = glob.glob("./image/" + category + "/*.txt", recursive=True)

    with open(link_files[0], 'r') as f:
        links = f.readlines()
        for i in range(len(links)):
            ind = links[i].find(':')
            links[i] = links[i][ind+2:].rstrip()
        f.close()
        return links


def get_img_title_for_category(category):
    img_dirs = glob.glob("./image/" + category + "/*.png", recursive=True)
    regex = re.compile(r'\W\w+.png')
    titles = []

    for img_dir in img_dirs:
        titles.append(regex.search(img_dir).group()[1:-4])  # /img_title.png' -> img_title
    return titles


def get_sound_dirs():
    sound_dirs = glob.glob("./sound/*.mp3", recursive=True)
    sound_dirs = ['.' + sound_dir for sound_dir in sound_dirs]
    return sound_dirs


# def get_sound_dirs_for_category(category):
#     sound_dirs = glob.glob("./sound/" + category + "/*.mp3", recursive=True)
#     sound_dirs = ['.' + sound_dir for sound_dir in sound_dirs]
#     return sound_dirs


if __name__ == '__main__':
    main()