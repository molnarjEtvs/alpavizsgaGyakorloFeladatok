import os
os.system('cls')
bruttoFizetes = float(input("Add meg a Bruttó fizetésed: "))
szja=bruttoFizetes*0.15
tb=bruttoFizetes*0.185
szocHo=bruttoFizetes*0.13

nettoFizetes=bruttoFizetes-szja-tb
munkaltatoKoltsege=bruttoFizetes+szocHo

os.system('cls')
print("A nettó fizetésed: "+str(nettoFizetes)+" Ft")
print("Levonásra kerül:")
print("Szja: "+str(szja))
print("Tb: "+str(tb))
print("Ez a munkáltatódnak: "+str(munkaltatoKoltsege)+" Ft-ba kerül!")


