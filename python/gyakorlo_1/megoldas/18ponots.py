import os
class Ajto:
    def __init__(self,tipus,szin):
        self.tipus=tipus
        self.szin=szin
        self.ajtoNegyzetMeterAr=6000
    
    def saveAjtoMeret(self,szelesseg,magassag):
        self.szelesseg=szelesseg
        self.magassag=magassag

    def genAjtoAra(self):
        self.ar = (self.szelesseg/100)*(self.magassag/100)*self.ajtoNegyzetMeterAr

os.system("cls")
f=open("ajtok.lst","r",encoding="UTF-8")
ajtok=[]
for sor in f:
    sor=sor[:-1]
    x=sor.split(";")
    ajto = Ajto(x[0],x[1])
    ajto.saveAjtoMeret(int(x[2]),int(x[3]))
    ajto.genAjtoAra()
    ajtok.append(ajto)
f.close()
print("Adatok feldolgozva")


i=open("arajanlat.txt","w",encoding="UTF-8")
for egyAjto in ajtok:
    i.write("Ajtó típusa: "+egyAjto.tipus+"\n")
    i.write("Ajtó ára: "+ str(egyAjto.ar)+" Ft"+"\n")
    i.write("Méret: "+str(egyAjto.szelesseg)+"x"+str(egyAjto.magassag)+" cm"+"\n")
    i.write("---------------------------------"+"\n")
i.close()
print("Fájlba írás kész")