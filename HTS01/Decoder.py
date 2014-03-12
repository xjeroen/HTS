__author__ = 'Jeroen'

import re

fileList = open("wordlist.txt", 'r')
enterList = open("enterlist.txt", 'r')
wordList = []
checkList = []
answer = ""

for words in fileList:
    wordList.append(re.sub('\n', '', words))

for words in enterList:
    checkList.append(re.sub('\n', '', words))

for words in checkList:
    for x in wordList:
        match = 0
        if len(x) == len(words):
            tempWords = words
            for l in x:
                for letters in tempWords:
                    if l == letters:
                        match += 1
                        tempWords = tempWords.replace(letters, "", 1)
                        break
            if match == len(words):
                print(words, "-->", x, match)
                answer += x+","

print("\n"+answer[:-1])