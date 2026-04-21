import codecs
import os
import re


def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()

    with codecs.open("temp.txt", "w") as file:
        file.write(html)

    text_res = ""
    with codecs.open("temp.txt", "r") as file:
        for line in file:
            match = re.search(r'>(.*?)<\/', line)
            if match:
                text_res = text_res + match.group(1) + "\n"

    with codecs.open(result_file, "w") as file:
        file.write(text_res)

    os.remove("temp.txt")


delete_html_tags("draft.html")