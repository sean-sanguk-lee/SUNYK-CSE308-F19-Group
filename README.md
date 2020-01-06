# SUNYK-CSE308-F19-Group

## 1. This Repository was Created...
1. Because the original repository was set private
2. The web application is not being deployed anymore
3. I wanted to keep my work for the project online

## 2. This Repository Includes...
1. The Software Requirement Specification of The Red Book web application
2. The Software Design Document of The Red Book web application
3. My own work done during the project

## 3. What Exactly My Works are...
> My resume regarding this project says: "Directly worked on data processing, automatic learning set (word-image pairs) population, and database management of the system."

The programs that I wrote are:

### 1. Emoji Parser
My initial decision for creating the learning set was to crawl [unicode.org](https://unicode.org) and parse the emoji-description pairs. For populating the database, the team decided to simply create an SQL file at the end of my pipeline. So what **Emoji Parser** does is to
1. Crawl the unicode.org
2. Parse the raw html to emoji-description pair into .xlsx
3. Create an SQL file from .xlsx, after
      1. Uploading the emoji image via imgur API and get a link returned, saved to the .xlsx
      2. Feeding the description of the emojis to Google Text-to-Speech API and get an .mp3 file returned, saved to the .xlsx

** The code for # 1-2: [here](https://github.com/sean-sanguk-lee/SUNYK-CSE308-F19-Group/blob/master/Question%20Generator/Emoji%20Parser/Emoji_Parser.py) <br>
** The code for # 3-1, 3-2: [here](https://github.com/sean-sanguk-lee/SUNYK-CSE308-F19-Group/blob/master/Question%20Generator/Emoji%20Parser/img_sound_producer.py)

Then feed the SQL file to the database manually.

### 2. SQL_to_JSON
But our frontend then decided to fetch the data from a JSON format instead of fetching it directly from the database, due to the concern with a network latency issue.

That's why **SQL_to_JSON** was wrote. Due to the limited time at the moment, I first wrote [SQL_to_JSON.py](https://github.com/sean-sanguk-lee/SUNYK-CSE308-F19-Group/blob/master/Question%20Generator/SQL%20to%20JSON/SQL_to_JSON.py) to simply convert the SQL file generated from the Emoji Parser to a JSON file, structured as the frontend needed.

### 3. Final_Questions
At the stage before the final presentation, few earlier decisions were changed for better production values. Changes include:
1. Using big emojis from [emojiisland.com](https://emojiisland.com) (the frontend directly sent the images to me)
2. Fixing the frontend to create the JSON file at the time of initial loading of users to apply the DB change

A fixed version of [img_sound_producer.py](https://github.com/sean-sanguk-lee/SUNYK-CSE308-F19-Group/blob/master/Question%20Generator/Final_Questions/img_sound_producer.py) was wrote to save the list of imgur links as .txt AND to save the .mp3 files separately, by using the big emoji images.

The way of handling #2 was straightforward: still create an SQL file [(query_creator.py)](https://github.com/sean-sanguk-lee/SUNYK-CSE308-F19-Group/blob/master/Question%20Generator/Final_Questions/query_creator.py), populate the database with the SQL file, then query the running MySQL database to fetch the data and create a JSON file with the return value [(jsonCreator.py)](https://github.com/sean-sanguk-lee/SUNYK-CSE308-F19-Group/blob/master/Question%20Generator/SQL%20to%20JSON/jsonCreator.py).

jsonCreator.py will run at the time of initial loading of user at the frontend.

## 4. Summary
1. This repo shows my work done during the F19 CSE308 Software Engineering course.
2. Each program was created for instantaneous purposes at some points during the project.
3. Descriptions for the programs contain decision making process of the team.
