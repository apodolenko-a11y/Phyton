# Ülesanne 5
# Anastasiia 26.11.25
import random
#5.3 Maatematika test (randint)
arv1 = random.randint(1,10)
arv2 = random.randint(1,10)
vastus = int(input(f"{arv1} * {arv2} =  "))
if vastus == arv1 * arv2:
    print("Õige")
else:
    print("Nõrk oled!")

#5.1 Vanusepiiranguga üritus
piirang = 18
vanus = int(input("Sisesta oma vanus: "))

if vanus >=piirang:
    print("Saab sisse!")
else:
     print("Ei saa sisse!")
     