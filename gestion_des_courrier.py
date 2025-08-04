class TypeCourrier:
    def __init__(self, numero, libelle):
        self.numero = numero
        self.libelle = libelle

    def __str__(self):
        return f"[TypeCourrier] {self.libelle} (N° {self.numero})"


class Partenaire:
    def __init__(self, numero, nom, prenom, courierRecus: list=[]):
        self.numero = numero
        self.nom = nom
        self.prenom = prenom
        self.courierRecus = courierRecus  # Liste des courriers reçus

    def __str__(self):
        return f"[Partenaire] {self.prenom} {self.nom}"
    
    def ajouter_courrier_recu(self, courrierRecu):
        self.courierRecus.append(courrierRecu)
        print(f"Courrier {courrierRecu.libelle} ajouté à {self.nom} {self.prenom}")


class Personne:
    def __init__(self, numero, nom, prenom):
        self.numero = numero
        self.nom = nom
        self.prenom = prenom

    def __str__(self):
        return f"[Personne] {self.prenom} {self.nom}"


class Destinataire:
    def __init__(self, numero, nom, prenom):
        self.numero = numero
        self.nom = nom
        self.prenom = prenom

    def __str__(self):
        return f"[Destinataire] {self.prenom} {self.nom}"


class Direction:
    def __init__(self, code, nom):
        self.code = code
        self.nom = nom
        self.services = []  

    def ajouter_service(self, service):
        self.services.append(service)

    def __str__(self):
        return f"[Direction] {self.nom} (Code {self.code})"


class Service:
    def __init__(self, code, nom, direction):
        self.code = code
        self.nom = nom
        self.direction = direction  

    def __str__(self):
        return f"[Service] {self.nom} rattaché à {self.direction.nom}"


class Courrier:
    def __init__(self, numero, libelle, type_courrier: TypeCourrier=None, partenaire: Partenaire=None, personne=None,
                 destinataire=None, service=None):
        self.numero = numero
        self.libelle = libelle
        self.type_courrier = type_courrier       
        self.partenaire = partenaire        
        self.personne = personne        
        self.destinataire = destinataire          
        self.service = service  
                          
    def envoyer(self, personne, destinataire):
        self.personne = personne
        self.destinataire = destinataire
        print(f"Courrier envoyé par {personne.nom} à {destinataire.nom}")

    def __str__(self):
        return (f"[Courrier] {self.libelle} (N° {self.numero})\n"
                f"  Type: {self.type_courrier}\n"
                f"  Envoyé par: {self.personne}\n"
                f"  Reçu de: {self.partenaire}\n"
                f"  Destinataire: {self.destinataire}\n"
                f"  Traitement: {self.service}")
        
    def __repr__(self):
        return self.libelle


if __name__ == "__main__":
    type_courrier = TypeCourrier(1, "Courrier administratif")
    partenaire = Partenaire(1, "Mouhi", "Kevin")
    personne = Personne(1, "Mouhi", "Kevin")
    destinataire = Destinataire(2, "Nassa", "Wilfried")
    direction = Direction("D01", "Direction Générale")
    service = Service("S01", "Service du Courrier", direction)

    courrier1 = Courrier(101, "Demande de stage", type_courrier, partenaire)
    courrier2 = Courrier(101, "Demande de diplome", type_courrier, partenaire)
    print("courier 1: ", courrier1)
    print("courier 2 : ", courrier2)
    partenaire.courierRecus = [courrier1, courrier2]  # Initialisation de la liste des courriers reçus
    # partenaire.ajouter_courrier_recu(courrier1)
    # partenaire.ajouter_courrier_recu(courrier2)
    print("list couriers")
    for courier in partenaire.courierRecus:
        print(f"{courier.libelle} - {courier.partenaire}")
    print()  
   
