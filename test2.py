import requests
from requests.exceptions import ConnectionError
from huepy import *


file1 = open('tvsm.txt', 'r') 
Lines = file1.readlines()
lamp = list(map(lambda x:x.strip(),Lines))
# print(lamp)
for i in range(0, len(lamp)):
    print(lamp[i])
    try:
        request = requests.get("https://"+lamp[i])
    except ConnectionError:
        print(red('Web site does not exist......'))
    else:
        print(green('Web site exists.......'))