from pycrtsh import Crtsh
import datetime
import os
import requests
import json
import subprocess
import time
import string



c = Crtsh()
:
    print(lamp[i])
    certs = c.search("awmdm.tvsmotor.com")
    # print(certs)
    time.sleep(2)
    details = c.get(certs[0]["id"], type="id")
    sub = details['subject']['commonName']
    autho = details['extensions']['authority_information_access']['CA Issuers']
    not_b4 = details['not_before']
    not_after = details['not_after']
    nb = not_b4.strftime('%d-%m-%Y')
    na = not_after.strftime('%d-%m-%Y')
    #----------------------------------------------------------#

    beta = not_after - not_b4
    print("PRinting date things......")
    print(beta)
    #----------------------------------------------------------#

    pubk = details.get('publickey')
    algo = pubk['algorithm']
    pubk['sha256']
    siz = pubk['size']
    issu = details['issuer']['commonName']

# res = subprocess.getoutput(['python3 ~/Documents/proc/sslc/python-ssllabs/ssllabs-cli.py tvsmotor.com |jq \".endpoints[] | [.grade]\"'])
# print(res[5])
    print("--------------------------------------------------------- \n ")
    print(sub) 
    print("--------------------------------------------------------- \n ")
    print(autho)
    print("--------------------------------------------------------- \n ")
    print(issu)
    print("--------------------------------------------------------- \n ")
    print(algo)
    print("--------------------------------------------------------- \n ")
    print(siz)
    print("--------------------------------------------------------- \n ")
    
print("thats all")