print("")
print("trions le tableau")
print("")

table=[]

for i in range(10) :
    print("sasir le nombre",i+1," : ",end="")
    nombre1=int(input(""))
    table.append(nombre1)
    
liste=table[0:]
chiffre=nombre1%2

for n in liste :
    if n>=0  and chiffre==0:
        liste.index(n)
        print("la valeur minimal est: ",min(liste))  
        print("la position est : ", liste.index(n))
    elif n>=0 and chiffre>0 :
        continue
    else :
        print("erreur de la saisir des valeurs !!!!....pas de saisir negative")
        break
        
    
    