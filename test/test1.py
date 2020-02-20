import requests
from requests.exceptions import ConnectionError
import time
from bs4 import BeautifulSoup
import os
file1 = open('tvsm.txt', 'r') 

Lines = file1.readlines()

lamp = list(map(lambda x:x.strip(),Lines))

print(lamp)

for i in range(0, len(lamp)):
  
  
    domanin_name = str(lamp[i])
    print(domanin_name)
    url = "https://www.sslshopper.com/ssl-checker.html#hostname=https://"+domanin_name+"/"
    print(url)
    resp=requests.get(url)
    time.sleep(5)
    if resp.status_code==200: 
    
        soup=BeautifulSoup(resp.text,'html.parser')	 
        for foo in soup.find_all('table', attrs={'class': 'checker_messages'}):
            try:
                bar = foo.find('td', attrs={'class': 'passed'})
                print("Theere is a website and data aare follewee..........")
            except:
                bar1 = foo.find('td',attrs={'class':'failed'})
                print("no website data availbale....")
                
    else:
        print("Website unavailable.....")

