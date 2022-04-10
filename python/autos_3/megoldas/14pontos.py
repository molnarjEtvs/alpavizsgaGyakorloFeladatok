import random
import os
os.system("cls")
def generalas():
    myList=[]
    while len(myList)<11:
        rnd = random.randint(1,5000)
        if rnd%2==0:
            myList.append(rnd)
    return myList

def feldolgoz(x):
    a=""
    b=""
    c=""
    for elem in x:
        if elem>=0 and elem<=1000:
            a+=str(elem)+", "
        elif elem>1000 and elem<3000:
            b+=str(elem)+", "
        else:
            c+=str(elem)+", "
    print("0 és 1000 között: "+a)
    print("1001 és 3000 között: "+b)
    print("3000 felett: "+c) 
    
szamok=generalas()
feldolgoz(szamok)