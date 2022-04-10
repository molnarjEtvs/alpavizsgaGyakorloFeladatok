import os
os.system('cls')
szel=int(input("Add meg a szoba szélességét méterben: "))
hosz=int(input("Add meg a szoba hosszúságát méterben: "))
nmAr=int(input("Add meg a burkolás egy m2 árát forintban: "))
nm = (szel*hosz)
ar=nm*nmAr*1.1
print("A szoba "+str(nm)+"m2, burkolási költsége: "+str(ar)+" Ft")