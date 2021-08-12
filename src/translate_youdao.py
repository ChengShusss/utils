#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import sys
import uuid
import requests
import hashlib
import time
import json
from imp import reload

from translate import translate_single_line

reload(sys)

YOUDAO_URL = 'https://openapi.youdao.com/api'
APP_KEY = '0a9281ed3866a819'
APP_SECRET = 'bTkkslWGOxuCNUi0k4OjUImMcA1ls9nX'


def encrypt(signStr):
    hash_algorithm = hashlib.sha256()
    hash_algorithm.update(signStr.encode('utf-8'))
    return hash_algorithm.hexdigest()


def truncate(q):
    if q is None:
        return None
    size = len(q)
    return q if size <= 20 else q[0:10] + str(size) + q[size - 10:size]


def do_request(data):
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    return requests.post(YOUDAO_URL, data=data, headers=headers)

def decode_response(data):
    """从返回值中解析出结果"""
    assert len(data) > 0, "Response is null."
    dic = json.loads(data.decode())

    assert 'translation' in dic, "Response does not contain result."
    assert len(dic['translation']) > 0, "No result."

    
    return (dic["translation"][0])


def translate(text):

    data = {}
    data['from'] = 'en'
    data['to'] = 'zh-CNS'
    data['signType'] = 'v3'
    curtime = str(int(time.time()))
    data['curtime'] = curtime
    salt = str(uuid.uuid1())
    signStr = APP_KEY + truncate(text) + salt + curtime + APP_SECRET
    sign = encrypt(signStr)
    data['appKey'] = APP_KEY
    data['q'] = text
    data['salt'] = salt
    data['sign'] = sign
    # data['vocabId'] = "您的用户词表ID"

    response = do_request(data)
    translate_result = decode_response(response.content)

    return translate_result


if __name__ == '__main__':
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
    res = translate(text)

    print(res)