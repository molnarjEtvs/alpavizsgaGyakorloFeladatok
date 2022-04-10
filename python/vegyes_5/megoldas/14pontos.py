import os
os.system('cls')
def allatBekeres():
    allatok = []
    while True:
        allat = input("Add meg az állat nevét: ")
        if len(allat)>0:
            allatok.append(allat)
        else:
            return allatok


def kezdoBetuSzamolas(allatLista):
    a=0
    b=0
    n=0
    for allat in allatLista:
        if allat[0].lower() == "a":
            a+=1
        elif allat[0].lower() == "b":
            b+=1
        else:
            n+=1
    print("Összesen: "+str(len(allatLista))+"db")
    print("a betűvel: "+str(a)+"db")
    print("b betűvel: "+str(b)+"db")
    print("minden más: "+str(n)+"db")
        
a=allatBekeres()
kezdoBetuSzamolas(a)