import os
os.system('cls')
def pokemonRogzites():
    pokemonLista=[]
    while True:
        nev=input("Add meg a pokemon nevét: ")
        if len(nev)==0:
            return pokemonLista
        else:
            pokemonLista.append(nev)

def kiErtekeles(adat):
    db=len(adat)
    print("Rögzített adatok száma: "+str(db))
    csek=""
    bsek=""
    egyeb=""
    for nev in adat:
        if nev[0]=="b":
            csek+=nev+", "
        elif nev[0] =="c":
            bsek+=nev+", "
        else:
            egyeb+=nev+", "
    print("B betűsek: "+csek)
    print("C betűsek: "+bsek)
    print("Minden más: "+egyeb)
    
pokemonok=pokemonRogzites()
kiErtekeles(pokemonok)