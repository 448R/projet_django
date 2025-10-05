from django import forms
from .models import Courrier, Partenaire, Destinataire, Service, Direction, TypeCourrier

class CourrierForm(forms.ModelForm):
    class Meta:
        model = Courrier
        fields = ['libelle_courrier', 'type_courrier', 'service', 'partenaire', 'destinataire']

class PartenaireForm(forms.ModelForm):
    class Meta:
        model = Partenaire
        fields = ['nom_partenaire', 'prenom_partenaire']

class DestinataireForm(forms.ModelForm):
    class Meta:
        model = Destinataire
        fields = ['prenom_destinataire', 'nom_destinataire', 'service']

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['code_service', 'nom_service', 'direction']

class DirectionForm(forms.ModelForm):
    class Meta:
        model = Direction
        fields = ['code_direction', 'nom_direction']

class TypeCourrierForm(forms.ModelForm):
    class Meta:
        model = TypeCourrier
        fields = ['libelle_type_courrier']
