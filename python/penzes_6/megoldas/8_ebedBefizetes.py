import os
os.system("cls")
napokSzama=int(input("Add meg a hétköznapok számát: "))
napiDij=int(input("Add meg az egy napi nettó díjat: "))
nettoDij=napokSzama*napiDij
bruttoDij = nettoDij*1.27
print("Napok száma: "+str(napokSzama))
print("Nettó összeg: "+str(nettoDij)+" Ft")
print("Bruttó összeg: "+str(bruttoDij)+" Ft")
