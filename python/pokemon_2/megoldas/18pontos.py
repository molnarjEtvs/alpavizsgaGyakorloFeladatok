import random
import os
class Pokemon:
    def __init__(self,dex,nev,ero):
        self.dex=dex
        self.nev=nev
        self.ero=ero
        self.ugrasiMagassag=0

    def setUgrasiMagassag(self):
        self.ugrasiMagassag = self.ero/3*0.885

    def kepessegGenerator(self):
        kepessegek=["párolgás","tűzhányás","lövés","gurulás"]
        rnd = random.randint(0,len(kepessegek)-1)
        self.kepesseg=kepessegek[rnd]


os.system("cls")
f=open("pokemonLista.txt","r",encoding="UTF-8")
pokemonok=[]
for sor in f:
    sor=sor[:-1]
    x=sor.split(",")
    pok = Pokemon(x[0],x[1],int(x[2]))
    pok.kepessegGenerator()
    pok.setUgrasiMagassag()
    pokemonok.append(pok)
f.close()
print("Adatok feldolgozva")


i=open("pokemonjaim.txt","w",encoding="UTF-8")
for egyPokemon in pokemonok:
    i.write("Dex szám #: "+egyPokemon.dex+"\n")
    i.write("Név: "+egyPokemon.nev+"\n")
    i.write("Erő: "+str(egyPokemon.ero)+" pont\n")
    i.write("Képesség: "+egyPokemon.kepesseg+"\n")
    i.write("Ugrási magasság: "+str(egyPokemon.ugrasiMagassag)+"m\n")
    i.write("---------------------------------"+"\n")
i.close()
print("Fájlba írás kész")
    


