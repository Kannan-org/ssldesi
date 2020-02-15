from tinydb import TinyDB, Query, Storage

db = TinyDB("domdb.json")
# dom = input("enter the domain name :  ")
# day = input("days left :  ")
# sig = input("signer:   ")
# hel = input("helath : ")
# enc = input("encrption:   ")
# db.insert({"domain":dom,"days_left":day,"signer":sig,"Health":hel,"enc": enc})
for item in db:
    print(item['domain'])