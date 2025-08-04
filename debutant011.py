print("quelle operation voulez vous faire")

solde=0

def depôt(solde):
    
    montant=input("entrer le montant : ")
    montant=int(montant)
    
    if montant < 0 :
        print("entrer un montant réel svp !!!")
        solde = solde
        return solde
    solde=solde+montant
    return solde

def retrait(solde):
    montant=input("entrer le montant du retrait : ")
    montant=int(montant)
    
    if montant>solde or montant<0 :
        print("votre solde est insuffisant!!!")
        solde=solde
        return solde
    solde=solde-montant
    return solde
    
condition=True

while condition:
    print("1.depôt")
    print("2.retrait")
    print("0.quitter")
    option=input("choisissez une option : ")
    option=int(option)
    
    if option==0 :
        condition=False 
        
    if option==1 :
        solde=depôt(solde) 
        print(solde)
        
    elif option==2 :
        solde=retrait(solde)
        print(solde)
        
    elif option==0 :
        print("merci d'être moov")
    else :
        print("ce service est momentanement indisponible")
        
