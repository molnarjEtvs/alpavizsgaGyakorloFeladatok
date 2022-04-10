import random
class Rendeles:
    def __init__(self,datum,osszeg,tetelszam):
        self.datum=datum
        self.osszeg=osszeg
        self.termekSzam=tetelszam

    def kedvezmenyGeneralas(self):
        kedvezmenyek  = [5,10,12,15]
        self.kedvezmeny = random.choice(kedvezmenyek)

    def kedvezmenySzamolas(self):
        self.kedvezmenyForintban=self.osszeg/100*self.kedvezmeny
        self.kedvezmenyesAr=self.osszeg-self.kedvezmenyForintban

#fájl beolvasása
f=open("rendelesek.txt","r",encoding="utf-8")
rendelesek=[]
for sor in f:
    sor=sor[:-1]
    d=sor.split(";")
    rendeles = Rendeles(d[0],int(d[1]),d[2])
    rendeles.kedvezmenyGeneralas()
    rendeles.kedvezmenySzamolas()
    rendelesek.append(rendeles)
f.close()

#fájlba írás
w=open("kedvezmenyek.txt","w",encoding="utf-8")
for egyRendeles in rendelesek:
    w.write("Rendeles dátuma: "+egyRendeles.datum+"\n")
    w.write("Összeg: "+str(egyRendeles.osszeg)+" Ft\n")
    w.write("Kedvezmény: "+str(egyRendeles.kedvezmeny)+"% -> "+str(egyRendeles.kedvezmenyForintban)+" Ft\n")
    w.write("Végösszeg: "+str(egyRendeles.kedvezmenyesAr)+" Ft\n")
    w.write("---------------------------------\n")
w.close()