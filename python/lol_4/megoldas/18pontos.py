import random

class lolHos:
    def __init__(self,az,nev,tipus,stilus):
        self.az=az
        self.nev=nev
        self.tipus=tipus
        self.serules=stilus
    
    def setNehezsegiSzint(self,nf):
        if nf=="1":
            self.nsz="Easy"
        elif nf=="2":
            self.nsz="Medium"
        else:
            self.nsz="Hard"

    def setKepesseg(self):
        kepessegek=["átokszórás","végítélet","halál","bájolás"]
        self.kepesseg=random.choice(kepessegek)

f=open("hosok.hsk","r",encoding="UTF-8")
hoseim=[]
for sor in f:
    sor=sor[:-1]
    ertek=sor.split("|")
    hos = lolHos(ertek[0],ertek[1],ertek[2],ertek[3])
    hos.setNehezsegiSzint(ertek[4])
    hos.setKepesseg()
    hoseim.append(hos)
f.close()

fw=open("hoseim.txt","w",encoding="UTF-8")
for egyHos in hoseim:
    fw.write("Azonosító: #"+egyHos.az+"\n")
    fw.write("Hős neve: "+egyHos.nev+"\n")
    fw.write("Nehézségi szint: "+egyHos.nsz+"\n")
    fw.write("Képesség: "+egyHos.kepesseg+"\n")
    fw.write("#####################################\n")
fw.close()