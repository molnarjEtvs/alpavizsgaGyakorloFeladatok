import os
os.system("cls")
a = int(input("Add meg az óraállásod 1: "))
b = int(input("Add meg az óraállásod 2: "))
c = int(input("Hány liter benzint tankoltál: "))
benzinAr = float(input("Benzin literenkénti ára: "))
tavolsag=b-a
atlagFogyasztas = (c/(b-a))*100
koltseg=(b-a)/100*benzinAr

print("Megtett távolság: "+str(tavolsag)+" km")
print("Az átlagfogyasztásod: "+str(atlagFogyasztas)+" liter/100 km")
print("Ez az utad "+str(koltseg)+" Ft-ba került!")