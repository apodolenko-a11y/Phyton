import json
import requests

url="https://dummyjson.com/recipes"
response= requests.get(url)
andmed= response.json()
retseptid=andmed["recipes"]


#alla 30 min
retseptid30 =[]
koostisosadmax =0
maxretsept =""
koguaeg =0
kokku =0

#kõige rohkem kostisosi
for retsept in retseptid:
    print(retsept["name"],retsept["cookTimeMinutes"])

    if retsept["cookTimeMinutes"] < 30:
        retseptid30.append(retsept["name"])
        #print ("lisatud alla 30")


    if len(retsept["ingredients"]) >koostisosadmax:
        koostisosadmax=len(retsept["ingredients"])
        maxretsept=retsept["name"]
        #print("uus retsept")

#keskm. aeg
koguaeg+=retsept["cookTimeMinutes"]
kokku += 1
#print("koguaeg:",koguaeg)

print("alla 30 minuti retseptid:")
for ret30 in retseptid30:
    print(ret30)
    #print("kontoll")

print("kõige rohkem koostisosi:")
print(maxretsept,koostisosadmax)

if kokku >0:
    print("keskmine aeg:")
    print(koguaeg /kokku)

#else:
    #print("vale")


