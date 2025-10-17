
# Create your models here.
from django.db import models

# -----------------------
# ENTITES PRINCIPALES
# -----------------------

class TypeCourrier(models.Model):
    num_type_courrier = models.AutoField(primary_key=True)
    libelle_type_courrier = models.CharField(max_length=100)

    def __str__(self):
        return self.libelle_type_courrier


class Partenaire(models.Model):
    num_partenaire = models.AutoField(primary_key=True)
    nom_partenaire = models.CharField(max_length=100)
    prenom_partenaire = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.prenom_partenaire} {self.nom_partenaire}"


class Direction(models.Model):
    code_direction = models.CharField(max_length=10, primary_key=True)
    nom_direction = models.CharField(max_length=100)

    def __str__(self):
        return self.nom_direction


class Service(models.Model):
    code_service = models.CharField(max_length=10, primary_key=True)
    nom_service = models.CharField(max_length=100)
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE, related_name='services')

    def __str__(self):
        return self.nom_service


class Destinataire(models.Model):
    num_destinataire = models.AutoField(primary_key=True)
    prenom_destinataire = models.CharField(max_length=100)
    nom_destinataire = models.CharField(max_length=100)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='destinataires')

    def __str__(self):
        return f"{self.prenom_destinataire} {self.nom_destinataire}"


class Courrier(models.Model):
    num_courrier = models.AutoField(primary_key=True)
    libelle_courrier = models.CharField(max_length=255)
    type_courrier = models.ForeignKey(TypeCourrier, on_delete=models.CASCADE, related_name='courriers')
    partenaire = models.ForeignKey(Partenaire, on_delete=models.CASCADE, related_name='courriers', null=True, blank=True)
    destinataire = models.ForeignKey(Destinataire, on_delete=models.CASCADE, related_name='courriers')

    def __str__(self):
        return self.libelle_courrier
