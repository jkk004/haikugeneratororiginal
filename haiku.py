import random
import re
import requests

haiku1 = ""
haiku2 = ""
haiku3 = ""

n = 5
start = 0
while n != 0:
    word = ""
    tally = 0
    #if n == 5:
       # choice = random.randint(1,n-1)
    #else:
    choice = random.randint(1, n)
    if choice == 1:
        page = random.randint(1,156)
    if choice == 2:
        page = random.randint(1,744)
    if choice == 3:
        page = random.randint(1,882)
    if choice == 4:
        page = random.randint(1,655)
    if choice == 5:
        page = random.randint(1,156)
    link = "https://syllablewords.net/" + str(choice) + "-syllable-words?page=" + str(page)
    f = requests.get(link)
    #print(f.text)
    res = [m.start() for m in re.finditer('col-12', f.text)]
    resChoice = random.randint(0, len(res) - 1)
    pick = res[resChoice] + 8
    while tally == 0:
        if f.text[pick] != "<":

            word += f.text[pick]
            pick += 1
        else:
            tally = 1
    if start == 0:
        word = word.capitalize()
        haiku1 += word
        start = 1
    else:
        haiku1 += " "
        haiku1 += word
    n -= choice
    if n == 0:
        haiku1 += ","
    #"word" > a
    #col-12"

n = 7
start = 0
while n != 0:
    word = ""
    tally = 0
    #if n == 5:
       # choice = random.randint(1,n-1)
    #else:
    choice = random.randint(1, n)
    if choice == 1:
        page = random.randint(1,156)
    if choice == 2:
        page = random.randint(1,745)
    if choice == 3:
        page = random.randint(1,882)
    if choice == 4:
        page = random.randint(1,655)
    if choice == 5:
        page = random.randint(1,156)
    if choice == 6:
        page = random.randint(1,156)
    if choice == 7:
        page = random.randint(1,44)
    link = "https://syllablewords.net/" + str(choice) + "-syllable-words?page=" + str(page)
    f = requests.get(link)
    #print(f.text)
    res = [m.start() for m in re.finditer('col-12', f.text)]
    resChoice = random.randint(0, len(res) - 1)
    pick = res[resChoice] + 8
    while tally == 0:
        if f.text[pick] != "<":

            word += f.text[pick]
            pick += 1
        else:
            tally = 1
    if start == 0:
        word = word.capitalize()
        haiku2 += word
        start = 1
    else:
        haiku2 += " "
        haiku2 += word
    n -= choice
    if n == 0:
        haiku2 += ","


n = 5
start = 0
while n != 0:
    word = ""
    tally = 0
    #if n == 5:
       # choice = random.randint(1,n-1)
    #else:
    choice = random.randint(1, n)
    if choice == 1:
        page = random.randint(1,156)
    if choice == 2:
        page = random.randint(1,744)
    if choice == 3:
        page = random.randint(1,882)
    if choice == 4:
        page = random.randint(1,655)
    if choice == 5:
        page = random.randint(1,156)
    link = "https://syllablewords.net/" + str(choice) + "-syllable-words?page=" + str(page)
    f = requests.get(link)
    #print(f.text)
    res = [m.start() for m in re.finditer('col-12', f.text)]
    resChoice = random.randint(0, len(res) - 1)
    pick = res[resChoice] + 8
    while tally == 0:
        if f.text[pick] != "<":

            word += f.text[pick]
            pick += 1
        else:
            tally = 1
    if start == 0:
        word = word.capitalize()
        haiku3 += word
        start = 1
    else:
        haiku3 += " "
        haiku3 += word
    n -= choice
    if n == 0:
        haiku3 += "."

print(haiku1)
print(haiku2)
print(haiku3)
