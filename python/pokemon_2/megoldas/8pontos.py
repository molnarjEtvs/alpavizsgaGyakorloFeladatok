import os
os.system('cls')
nev=input("Adj meg egy pokemon nevet: ")
ero=int(input("Add meg az erőt: "))
utesiPont=(ero/2)*0.43
rugasiPont=(ero/3)*0.9
print("A pokemon neve: "+nev)
print("Erő: "+str(ero)+" pont")
print("Rugás->"+str(rugasiPont)+" pont, Ütés->"+str(utesiPont)+" pont")