# Définition des deux tableaux
Tab1 = [1, 2, 3, 4, 5]
Tab2 = [10, 20, 30, 40, 50]

# Initialisation du tableau résultat
TabSomme = []

# Boucle pour additionner les éléments
for i in range(len(Tab1)):
    TabSomme.append(Tab1[i] + Tab2[i])

# Affichage du résultat
print("Somme des deux tableaux :", TabSomme)
 