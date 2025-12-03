#Kordamine 1
#Anastasiia 26.11.25
inim = 80
kohad = 40

tais = inim // kohad
yle = inim % kohad

if yle == 0:
    lisa_buss = 0
else:
    lisa_buss = 1

busse_kokku = tais + lisa_buss

print(f"Täis busse: {tais}")
print(f"Viimases: {yle}")
print(f"Busse kokku: {busse_kokku}")











print("Tere maailm!")
aasta = 2020
liblikas = "teelehe-mosaiikliblikas"
lause_keskosa = ". aasta liblikas on"
lause = str(aasta) + lause_keskosa + liblikas
print(lause)

try:
    korgus = float(input("Sisesta pilvede kõrgus: "))
    if korgus > 6.0:
        print("Need on ülemised pilved")
    else:
        print("Need ei ole ülemised pilved")
except:
    print("urror-Nimfa")