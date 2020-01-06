DROP DATABASE if exists REDBOOK;
CREATE DATABASE REDBOOK;
GRANT ALL PRIVILEGES ON REDBOOK.* to root@localhost IDENTIFIED BY 'root';
use REDBOOK;

CREATE TABLE USERS (
   userid VARCHAR(254) NOT NULL,
   password VARCHAR(254) NOT NULL,
   userType VARCHAR(254) NOT NULL,
   PRIMARY KEY (userid)
);

CREATE TABLE STUDENTS (
   sid VARCHAR(254) NOT NULL,
   fname VARCHAR(254) NOT NULL,
   lname VARCHAR(254) NOT NULL,
   email VARCHAR(254) NOT NULL UNIQUE,
   averageRating INT DEFAULT NULL,
   PRIMARY KEY (sid),
   FOREIGN KEY (sid) REFERENCES USERS(userid)
)ENGINE=InnoDB;

CREATE TABLE TEACHERS (
    tid VARCHAR(254) NOT NULL,
    fname VARCHAR(254) NOT NULL,
    lname VARCHAR(254) NOT NULL,
    teacherCode VARCHAR(254) NOT NULL,
    email VARCHAR(254) NOT NULL UNIQUE,
    PRIMARY KEY (tid),
    FOREIGN KEY (tid) REFERENCES USERS(userid)
)ENGINE=InnoDB;

CREATE TABLE FLASHCARDS (
   fid INTEGER NOT NULL AUTO_INCREMENT,
   tid VARCHAR(254) NOT NULL,
   name VARCHAR(254) NOT NULL,
   image VARCHAR(254) NOT NULL,
   sound VARCHAR(254) NOT NULL,
   category VARCHAR(254) NOT NULL,
   averageRating INTEGER DEFAULT NULL,
   PRIMARY KEY (fid),
   FOREIGN KEY (tid) REFERENCES TEACHERS(tid)
)ENGINE=InnoDB;

CREATE TABLE GAME (
    gameID INTEGER NOT NULL,
    cardID INTEGER NOT NULL,
    FOREIGN KEY (cardID) REFERENCES FLASHCARDS(fid)
    ON DELETE CASCADE
);

CREATE TABLE TEACHERCODES (
   teacherCode VARCHAR(254) NOT NULL,
   PRIMARY KEY (teacherCode)
);



