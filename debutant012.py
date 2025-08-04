print("quelle operation voulez vous faire")

def addition():
    nombre1=input("entrer le nombre1 : ")
    nombre1=int(nombre1)
    nombre2=input("saisir le nombre2 : ")
    nombre2=int(nombre2)
    operation=nombre1 + nombre2        
    return operation   

def soustraction() :
    nombre1=input("entrer le nombre1 : ")
    nombre1=int(nombre1)
    nombre2=input("saisir le nombre2 : ")
    nombre2=int(nombre2)
    operation=nombre1 - nombre2        
    return operation 

def multiplication() :
    nombre1=input("entrer le nombre1 : ")
    nombre1=int(nombre1)
    nombre2=input("saisir le nombre2 : ")
    nombre2=int(nombre2)
    operation=nombre1 * nombre2        
    return operation 

def division() : 
        nombre1=input("entrer le nombre1 : ")
        nombre1=int(nombre1)
        nombre2=input("saisir le nombre2 : ")
        nombre2=int(nombre2)
        operation=nombre1 / nombre2
        return operation



variable=True

while variable :
    print("1.addition")
    print("2.soustraction")
    print("3.multiplication")
    print("4.division")
    
    chiffre=input("saisir un numero : ")
    chiffre=int(chiffre)
    
    if chiffre==1 :
        operation=addition()
        print(operation)
        
    elif chiffre==2 : 
        operation=soustraction()
        print(operation)
        
    elif chiffre==3 : 
        operation=multiplication()
        print(operation)
        
    elif chiffre==4:
        operation=division()
        print(operation)
        
    else : 
        print("erreur")