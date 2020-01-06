### SQL INSERT Queries -> JSON

# db name = REDBOOK.sql
# table name = MatchingGame
# Flashcard Object = [FID, IMG, CONTENT, SOUND]
# JSON Format: check template.json in the same directory

import json
import os
import re
import numpy as np

infile_dir = os.getcwd() + "/REDBOOK.sql"
outfile_dir = os.getcwd() + "/questions.json"
# p = re.compile("s[(].*\"")
p = re.compile("ht.*[\\']")        # regex for filtering the 3-tuple in each INSERT queries
questions = {'games': [             # basic structure of template.json
                {'images': [

                ]}
            ]}
contents = []


## read the sql file
with open(infile_dir) as sql:
    for query in sql:
        # only process INSERT queries
        if query.startswith('INSERT'):
            elms = p.findall(query)[0].replace(' ', '').split(",")      # 3-tuple converted to list
            elm_dict = {}

            # ['web link of img', 'Correct answer', 'relative link of sound']
            img_link, sound_link, answr = elms[0][:-1], elms[1][2:-1], elms[2][1:-1]

            # store all the correct answers to utilize them as possible answers of other questions
            contents.append(answr)
            elm_dict = {"image": img_link, "sound": sound_link, "content": [], "correct": -1}
            questions['games'][0]['images'].append(elm_dict)
    sql.close()


## pick 4 possible answers (contents) including the correct one
for i, question in enumerate(questions['games'][0]['images']):
    temp = contents[i]     # correct answer
    content_lst = [temp]

    # pick 3 but excluding the correct answer
    del contents[i]
    elm_content = np.random.choice(contents, 3, replace=False)
    contents.insert(i, temp)
    content_lst.extend(elm_content)
    np.random.shuffle(content_lst)

    question['content'] = content_lst           # 4 possible answers with the correct answer
    question['correct'] = content_lst.index(contents[i])        # index of the correct answer


## prettyprint to output .json file
with open(outfile_dir, "w") as jf:
    jf.write(json.dumps(questions, indent=4))
    jf.close()