INSERT INTO USERS (userid, password, userType) VALUES ('0', 'ADMIN', 'TEACHER');
INSERT INTO TEACHERS (tid, fname, lname, teacherCode, email) VALUES ('0', 'DEFAULT', 'DEFAULTO', 'DEFAULTCODE', 'default@default.com');
INSERT INTO FlashCards (tid, name, image, sound, category) values ('0', 'Ant', 'https://i.imgur.com/pm9mP2j.png', '../sound/Ant.mp3', 'animals-1');
INSERT INTO FlashCards (tid, name, image, sound, category) values ('0', 'Dolphin', 'https://i.imgur.com/LXlxAdF.png', '../sound/Dolphin.mp3', 'animals-1');
INSERT INTO FlashCards (tid, name, image, sound, category) values ('0', 'Fish', 'https://i.imgur.com/aWhTAcC.png', '../sound/Fish.mp3', 'animals-1');
INSERT INTO FlashCards (tid, name, image, sound, category) values ('0', 'Frog', 'https://i.imgur.com/VNisFlc.png', '../sound/Frog.mp3', 'animals-1');
INSERT INTO FlashCards (tid, name, image, sound, category) values ('0', 'Honeybee', 'https://i.imgur.com/f7M0LFj.png', '../sound/Honeybee.mp3', 'animals-1');
INSERT INTO FlashCards (tid, name, image, sound, category) values ('0', 'Octopus', 'https://i.imgur.com/lAxer4L.png', '../sound/Octopus.mp3', 'animals-1');
INSERT INTO FlashCards (tid, name, image, sound, category) values ('0', 'Shell', 'https://i.imgur.com/ssQyzMC.png', '../sound/Shell.mp3', 'animals-1');
INSERT INTO FlashCards (tid, name, image, sound, category) values ('0', 'Snake', 'https://i.imgur.com/7Vy94L2.png', '../sound/Snake.mp3', 'animals-1');
INSERT INTO FlashCards (tid, name, image, sound, category) values ('0', 'Turtle', 'https://i.imgur.com/bbuPsMs.png', '../sound/Turtle.mp3', 'animals-1');
INSERT INTO FlashCards (tid, name, image, sound, category) values ('0', 'Whale', 'https://i.imgur.com/jU1cnF3.png', '../sound/Whale.mp3', 'animals-1');
INSERT INTO FlashCards (tid, name, image, sound, category) values ('0', 'Bear', 'https://i.imgur.com/GP0R3JZ.png', '../sound/Bear.mp3', 'animals-2');
INSERT INTO FlashCards (tid, name, image, sound, category) values ('0', 'Cat', 'https://i.imgur.com/BmMOrnU.png', '../sound/Cat.mp3', 'animals-2');
INSERT INTO FlashCards (tid, name, image, sound, category) values ('0', 'Cow', 'https://i.imgur.com/ulBf9HI.png', '../sound/Cow.mp3', 'animals-2');
INSERT INTO FlashCards (tid, name, image, sound, category) values ('0', 'Dog', 'https://i.imgur.com/6GPIrN4.png', '../sound/Dog.mp3', 'animals-2');
INSERT INTO FlashCards (tid, name, image, sound, category) values ('0', 'Koala', 'https://i.imgur.com/tr6lwex.png', '../sound/Koala.mp3', 'animals-2');
INSERT INTO FlashCards (tid, name, image, sound, category) values ('0', 'Monkey', 'https://i.imgur.com/4tx9IxG.png', '../sound/Monkey.mp3', 'animals-2');
INSERT INTO FlashCards (tid, name, image, sound, category) values ('0', 'Panda', 'https://i.imgur.com/DJLLhIA.png', '../sound/Panda.mp3', 'animals-2');
INSERT INTO FlashCards (tid, name, image, sound, category) values ('0', 'Pig', 'https://i.imgur.com/zOrcWJj.png', '../sound/Pig.mp3', 'animals-2');
INSERT INTO FlashCards (tid, name, image, sound, category) values ('0', 'Rabbit', 'https://i.imgur.com/tZ1HRgs.png', '../sound/Rabbit.mp3', 'animals-2');
INSERT INTO FlashCards (tid, name, image, sound, category) values ('0', 'Tiger', 'https://i.imgur.com/NZ04EN2.png', '../sound/Tiger.mp3', 'animals-2');
INSERT INTO FlashCards (tid, name, image, sound, category) values ('0', 'Cry', 'https://i.imgur.com/jBrB5IA.png', '../sound/Cry.mp3', 'emotions');
INSERT INTO FlashCards (tid, name, image, sound, category) values ('0', 'Disappoint', 'https://i.imgur.com/YvUfkVD.png', '../sound/Disappoint.mp3', 'emotions');
INSERT INTO FlashCards (tid, name, image, sound, category) values ('0', 'Fear', 'https://i.imgur.com/nin73PJ.png', '../sound/Fear.mp3', 'emotions');
INSERT INTO FlashCards (tid, name, image, sound, category) values ('0', 'Happy', 'https://i.imgur.com/NLhzK3x.png', '../sound/Happy.mp3', 'emotions');
INSERT INTO FlashCards (tid, name, image, sound, category) values ('0', 'Kiss', 'https://i.imgur.com/5SgK1pw.png', '../sound/Kiss.mp3', 'emotions');
INSERT INTO FlashCards (tid, name, image, sound, category) values ('0', 'Love', 'https://i.imgur.com/bm7hF4u.png', '../sound/Love.mp3', 'emotions');
INSERT INTO FlashCards (tid, name, image, sound, category) values ('0', 'Sad', 'https://i.imgur.com/E4MtQGc.png', '../sound/Sad.mp3', 'emotions');
INSERT INTO FlashCards (tid, name, image, sound, category) values ('0', 'Sleepy', 'https://i.imgur.com/ag3Wfzn.png', '../sound/Sleepy.mp3', 'emotions');
INSERT INTO FlashCards (tid, name, image, sound, category) values ('0', 'Surprise', 'https://i.imgur.com/cHXCHpc.png', '../sound/Surprise.mp3', 'emotions');
INSERT INTO FlashCards (tid, name, image, sound, category) values ('0', 'Wink', 'https://i.imgur.com/oysufAl.png', '../sound/Wink.mp3', 'emotions');
INSERT INTO FlashCards (tid, name, image, sound, category) values ('0', 'Burger', 'https://i.imgur.com/3rOYD9j.png', '../sound/Burger.mp3', 'foods');
INSERT INTO FlashCards (tid, name, image, sound, category) values ('0', 'Cake', 'https://i.imgur.com/ekwGc7G.png', '../sound/Cake.mp3', 'foods');
INSERT INTO FlashCards (tid, name, image, sound, category) values ('0', 'Chocolate', 'https://i.imgur.com/m2B2Bfn.png', '../sound/Chocolate.mp3', 'foods');
INSERT INTO FlashCards (tid, name, image, sound, category) values ('0', 'Cookie', 'https://i.imgur.com/4t2Tg26.png', '../sound/Cookie.mp3', 'foods');
INSERT INTO FlashCards (tid, name, image, sound, category) values ('0', 'Donut', 'https://i.imgur.com/Tg74VUa.png', '../sound/Donut.mp3', 'foods');
INSERT INTO FlashCards (tid, name, image, sound, category) values ('0', 'Fries', 'https://i.imgur.com/LKS3oty.png', '../sound/Fries.mp3', 'foods');
INSERT INTO FlashCards (tid, name, image, sound, category) values ('0', 'Meat', 'https://i.imgur.com/oFsLm3y.png', '../sound/Meat.mp3', 'foods');
INSERT INTO FlashCards (tid, name, image, sound, category) values ('0', 'Pizza', 'https://i.imgur.com/SQBSKKd.png', '../sound/Pizza.mp3', 'foods');
INSERT INTO FlashCards (tid, name, image, sound, category) values ('0', 'Sushi', 'https://i.imgur.com/6WCXyUg.png', '../sound/Sushi.mp3', 'foods');
INSERT INTO FlashCards (tid, name, image, sound, category) values ('0', 'Taco', 'https://i.imgur.com/O6aIiiq.png', '../sound/Taco.mp3', 'foods');
INSERT INTO FlashCards (tid, name, image, sound, category) values ('0', 'Apple', 'https://i.imgur.com/aVIV37X.png', '../sound/Apple.mp3', 'fruits');
INSERT INTO FlashCards (tid, name, image, sound, category) values ('0', 'Banana', 'https://i.imgur.com/D6nq4p6.png', '../sound/Banana.mp3', 'fruits');
INSERT INTO FlashCards (tid, name, image, sound, category) values ('0', 'Cherry', 'https://i.imgur.com/yUhBR5m.png', '../sound/Cherry.mp3', 'fruits');
INSERT INTO FlashCards (tid, name, image, sound, category) values ('0', 'Eggplant', 'https://i.imgur.com/IwKLYfv.png', '../sound/Eggplant.mp3', 'fruits');
INSERT INTO FlashCards (tid, name, image, sound, category) values ('0', 'Grape', 'https://i.imgur.com/a3X2CXX.png', '../sound/Grape.mp3', 'fruits');
INSERT INTO FlashCards (tid, name, image, sound, category) values ('0', 'Lemon', 'https://i.imgur.com/bJvBCda.png', '../sound/Lemon.mp3', 'fruits');
INSERT INTO FlashCards (tid, name, image, sound, category) values ('0', 'Orange', 'https://i.imgur.com/Q9mBSm3.png', '../sound/Orange.mp3', 'fruits');
INSERT INTO FlashCards (tid, name, image, sound, category) values ('0', 'Peach', 'https://i.imgur.com/qHX8ZlR.png', '../sound/Peach.mp3', 'fruits');
INSERT INTO FlashCards (tid, name, image, sound, category) values ('0', 'Watermelon', 'https://i.imgur.com/MHYBCcu.png', '../sound/Watermelon.mp3', 'fruits');
INSERT INTO FlashCards (tid, name, image, sound, category) values ('0', 'Cloud', 'https://i.imgur.com/BjcvugX.png', '../sound/Cloud.mp3', 'nature');
INSERT INTO FlashCards (tid, name, image, sound, category) values ('0', 'Earth', 'https://i.imgur.com/NXIy3U3.png', '../sound/Earth.mp3', 'nature');
INSERT INTO FlashCards (tid, name, image, sound, category) values ('0', 'Lightning', 'https://i.imgur.com/qyUhqE9.png', '../sound/Lightning.mp3', 'nature');
INSERT INTO FlashCards (tid, name, image, sound, category) values ('0', 'Moon', 'https://i.imgur.com/vs7DtKm.png', '../sound/Moon.mp3', 'nature');
INSERT INTO FlashCards (tid, name, image, sound, category) values ('0', 'Rainbow', 'https://i.imgur.com/Q3S1CNq.png', '../sound/Rainbow.mp3', 'nature');
INSERT INTO FlashCards (tid, name, image, sound, category) values ('0', 'Rose', 'https://i.imgur.com/Ffp8NwH.png', '../sound/Rose.mp3', 'nature');
INSERT INTO FlashCards (tid, name, image, sound, category) values ('0', 'Snow', 'https://i.imgur.com/SOUEq9i.png', '../sound/Snow.mp3', 'nature');
INSERT INTO FlashCards (tid, name, image, sound, category) values ('0', 'Star', 'https://i.imgur.com/L2sauBF.png', '../sound/Star.mp3', 'nature');
INSERT INTO FlashCards (tid, name, image, sound, category) values ('0', 'Sun', 'https://i.imgur.com/SGNtdAg.png', '../sound/Sun.mp3', 'nature');
INSERT INTO FlashCards (tid, name, image, sound, category) values ('0', 'Wave', 'https://i.imgur.com/Jgwnzoz.png', '../sound/Wave.mp3', 'nature');