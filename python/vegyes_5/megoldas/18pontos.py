import random
#osztály létrehozása
class Rendeles:
    #konstruktor vagyis az _init_
    def __init__(self,datum,osszeg,tetelszam):
        #osztályváltozók egyenlővé tétele a bemeneti paraméterekkel:
        self.datum=datum
        self.osszeg=osszeg
        self.termekSzam=tetelszam

    #osztálymetódus készítése:
    def kedvezmenyGeneralas(self):
        kedvezmenyek  = [5,10,12,15]
        self.kedvezmeny = random.choice(kedvezmenyek)

    #osztálymetódus készítése:
    def kedvezmenySzamolas(self):
        self.kedvezmenyForintban=self.osszeg/100*self.kedvezmeny
        self.kedvezmenyesAr=self.osszeg-self.kedvezmenyForintban

#fájl megnyitása olvasásra
f=open("rendelesek.txt","r",encoding="utf-8")
#üres lista létrehozása, hogy legyen mibe tárolnom az adatokat
rendelesek=[]
#a fájl sorain "végig megyek" soronként
for sor in f:
    #sor végéről az enter eltávolítása
    sor=sor[:-1]
    #sor szétválasztása ; karakternél
    d=sor.split(";")
    #a beolvasott sorból készítek egy objektumot (az osztály egy példánya)
    #lényegében itt hívom meg az __init__ metódust:
    rendeles = Rendeles(d[0],int(d[1]),d[2])
    #meghívom az egyik osztály metódust:
    rendeles.kedvezmenyGeneralas()
    #meghívom a másik osztály metódust:
    rendeles.kedvezmenySzamolas()
    #hozzáadom az objektumot a listámhoz
    rendelesek.append(rendeles)
#lezárom a fájlt
f.close()
#ezután következik a fájlba írás.
#a feltöltött lista elemeit kell felhasználni
#fájl megnyitása írásra, a w azt jelenti, hogy ha a fájl nem létezik akkor létre is hozza, ha létezik akkor pedig felülírja a tartalmat
w=open("kedvezmenyek.txt","w",encoding="utf-8")
#végigmegyek egyesével a lista összes elemén
for egyRendeles in rendelesek:
    #kiírom fájlba az adatokat:
    w.write("Rendeles dátuma: "+egyRendeles.datum+"\n")
    w.write("Összeg: "+str(egyRendeles.osszeg)+" Ft\n")
    w.write("Kedvezmény: "+str(egyRendeles.kedvezmeny)+"% -> "+str(egyRendeles.kedvezmenyForintban)+" Ft\n")
    w.write("Végösszeg: "+str(egyRendeles.kedvezmenyesAr)+" Ft\n")
    w.write("---------------------------------\n")
#fájl lezárása
w.close()