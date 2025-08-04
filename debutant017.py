
print("")
print("Moyenne de la classe")
print("")


eleves = 5
eleves=int(eleves)

print("")
print("la matière d'informatique")

note1_informatique=[]
note2_informatique=[]
print("")
print("première notes informatique")
for info in range(eleves) : 
    info1 = input(f"entrez la note {info+1} : ")
    info1=float(info1)
    note1_informatique.append(info1)
    
print("")
print("deuxième notes informatique")
for infos in range(eleves) : 
    info2 = input(f"entrez la note {infos+1} : ")
    info2=float(info2)
    note2_informatique.append(info2)
    
for info1,info2 in zip(note1_informatique,note2_informatique) :
    print("la moyenne de l'élève n°",infos+1)
    
print("") 
print("la matière mathématique ")

note1_mathematique=[]
note2_mathematique=[]
print("")
print("première notes mathematique")
for math in range(eleves) : 
    math1 = input(f"entrez la note {math+1} : ")
    math1=float(math1)
    note1_mathematique.append(math1)
    
print("")
print("deuxième notes mathematique")
for maths in range(eleves) : 
    math2 = input(f"entrez la note {maths+1} : ")
    math2=float(info2)
    note2_mathematique.append(math2)
    
for math1,math2 in zip(note1_mathematique,note2_mathematique) :
    print(((math1*5) +(math2*3))*3)/11
    
print("")
print("la matière anglais")

note1_anglais=[]
note2_anglais=[]
print("")
print("première notes anglais")
for anglais in range(eleves) : 
    anglais1 = input(f"entrez la note {anglais+1} : ")
    anglais1=float(anglais1)
    note1_anglais.append(anglais1)
    
print("")
print("deuxième notes anglais")
for anglaiss in range(eleves) : 
    anglais2 = input(f"entrez la note {anglaiss+1} : ")
    anglais2=float(anglais2)
    note2_anglais.append(anglais2)
    
for anglais1,anglais2 in zip(note1_anglais,note2_anglais) :