#
#     Connect to a running MySQL Database
#     Grab flashcards based on the category the user chose
#     Create a JSON file (check template.json for the format)
#         10 Flashcards with:
#           image link (String)
#           directory to the TTS (String)
#           choices - previously 'contents' (List)
#           correct answers (Integer)

import json
import numpy as np
import pymysql

config = {
  'user': 'root',
  'password': 'root',
  'host': 'localhost',
  'port': 8889,
  'database': 'REDBOOK',
}
outfile_dir = "../flashcards.json"


def main():
  conn = connect()
  cursor = conn.cursor()

  flashcards = fetchAllFlashcards(cursor)
  JSONBody = createJSONBody(flashcards)

  ## prettyprint to output .json file
  with open(outfile_dir, "w") as jf:
    jf.write(json.dumps(JSONBody, indent=4))
    jf.close()

  conn.close()
  print("Created a JSON file from the tuples in the database")


def connect():
  return pymysql.connect(host=config['host'], port=config['port'],
                         user=config['user'], password=config['password'], database=config['database'])


def fetchAllFlashcards(cursor):
  cursor.execute('SELECT * FROM FLASHCARDS')
  return cursor.fetchall()


def createJSONBody(flashCardTuples):
  game_object = {"games": []}
  category_placeholder = {"category": []}
  contents = []
  for i, tuple in enumerate(flashCardTuples):
    fid, category, img_link, sound_link = tuple[0], tuple[5], tuple[3], tuple[4]
    name = tuple[2]

    # store all the correct answers to utilize them as possible answers of other questions
    contents.append(name)
    elm_dict = {"fid": fid, "category": category, "image": img_link,
                "sound": sound_link, "content": [name], "correct": -1}
    category_placeholder["category"].append(elm_dict)

    if i != 0 and i % 10 == 0:
      ## pick 4 possible answers (contents) including the correct one
      for i, flashcard in enumerate(category_placeholder["category"]):
        temp = contents[i]  # correct answer
        content_lst = [temp]

        # pick 3 but excluding the correct answer
        del contents[i]
        elm_content = np.random.choice(contents, 3, replace=False)
        contents.insert(i, temp)
        content_lst.extend(elm_content)
        np.random.shuffle(content_lst)

        flashcard['content'] = content_lst  # 4 possible answers with the correct answer
        flashcard['correct'] = content_lst.index(contents[i])  # index of the correct answer

      np.random.shuffle(category_placeholder["category"])
      game_object['games'].append(category_placeholder)
      category_placeholder, contents = {"category": []}, []

  return game_object


if __name__ == '__main__':
  main()