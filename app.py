
# Python tool for checking SSL server side validity.    #
#                                                       #
# Soly Framework built by Kannan and Work done by Pooja #
#                                                       #
# This project is only a Prototype and the main         #
# production project will be soon deployed and prop     #
#                                                       #
# Please Support The Project                            #

""" The Documentation of the Program goes here:
          This program is simple flask based web framework program.
          This can check for SSL validyty health and some other stuffs
          The program uses API call from crt.sh and a api is being created using [ME]
          The api call for th ehealth of domain
          For more development PLease do look into th eprogram cmmnet line and map it with the commnet file in the folder.
          PLease do not delete or comment any line as the append and api call have been crafted acoordingly...... """

import requests
from flask import Flask, render_template
from requests.exceptions import ConnectionError
import time
from bs4 import BeautifulSoup
from pycrtsh import Crtsh
import os 

app = Flask(__name__)



urls ='http://ns.tools/'



file1 = open('tvsm.txt', 'r') 

Lines = file1.readlines()

lamp = list(map(lambda x:x.strip(),Lines))

print(lamp)


c = Crtsh()

tok = os.urandom(32)

print(tok)


new_data = []


for i in range(0, len(lamp)):
  
  
    domanin_name = str(lamp[i])
    print(domanin_name)
    
    try:
      
        request = requests.get("https://"+lamp[i])
        
                
    except ConnectionError:
      
        print("website not available............")
        data = [{
                      "domain": domanin_name,
                      "day_left": "No data available",
                      "Encryption": "No data available",
                      "Health": "No data Available",
                      "signer": "No data available.."
                    }]
        
        
        new_data.append(data[0])
        
    else:
        
        print("website available.................")
        certs = c.search(lamp[i])
        
        time.sleep(1)
        
        try:
          details = c.get(certs[0]["id"], type="id")
            
          time.sleep(2)
          
          sub = details['subject']['commonName']
          
          autho = details['extensions']['authority_information_access']['CA Issuers']
          
          not_b4 = details['not_before']
          
          not_after = details['not_after']
          
          not_b4.strftime('%d-%m-%Y')
          
          not_after.strftime('%d-%m-%Y')
          
          day = not_after - not_b4
          
          days = str(day)
          
          pubk = details.get('publickey')
          
          algo = pubk['algorithm']
          
          pubk['sha256']
          
          siz = str(pubk['size'])
          
          issu = details['issuer']['commonName']
          
          enc = algo + siz
          
          url = urls+lamp[i]
          
          resp=requests.get(url) 
          
          time.sleep(5)
          
          
          if resp.status_code==200: 

 
              
              soup=BeautifulSoup(resp.text,'html.parser')	 
              
              l=soup.find("span",{"class":"__score-title"})
              
              dns=soup.find("div",{"id":"score__dns__disp"})
              
              domain=soup.find("div",{"id":"score__domain__disp"})
              
              mail=soup.find("div",{"id":"score__mail__disp"})
              
              web=soup.find("div",{"id":"score__web__disp"})
              
              score=soup.find("span",{"itemprop":"ratingValue"})
              
              data = [{
                      "domain": str(sub),
                      "day_left": str(days),
                      "Encryption": str(enc),
                      "Health": str(score),
                      "signer": str(issu)
                    }]
              
              
              new_data.append(data[0])
          
          
          else:
            
            data = [{
                      "domain": domanin_name,
                      "day_left": "No data available",
                      "Encryption": "No data available",
                      "Health": "No data Available",
                      "signer": "No data available.."
                    }]  
            
            
            new_data.append(data)
        
        
        except IndexError:
          
          print("No certs available for this websites.................")
          data = [{
                      "domain": domanin_name,
                      "day_left": "No data available",
                      "Encryption": "No data available",
                      "Health": "No data Available",
                      "signer": "No data available.."
                    }]
          
          
          
          
          new_data.append(data[0])



columns = [
  {
    "field": "domain", # which is the field's name of data key 
    "title": "Domain", # display as the table header's name
    "sortable": True, 
  },
  {
    "field": "day_left",
    "title": "Days Left",
    "sortable": True,
  },
  {
    "field": "Encryption",
    "title": "Encryption",
    "sortable": True,
  },
  {
    "field": "Health",
    "title": "Health",
    "sortable": True,
  },
  {
    "field": "signer",
    "title": "Cert Signer",
    "sortable": True,
  },
]




@app.route('/')

def index():
    
    
    return render_template("table.html",
      data=new_data,
      columns=columns,
      title='SSL Check Validity Dashboard[prototype]')



if __name__ == '__main__':
  
  print("\x56\x47\x68\x70\x63\x79\x42\x70\x63\x79\x42\x68\x49\x48\x42\x79\x62\x32\x64\x79\x59\x57\x30\x67\x64\x47\x68\x68\x64\x43\x42\x33\x59\x58\x4d\x67\x59\x6e\x56\x70\x62\x48\x51\x67\x59\x6e\x6b\x67\x53\x32\x46\x75\x62\x6d\x46\x75\x49\x45\x63\x67\x57\x31\x56\x53\x4d\x54\x56\x44\x55\x7a\x41\x35\x4f\x56\x30\x67\x59\x57\x35\x6b\x49\x48\x42\x76\x62\x32\x70\x68\x4c\x69\x42\x7a\x62\x79\x42\x33\x61\x47\x38\x67\x5a\x58\x5a\x6c\x63\x69\x42\x6d\x61\x57\x35\x6b\x49\x48\x52\x6f\x61\x58\x4d\x67\x65\x57\x39\x31\x49\x47\x68\x68\x64\x6d\x55\x67\x64\x47\x38\x67\x61\x32\x35\x76\x64\x79\x42\x70\x64\x48\x4d\x67\x62\x6d\x39\x30\x49\x47\x46\x75\x62\x32\x35\x6c\x49\x47\x56\x73\x63\x32\x55\x75")
  # Has64X
  app.run(debug=True)