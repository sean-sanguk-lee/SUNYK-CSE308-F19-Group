# Get Raw HTML file from https://unicode.org/emoji/charts/full-emoji-list.html
# Process the file to parse data as (emoji #, Emoji Char, Browser Repr Img, CLDR Short Name)
    # Each worksheet shall have emojis of each categories
# Save result as .xlsx

import os
import re
from bs4 import BeautifulSoup
import requests
import openpyxl as xl

web_url = "https://unicode.org/emoji/charts/full-emoji-list.html"
filename = "emoji-word-data.html"


def flatten_str_lst(str_lst):
    ret = ""
    for str in str_lst:
        ret += str
    return ret


def main():
    ## request and save raw html
    outfile_dir = os.getcwd() + '/' + filename

    if not os.path.isfile(outfile_dir):
        resp = requests.get(web_url)
        with open(outfile_dir, 'w') as f:
            f.writelines(resp.text)
            f.close()

    ## init workbook
    write_wb = xl.Workbook()
    ws_active = write_wb.active
    ws_active.title = "Summary"

    ## init regex
    # regex_img = re.compile('src=".*"/>')

    ## init Soup and fetch
    with open(outfile_dir, 'r') as fp:
        bs = BeautifulSoup(fp, 'html.parser')

        # get categories and set it as worksheet title
        category_name = bs.findAll('th', {'class': 'mediumhead'})
        emoji_char = bs.findAll('td', {'class': 'chars'})
        cldr = bs.findAll('td', {'class': 'name'})

        num_in_cat = 0
        for i in range(len(category_name)):
            # init worksheet
            current_ws = write_wb.create_sheet(category_name[i].text)

            # writing header
            current_ws.append(['Emoji Char', 'Short Description', 'Base64 Img', 'Imgur Link', 'Sound'])

            cat_line_lookahead = category_name[i+1].sourceline if i < len(category_name)-1 else category_name[i].sourceline

            while True:
                emoji_line = emoji_char[num_in_cat].sourceline
                cldr_line = cldr[num_in_cat].sourceline
                emoji_base64 = emoji_char[num_in_cat].next_sibling.next_sibling.__repr__()
                ind1 = emoji_base64.find('src=')
                emoji_base64 = emoji_base64[ind1+5:-8]

                if cat_line_lookahead < emoji_line and cat_line_lookahead < cldr_line:
                    break

                current_ws.append([emoji_char[num_in_cat].text, cldr[num_in_cat].text, emoji_base64])
                num_in_cat += 1

        fp.close()

    ## save workbook
    write_wb.save(os.getcwd() + '/emojis.xlsx')


if __name__ == '__main__':
    main()