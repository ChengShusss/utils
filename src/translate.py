#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

import time
import requests




def translate_single_line(line):
    """翻译一行文本，"""
    # url = "https://translate.googleapis.com/translate_a/single"
    url = "https://translate.google.cn/translate_a/single"
    param = {
        "client": "gtx",
        "dt": "t",
        "sl": "en",
        "tl": "zh-CN",
        "q": line
    }
    
    response = requests.get(url, param)

    print(response.headers)
    print(response.text)

    assert response.status_code == 200, ("Get translation of [" + line + "] failed, Status code: " + str(response.status_code))

    res_json = response.json()
    
    assert len(res_json) > 0 and len(res_json[0]) > 0 and len(res_json[0][0]) > 0, (
        "Response struct is out of expection. Response: " + res_json
    )
    
    return res_json[0][0][0]

def translate_text(text):
    lines = text.split('\n')
    res = []
    for line in lines:
        if len(line.strip()) == 0:
            continue
        
        result = translate_single_line(line.strip())
        res.append(result.strip())
        time.sleep(2000)
    
    return ("\n".join(res))



def main():
    text = """ 

    If you spend a lot of time typing plain text, writing programs or HTML, you can save much of that time by using a good editor and using it effectively. This paper will present guidelines and hints for doing your work more quickly and with fewer mistakes.

    The open source text editor Vim (Vi IMproved) will be used here to present the ideas about effective editing, but they apply to other editors just as well. Choosing the right editor is actually the first step towards effective editing. The discussion about which editor is the best for you would take too much room and is avoided. If you don't know which editor to use or are dissatisfied with what you are currently using, give Vim a try; you won't be disappointed.

    [Vim commands and options are printed in this font]
    French translation

        Part 1: edit a file

    1. Move around quickly


    Quite often you will want to search for some text you know is there. Or look at all lines where a certain word or phrase is used. You could simply use the search command /pattern to find the text, but there are smarter ways:

    If you see a specific word and want to search for other occurrences of the same word, use the * command. It will grab the word from under the cursor and search for the next one.
    If you set the 'incsearch' option, Vim will show the first match for the pattern, while you are still typing it. This quickly shows a typo in the pattern.
    If you set the 'hlsearch' option, Vim will highlight all matches for the pattern with a yellow background. This gives a quick overview of where the search command will take you. In program code it can show where a variable is used. You don't even have to move the cursor to see the matches. 
    """

    res = translate_text(text)

    print(res)


if (__name__ == "__main__"):
    main()