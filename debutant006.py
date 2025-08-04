def calcule(nom,prenom,age):
    print("le nom de l'individu est: {}, son prenom est: {}, l'age est: {}".format(nom,prenom,age) )
    age=int(age)
    
    if age>=18 and age<22 :
        print(nom, prenom, "vous êtes majeur", age)
    
    elif age>=22 :
        print(nom, prenom, "vous êtes adultes", age)
        
    else :
        print(nom, prenom, "vous êtes mineur", age)
     
calcule(
    input("entrer votre nom :"),
    input("entrer votre prenom :"),
    input("entrer votre age :")
        )

