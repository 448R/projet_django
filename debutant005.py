nombre_1=input("saisir le nombre1 : ")
nombre_2=input("saisir le nombre2 : ")
nombre_3=input("saisir le nombre3 : ")

nombre_1=int(nombre_1)
nombre_2=int(nombre_2)
nombre_3=int(nombre_3)

if nombre_1<nombre_2  and nombre_2<nombre_3 :
    print("le nombre3 est le plus grand :",nombre_3)
    
elif nombre_1>nombre_2 and nombre_1>nombre_3 :
    print("le nombre1 est le plus grand :",nombre_1)
    
elif nombre_1==nombre_2==nombre_3 :
    print("les trois nombre sont égaux",nombre_1)
    
elif nombre_1==nombre_2 and nombre_3> nombre_2 :
    print("les nombre1 et 2 sont egaux",nombre_2)
    print("mais le plus grand nombre est le nombre3",nombre_3)
     
elif nombre_1==nombre_3 and nombre_2> nombre_3 :
     print("les nombre1 et 3 sont egaux",nombre_1)
     print("mais le plus grand nombre est le nombre2",nombre_2)
     
elif nombre_2==nombre_3 and nombre_1> nombre_3 :
    print("les nombre2 et 3 sont egaux",nombre_2)
    print("mais le plus grand nombre est le nombre1",nombre_1)
    
else :
    print("le nombre2 est le plus grand :",nombre_2)