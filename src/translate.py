#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

import re
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

    # print(response.headers)
    # print(response.text)

    assert response.status_code == 200, ("Get translation of [" + line + "] failed, Status code: " + str(response.status_code))

    res_json = response.json()
    
    assert len(res_json) > 0 and len(res_json[0]) > 0 and len(res_json[0][0]) > 0, (
        "Response struct is out of expection. Response: " + res_json
    )
    
    return res_json[0][0][0]

def translate_text(text):
    lines = re.split(r"\n.!?")
    res = []
    for line in lines:
        if len(line.strip()) == 0:
            continue
        
        result = translate_single_line(line.strip())
        res.append(result.strip())
        time.sleep(2)
    
    return ("\n".join(res))



def main():
    text = """ 
“One of the most persistent fallacies is the reflexive association of wealth with wisdom,” Ed Borgato once wrote.
Wealth might be a sign of good decisions, but can those decisions be repeated? And do good decisions in one field translate to wisdom in other areas of life? Maybe, maybe not – that’s the best we can say. And there are times where exceptional wealth can prevent empathizing with ordinary people, making insight more precarious.
A similar mistake, a bit harder to grasp, is the assumption that smart people have the right answers.
They may. But does intelligence in one field convert to others? Does being good at taking tests translate to, say, leading groups of people?
Maybe. It’s never clear.
And like wealth, there are situations where people become too smart for their own good, where intelligence is a liability and blocks good decisions.
A few causes:
The ability to create complex stories makes it easy to fool people, including yourself.
I know people I would not want to debate with on the question, “What is 2 + 2?” because they could go down a rabbit hole that’s over my head and leave me either exhausted or convinced the answer may not be four.
The dangerous thing is that those people can do the same things to themselves.
Richard Feynman said, “The first principle is that you must not fool yourself — and you are the easiest person to fool.” The smarter you are I think the truer that becomes.
When you’re blessed with intelligence you’re cursed with the ability to use it to concoct intricate stories about why things happened – especially stories justifying why you made a mistake or why you’ll eventually be right in an area you’re wrong.
The big blowups in any field aren’t typically caused by a lack of smarts. The catastrophes are typically caused by extreme intelligence that causes people to believe their own dangerous stories – that you can predict with accuracy, use leverage because your prediction must be true, and ignore warning signs that would have been obvious to a normal person who’s less adept at mental gymnastics
What’s boring is often important and the smartest people are the least interested in what’s boring.
Ninety percent of personal finance is just spend less than you make, diversify, and be patient.
But if you’re very intelligent that bores you to tears and feels like a waste of your potential. You want to spend your time on the 10% that’s mentally stimulating.
Which isn’t necessarily bad. But if your focus on the exciting part of finance comes at the expense of attention to the 90% of the field that’s boring, it’s disastrous. Hedge funds blow up and Wall Street executives go bankrupt doing things a less intelligent person would never consider. A similar thing happens in medicine, a field that attracts brilliant people who may be more interested in exciting disease treatments than boring disease prevention.
There’s a sweet spot where you grasp the important stuff but you’re not smart enough to be bored with it.
Intelligence can make it difficult to communicate with ordinary people, who may have the missing insight you’re looking for.
How many academics have discovered something amazing, but wrote it in a paper so dense and complex that no one else can understand it?
And how many ordinary people would be able to bring an academic’s discovery into the real world if they could understand what was written in those papers?
It has to be so many.
Computer scientist Edsger Dijkstra once wrote:
    [Complexity has] a morbid attraction. When you give an academic audience a lecture that is crystal clear from alpha to omega, your audience feels cheated and leaves the lecture hall commenting to each other: “That was rather trivial, wasn’t it?” The sore truth is that complexity sells better.
When complexity is the preferred language of very smart people, great ideas can become walled off from ordinary people. Most of the allure of the information age is that ideas can be shared among huge groups of people. But among the superintelligent, that’s often not the case – they’re speaking a different language.
Occasionally someone like Richard Feynman comes along, whose storytelling skills equal his genius. But it’s rare. Communication and intelligence are not just separate skills; they can repel each other, and the smarter you become the more complex your communication and the smaller the audience you may be able to persuade.
The key, like so many things, is respecting balance and diverse views.
    """

    res = translate_text(text)

    print(res)


if (__name__ == "__main__"):
    main()