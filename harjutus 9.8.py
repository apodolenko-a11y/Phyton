# #9.8
# import random
# for i in range(11):
#     print(f"{i} * {i} = {i*i}")
#     
#     
# #9.9
# tehe = ["+","-","*","/"]
# 
# for _ in range(10):
#     arv1 = random.randint(1,10)
#     arv2 = random.randint(1,10)
#     t =random.choice(tehe)
#     
#     
# if t=="+":
#     print(f"{arv1}{t}{arv2}=")
#     v = int(input("Vastus: "))
#     if arv1+arv2 ==v:
#         punktid+=1
#     
# elif t=="-":
#     print(f"{arv1}{t}{arv2}=")
#     v = int(input("Vastus: "))
#     if arv1+arv2 ==v:
#         punktid+=1
# elif t=="*":
#     print(f"{arv1}{t}{arv2}=")
#     v = int(input("Vastus: "))
#     if arv1+arv2 ==v:
#         punktid+=1
# elif t=="/":
#     print(f"{arv1}{t}{arv2}=")
#     v = float(input("Vastus: "))
#     if round(arv1/arv2,1) ==v:
#         punktid+=1
# print(f"A-{kysimuste_arv}-{punktid}-{punktid/kysimuste_arv}")
# if kysimuste_arv/punktid >=0.5:
#     print(f"A{punktid}/{kysimuste_arv}")
#     
# else:
#     print(f"MA-{punktid}/{kysimuste_arv}")
# #1    
# for _ in range(1,6):
#     print(" " * i + "*" * arv)
#     arv-=1
#     
# #2
# for i in range(1,6):
#     print("*" * i )
#     
# #3
# arv = 5
# for i in range(1,6):
#     print(" " * arv + "*" * i)
#     arv-=1
#     
# #4
# for i in range(1,6):
#     print("*" * i)
#     
# #9.12
# summa = 0
# even_nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 3, 32, 34, 36, 38]
# for i in even-nums:
#     summa+=1
# print(summa)



#9.13
print("")
autode_hind = 0
autode_hind_kokku = 0

ev_data = [
['vehicle', 'range', 'price'],
['Tesla Model Y Long Range', '330', '58990'],
['Volkswagen ID.4 Pro', '260', '39995'],
['Ford Mustang Mach-E', '300', '42995'],
['Audi e-tron GT', '238', '102700'],
['Nissan Leaf', '149', '27400'],
['BMW iX xDrive50', '324', '83995'],
['Polestar 2', '265', '45500'],
['Kia EV6 Long Range', '310', '47795'],
['Mercedes-Benz EQS 450+', '350', '102310'],
['Hyundai Kona Electric', '258', '37400']
]

for i in ev_data:
   print(f"{i[0]:26} {i[1]:6} {i[2]:8}") 

for i in range(1,len(ev_data)):
    autode_hind+=int(ev_data[i][2])
    autode_hind_kokku+=1
    
# print(f"keskmine ulatus:(range_summa/range_kokku")
print(f"keskmine summa: {autode_hind/autode_hind_kokku}")
print("--------------")


max_koef = 100000000
parim_auto = ""

for i in range(1,len(ev_data)):
    koef = int(ev_data[i][2])/int(ev_data[i][1])
    if koef<max_koef:
        max_koef = koef
        parim_auto=ev_data[i][0]
        
print(max_koef)
print(parim_auto)


        
    