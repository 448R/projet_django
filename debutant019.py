from datetime import datetime

# Variables
employes = []
matricules = set()
annee_actuelle = datetime.now().year

# Enregistrements
for i in range(10):
    while True:
        matricule = input(f"Entrez le matricule de l'employé {i+1}: ")
        if matricule in matricules:
            print("Matricule déjà utilisé. Veuillez entrer un autre matricule.")
        else:
            matricules.add(matricule)
            break
    
    nom = input("Entrez le nom: ")
    prenom = input("Entrez le prénom: ")
    annee_embauche = int(input("Entrez l'année d'embauche: "))
    
    employe = {
        "matricule": matricule,
        "nom": nom,
        "prenom": prenom,
        "annee_embauche": annee_embauche
    }
    employes.append(employe)
    print("")

# Recherche de l'employé le plus expérimenté
max_experience = -1
employe_experimente = None

for employe in employes:
    experience = annee_actuelle - employe["annee_embauche"]
    if experience > max_experience:
        max_experience = experience
        employe_experimente = employe

# Affichage du résultat
print("\nL'employé le plus expérimenté est :")
print(f"Matricule : {employe_experimente['matricule']}")
print(f"Nom : {employe_experimente['nom']}")
print(f"Prénom : {employe_experimente['prenom']}")
print(f"Année d'embauche : {employe_experimente['annee_embauche']}")
print(f"Expérience : {max_experience} ans")
