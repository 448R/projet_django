from abc import ABC, abstractmethod

class Document(ABC):
    def __init__(self, titre, auteur, annee):
        self.__titre = titre
        self.__auteur = auteur
        self.__annee = annee

    @abstractmethod
    def description(self):
        pass

    @property
    def titre(self):
        return self.__titre

    @property
    def auteur(self):
        return self.__auteur

    @property
    def annee(self):
        return self.__annee

    def __str__(self):
        return f"{self.__titre} ({self.__annee})"

    def __repr__(self):
        return f"{self.__class__.__name__}(titre='{self.__titre}', auteur='{self.__auteur}', annee={self.__annee})"

# 🕮 Classe Livre
class Livre(Document):
    def __init__(self, titre, auteur, annee, nb_pages):
        super().__init__(titre, auteur, annee)
        self.__nb_pages = nb_pages

    def description(self):
        return f"Livre: {self.titre} par {self.auteur}, {self.annee}, {self.__nb_pages} pages"

# 🗞 Classe Journal
class Journal(Document):
    def __init__(self, titre, auteur, annee, date_parution):
        super().__init__(titre, auteur, annee)
        self.__date_parution = date_parution

    def description(self):
        return f"Journal: {self.titre}, paru le {self.__date_parution}"

# 📀 Classe DVD
class DVD(Document):
    def __init__(self, titre, auteur, annee, duree):
        super().__init__(titre, auteur, annee)
        self.__duree = duree

    def description(self):
        return f"DVD: {self.titre}, durée : {self.__duree} minutes"

# 📚 Gestion de la bibliothèque
class Bibliotheque:
    def __init__(self):
        self.__documents = []

    def ajouter_document(self, doc):
        if isinstance(doc, Document):
            self.__documents.append(doc)

    def afficher_documents(self):
        for doc in self.__documents:
            print(doc.description())

# 🚀 Utilisation
livre1 = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", 1943, 96)
journal1 = Journal("Le Monde", "Rédaction", 2025, "2025-07-21")
dvd1 = DVD("Inception", "Christopher Nolan", 2010, 148)

biblio = Bibliotheque()
biblio.ajouter_document(livre1)
biblio.ajouter_document(journal1)
biblio.ajouter_document(dvd1)

biblio.afficher_documents()
