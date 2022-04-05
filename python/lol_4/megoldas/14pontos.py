import os
os.system('cls')
def hosRogzites():
    hosok=[]
    while True:
        hosNev=input("Hős neve: ")
        if len(hosNev)!=0:
            hosok.append(hosNev)
        else:
            return hosok

def hosErtekeles(h):
    harom=""
    ot=""
    hatNagyobb=""
    for egy in h:
        if len(egy)<=3:
            harom+=egy+", "
        elif len(egy)<=5:
            ot+=egy+","
        else:
            hatNagyobb+=egy+", "
    print("Hősök száma: "+str(len(h))+" db")
    print("Három betűsek: "+harom)
    print("Ötbetűsek: "+ot)
    print("Hat és több betűsek: "+hatNagyobb)

hosLista = hosRogzites()
hosErtekeles(hosLista)