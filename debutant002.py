effectif_total=0
effectif_1=0
effectif_2=0
effectif_3=0
effectif_4=0

pourcent_1=0,0
pourcent_2=0,0
pourcent_3=0,0
pourcent_4=0,0

effectif_total=input("entrer l'effectif total :")
effectif_total=int(effectif_total)

i=0
while i<=effectif_total :
    note=input("entrer la note :")
    note=int(note)
    i +=1
        
    if note>=10 and note<12 :
        effectif_1 += 1
    
    elif note>=12 and note<14 :
        effectif_2 += 1
    
    elif note>=14 and note<16 :
        effectif_3 += 1
    
    elif note>=16 and note<=20 :
        effectif_4 += 1

    else : 
        print("saisir une note correcte")
    
    pourcent_1= (effectif_1/effectif_total)*100
    pourcent_2= (effectif_2/effectif_total)*100
    pourcent_3= (effectif_3/effectif_total)*100
    pourcent_4= (effectif_4/effectif_total)*100

print("les notes [10;12[,pourcentage  :", pourcent_1,"%")
print("les notes [12;14[,pourcentage  :", pourcent_2,"%")
print("les notes [14;16[,pourcentage  :", pourcent_3,"%")
print("les notes [16;20[,pourcentage  :", pourcent_4,"%")