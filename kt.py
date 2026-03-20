import json
import requests
from datetime import datetime

url = f"https://metshein.com/kordamine/json/uritused.json"

#loeme andmed
andmed= requests.get(url).json()
uritused=andmed["uritused"]

#kui palju üritus Tallinnas
arv_tallinn=0
for sundmus in uritused:
    if sundmus["koht"]=="Tallinn":
        arv_tallinn=arv_tallinn + 1
print("Tallinas üritusi:",arv_tallinn)

#prazdniki posle 18:00
for sundmus in uritused:
    if sundmus["kellaaeg"] >= "18:00":
        print(sundmus["nimetus"], sundmus["kellaaeg"])
        
#kuu,gde bolshe vsego üritusi
kuu_loendur={}
for sundmus in uritused:
    kuu=sundmus["kuupäev"].split("-")[1]
    if kuu in kuu_loendur:
        kuu_loendur[kuu]= kuu_loendur[kuu] + 1
    else:
        kuu_loendur[kuu] = 1
max_kuu = max (kuu_loendur, key=kuu_loendur.get)
print("Kõige rohkem üritusi kuus:", max_kuu)

