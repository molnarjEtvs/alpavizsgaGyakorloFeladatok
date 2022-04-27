import random
class Befizetes:
    def __init__(self,nev,osszeg,darabszam):
        self.nev=nev
        self.osszeg=osszeg
        self.darabszam=darabszam

    def atlagBefizetes(self):
        self.atlag=self.osszeg/self.darabszam
    
    def kedvezmenyVeletlen(self):
        kedvezmenyek=[10,20,30,40]
        self.kedvezmeny=random.choice(kedvezmenyek)
        self.kedvezmenyOsszeg=self.osszeg*(self.kedvezmeny/100)

befizetesek=[]
f=open("befizetesek.txt","r",encoding="utf-8")
for sor in f:
    sor=sor[:-1]
    d=sor.split(",")
    egyBefizetes=Befizetes(d[0],int(d[1]),int(int(d[2])))
    egyBefizetes.atlagBefizetes()
    egyBefizetes.kedvezmenySzamolas()
    befizetesek.append(egyBefizetes)
f.close()

w=open("kimutatas.txt","w",encoding="utf-8")
for egy in befizetesek:
    w.write("Név: "+egy.nev+"\n")
    w.write("Befizetett összeg: "+str(egy.osszeg)+" Ft\n")
    w.write("Átlag befizetés: "+str(egy.atlag)+" Ft\n")
    w.write("Kedvezmény: "+str(egy.kedvezmeny)+" %\n")
    w.write("Kedvezmény összege: "+str(egy.kedvezmenyOsszeg)+" Ft\n")
    w.write("-----------------------------------\n")
w.close()