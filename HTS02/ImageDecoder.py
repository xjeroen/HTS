__author__ = 'root'
from PIL import Image

# I wrote this script to complete HTS programming challenge 2. I wrote it in Python 2.7 so it does not work in Python 3
# The challenge was to obtain a code from an image which were a few dots on a black background. The code was given in
# morse so it also had to be translated back afterwards.

image_file = Image.open("PNG.png")
pix = image_file.load()

print image_file.size

imageList = []
numberList = []
rowCounter = 0
lastNumber = 0
answer = ""
for rows in range(image_file.size[1]):
    imageList.append([])
    for i in range(100):
        imageList[rows].append(pix[i, rows])
        if pix[i, rows] == 1:
            if i < 10:
                numberList.append(str(rows)+"0"+str(i))
            else:
                numberList.append(str(rows)+str(i))

for rows in imageList:
    print rows

print numberList

for numbers in numberList:
    answer += chr(int(numbers)-lastNumber)
    lastNumber = int(numbers)
    print(answer)


print answer

def morsetranslator(s):
    normalString = ""
    morseDict = {".-" : "A", "-...": "B", "-.-." : "C", "-..": "D" , ".": "E", "..-.": "F", "--.": "G", "...." : "H",
                 "..": "I", ".---": "J", "-.-" : "K", ".-..": "L", "--": "M", "-." : "N","---": "O",
                 ".--.": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T", "..-": "U", "...-": "V", ".--": "W",
                 "-..-": "X", "-.--": "Y", "--..": "Z", ".-.-.-": ".", "--..--": ",", "..--..": "?", "-..-.": "/",
                 ".--.-.": "@", ".----": "1", "..---": "2", "...--": "3", "....-": "4", ".....": "5", "-....": "6",
                 "--...": "7", "---..": "8", "----.": "9", "-----": "0"}
    inputList = s.split()
    for x in inputList:
        normalString += morseDict[x]
    return normalString

print morsetranslator(answer)