import os
#Script tervitab kasutajat tgema operatsioonisüsteemi siselogiminime alusel
print("Tere",os.getlogin())

#Skript kuvab kasutajale praeguse töökatalogi tee
print(os.getcwd())


#Kataloogide loomine:
#Skript küsib kasutajalt, mitu kataloogi ta soovib luua
#Kataloogid luuakse praegusesse töökataloogi kuupäevaga märgistatud kataloogi sees, nummerdatuna (nt “1”, “2”)

mitu=int(input("Mitu kataloogi tahad: "))
today=str(date.today())
try:
    os.mkdir(today)
    for i in range(mitu):
        os.mkdir(today+"/"+str(i+1))
except FileExistsError:
    print(f"Kataloog {today} juba eksisteerib.")