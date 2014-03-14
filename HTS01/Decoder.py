__author__ = 'Jeroen'

import re

# I made this script to unscramble words which were randomly taken from a wordlist.
# The answer had to be given in the format : word1,word2,word3 etc.
# I managed to complete the challenge with this script , however there is still a bug in it.

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