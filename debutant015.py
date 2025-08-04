print("facture SODECI")
print("")
print("saisr le nombre d'abonné : ",end="")
nombre=input("")
nombre=int(nombre)
print("")

for i in range(1,nombre) :
    print("nom et prenom de l'abonné",i," : ",end="")
    person=input("")
    person=str(person)
    print("saisir la consommation : ",end="")
    consommation=input("")
    consommation=int(consommation)
    
    if consommation<=50 :
        ht=100*consommation
        print("le montant hors taxe est de : ",ht)
        ttc=(ht*18)/100 + 10000
        print("le prix net à payer : ",ttc)
        print("")
        
    elif consommation>50 and consommation<=150 :
        ht=50*consommation
        print("le montant hors taxe est de : ",ht)
        ttc=(ht*18)/100 + 10000
        print("le prix net à payer : ",ttc)
        print("")
        
    elif consommation>150 and consommation<=300 :
        ht=60*consommation
        print("le montant hors taxe est de : ",ht)
        ttc=(ht*18)/100 + 10000
        print("le prix net à payer : ",ttc)
        print("")
        
    elif consommation<300 and consommation<=600 :
        ht=70*consommation
        print("le montant hors taxe est de : ",ht)
        ttc=(ht*18)/100 + 10000
        print("le prix net à payer : ",ttc)
        print("")
        
    else :
        print("erreur du system")
        