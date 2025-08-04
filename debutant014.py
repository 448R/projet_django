print("")
print("trions les nombres")
print("")


nombre = input("entrer les nombres : ")
nombre=int(nombre)

print("")

tableau=[]

for i in range(nombre) : 
    chiffre = input(f"entrez le nombre {i+1} : ")
    chiffre=int(chiffre)
    tableau.append(chiffre)
    
nombre_positifs = [] 
nombre_negatifs = []

for indice, element in enumerate(tableau):
    if element < 0 : 
        nombre_negatifs.append(element)
        
    else : 
        nombre_positifs.append(element)   

print("il ya ", len(nombre_negatifs) ,"nombres negatifs") 
for indice, element in enumerate(nombre_negatifs):
    print(f"la position {indice+1} | element {element}")
    
print("il ya ", len(nombre_positifs) ,"nombres positifs") 
for indice, element in enumerate(nombre_positifs):
    print(f"la position {indice+1} | element {element}")  