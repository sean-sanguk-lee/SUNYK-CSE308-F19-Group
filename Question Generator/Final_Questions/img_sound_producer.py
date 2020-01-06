import time
import glob
import re

import pyimgur
from gtts import gTTS

CLIENT_ID = '209b7fbc19960da'


def main():
    categories = ['animals-1', 'emotions']
    # categories = ['animals-1', 'animals-2', 'emotions', 'foods', 'fruits', 'nature']

    for category in categories:
        img_paths = glob.glob("./image/" + category + "/*.png")
        img_paths.sort()
        img_titles = [crop_title_from_path(path) for path in img_paths]

        with open("./image/" + category + "/imgur_links.txt", "w") as f:
            for i in range(len(img_paths)):
                img_path = img_paths[i]
                img_title = img_titles[i]
                imgur_link = upload_to_imgur(CLIENT_ID, img_path, img_title).link
                get_tts_mp3(category, img_title)

                f.write(img_title + ": " + imgur_link + "\n")
            f.close()


def crop_title_from_path(img_path):
    regex = re.compile(r'\W\w+.png')
    title = regex.search(img_path).group()[1:-4]    # /img_title.png' -> img_title
    return title


def get_tts_mp3(category, title):
    # query Google TTS and save .mp3
    try:
        tts = gTTS(text=title, lang='en')
        mp3_outdir = './sound/' + category + "/" + title + ".mp3"
        tts.save(mp3_outdir)
        print("Successfully downloaded to: " + mp3_outdir)

    except:
        print("Google TTS Error")
        raise Exception


def upload_to_imgur(client_id, PATH, filename):
    try:
        time.sleep(4)   # to prevent request timeout

        imgur_client = pyimgur.Imgur(client_id)
        uploaded_link = imgur_client.upload_image(PATH, title=filename)
        print("Successfully uploaded: " + filename)
        return uploaded_link

    except:
        print("Imgur Error")
        raise Exception


if __name__ == '__main__':
    main()