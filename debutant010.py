print("saisir le nombre de fois")
print("")

nombre=input("saisir le nombre totale :")
nombre=int(nombre)
print("")

for i in range(1,nombre) :
    print("saisir le nombre", i,":")
    chiffre=input("")
    chiffre=int(chiffre)
    
    if chiffre >= 0:
        print("le nombre saisr est positive")
        print("")
        
    else :
        print("le nombre saisr est negative")
        print("")
    
    
    