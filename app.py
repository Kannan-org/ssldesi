from flask import Flask, render_template
import json
from pycrtsh import Crtsh
import pprint
import datetime
import os
import requests
import subprocess
import time

"""
A example for creating a Table that is sortable by its header
"""

app = Flask(__name__)
c = Crtsh()
file1 = open('tvsm.txt', 'r') 
Lines = file1.readlines()
lamp = list(map(lambda x:x.strip(),Lines))
for i in range(0, len(lamp)):
  print(lamp[i])
  certs = c.search(lamp[i])
  # print(certs)
  time.sleep(2)
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
# res = subprocess.getoutput(['python3 ~/Documents/proc/sslc/python-ssllabs/ssllabs-cli.py --use-cache elearning.tvsmotor.com |jq \".endpoints[] | [.grade]\"'])
  hel = "A"
  data = [{
    "domain": sub,
    "day_left": days,
    "Encryption": enc,
    "Health": hel,
    "signer": issu
  }]
# other column settings -> http://bootstrap-table.wenzhixin.net.cn/documentation/#column-options
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
      data=data,
      columns=columns,
      title='SSL Check Validity Dashboard[prototype]')


if __name__ == '__main__':
  app.run(debug=True)