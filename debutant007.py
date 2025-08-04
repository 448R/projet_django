def impôt() :
    tva=0.18
    prixht=input("saisir le prix hors taxe")
    prixht=float(prixht)
    ttc=(prixht*tva)+prixht
    return 

    if ttc>=10000 and ttc<30000 :
        ttc=impôt()  
        print("moyen entrepreuneur")
    
    elif ttc>=30000 :
        ttc=impôt()
        print("excellent entrepreuneur")

    else :
        ttc=impôt()
        print("revoir la somme versé stp!!!")