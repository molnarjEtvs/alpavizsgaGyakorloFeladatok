import os
os.system("cls")
def zsebpenzBekeres():
    zsebpenzLista=[]
    while True:
        zsebpenz=input("Mennyi zsebpénzt kaptál?: ")
        if len(zsebpenz)>0:
            zsebpenzLista.append(zsebpenz)
        else:
            return zsebpenzLista

def kimutatas(osszegek):
    osszesen=0
    db=len(osszegek)
    for egyOsszeg in osszegek:
        osszesen+=int(egyOsszeg)
    atlag=osszesen/db
    print("Ennyi zsebpénzed van: "+str(osszesen)+" Ft")
    print(str(db)+" db befizetésed volt.")
    print("Átlagosan: "+str(atlag)+" Ft-ot fizettél be")

fizetesek=zsebpenzBekeres()
kimutatas(fizetesek)