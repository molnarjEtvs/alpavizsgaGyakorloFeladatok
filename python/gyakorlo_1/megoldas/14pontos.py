import os
def bekeres():
    szavak = []
    while True:
        os.system('cls')
        szo = input("Adj meg egy szót: ")
        if len(szo)==0:
            return szavak
        else:
            szavak.append(szo)

def megallapitas(szavak):
    os.system('cls')
    print("Darabszám: "+str(len(szavak))+" db")
    print("Az első szó: "+szavak[0])
    print("Az utolsó szó: "+szavak[len(szavak)-1])

x = bekeres()
megallapitas(x)