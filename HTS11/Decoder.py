__author__ = 'Jeroen'

import re
import urllib.parse
import urllib.request
import http.cookiejar

# This script was made for HTS programming challenge 11, it reverses a simple cipher text.
# The script logs me in on the website, goes to the correct page and obtains the cipher and shift.
# Afterwards it decodes it and inputs it on the site, completing the challenge in less than 3 seconds.

username = "username"
password = "password"
phpSESSID = ""

cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
login_data = urllib.parse.urlencode({'username': username, 'password': password})
binary_data = login_data.encode('ascii')
opener.open("https://www.hackthissite.org/user/login", binary_data)
opener.addheaders.append(('Cookie', phpSESSID))
resp = opener.open("https://www.hackthissite.org/missions/prog/11/")

URLString = resp.read().decode("utf-8")
encodedString = re.search(r'Generated String: (.*?<)', URLString, re.I | re.M)
encodedString = encodedString.group(1)[:-1]
shift = re.search(r'Shift: (.*?<)', URLString, re.I | re.M)
shift = int(shift.group(1)[:-1])

stringLst = re.sub(r'[^0-9]', "$", encodedString)
stringLst = stringLst.split("$")[:-1]
value = ""
for x in stringLst:
    value += chr(int(x)-shift)

print(value)
query_args = {'solution': value}
data = urllib.parse.urlencode(query_args)
binData = data.encode('ascii')
opener.addheaders.append(('Referer', 'http://www.hackthissite.org/'))
try11 = opener.open("https://www.hackthissite.org/missions/prog/11/index.php", binData)
print(try11.read())
