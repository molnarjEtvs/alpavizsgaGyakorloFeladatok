import os
os.system('cls')
lolNev = input("Adj meg egy hős nevet: ").upper()
alapEro = float(input("Add meg az alap erőt: "))
futasiSebesseg = alapEro*0.225+10
magikusEro = alapEro/2*0.9
print("A hősöd neve: "+lolNev)
print("Futási sebessége: "+str(futasiSebesseg)+" km/h")
print("Mágikus erő: "+str(magikusEro)+" Mp")