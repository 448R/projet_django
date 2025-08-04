from django.db import models

class Direction(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Service(models.Model):
    nom = models.CharField(max_length=100)
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE, related_name="services")

    def __str__(self):
        return self.nom

class Destinataire(models.Model):
    nom = models.CharField(max_length=100)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="destinataires")

    def __str__(self):
        return self.nom

class Partenaire(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Personne(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class TypeCourrier(models.Model):
    libelle = models.CharField(max_length=100)

    def __str__(self):
        return self.libelle

class Courrier(models.Model):
    objet = models.CharField(max_length=200)
    date_reception = models.DateField()
    type_courrier = models.ForeignKey(TypeCourrier, on_delete=models.CASCADE) 
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True, blank=True)  
    destinataire = models.ForeignKey(Destinataire, on_delete=models.CASCADE, null=True, blank=True) 
    partenaire_expediteur = models.ForeignKey(Partenaire, on_delete=models.SET_NULL, null=True, blank=True, related_name="courriers_envoyes")  
    partenaire_recepteur = models.ForeignKey(Partenaire, on_delete=models.SET_NULL, null=True, blank=True, related_name="courriers_recus")  
    personne_expediteur = models.ForeignKey(Personne, on_delete=models.SET_NULL, null=True, blank=True, related_name="courriers_envoyes") 
    personne_reception = models.ForeignKey(Personne, on_delete=models.SET_NULL, null=True, blank=True, related_name="courriers_recus")  

    def __str__(self):
        return self.objet
