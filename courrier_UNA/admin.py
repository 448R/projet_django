
# Register your models here.
from django.contrib import admin
from .models import TypeCourrier, Partenaire, Direction, Service, Destinataire, Courrier
from django.contrib import admin
from .models import Service, Direction
from .models import Direction
from .models import Destinataire
from .models import Direction, Service
from .models import Courrier


admin.site.site_header="ADMINISTRATION"
admin.site.index_title="GESTION DES COURRIERS"
admin.site.site_title="ADMINISTRATION"


admin.site.register(TypeCourrier)
admin.site.register(Partenaire)


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('nom_service', 'get_direction')
    list_filter = ('direction',)
    def get_direction(self, obj):
        return obj.direction.nom_direction  
    get_direction.short_description = 'Direction'  
admin.site.register(Service, ServiceAdmin)


class DirectionAdmin(admin.ModelAdmin):
    list_display = ('nom_direction', 'nombre_services')
    def nombre_services(self, obj):
        return obj.services.count() 
    nombre_services.short_description = 'Nombre de services'
admin.site.register(Direction, DirectionAdmin)


class DestinataireAdmin(admin.ModelAdmin):
    list_display = ('nom_destinataire', 'service',)
    list_filter = ('service',)
    search_fields = ('nom_destinataire',)
admin.site.register(Destinataire, DestinataireAdmin)



class CourrierAdmin(admin.ModelAdmin):
    list_display = ('libelle_courrier', 'get_type_courrier', 'get_partenaire', 'get_destinataire')

    def get_type_courrier(self, obj):
        return obj.type_courrier.libelle_type_courrier if obj.type_courrier else "-"
    get_type_courrier.short_description = 'Type de Courrier'

    def get_partenaire(self, obj):
        if obj.partenaire:
            return f"{obj.partenaire.prenom_partenaire} {obj.partenaire.nom_partenaire}"
        return "-"
    get_partenaire.short_description = 'Partenaire'

    def get_destinataire(self, obj):
        if obj.destinataire:
            return f"{obj.destinataire.prenom_destinataire} {obj.destinataire.nom_destinataire}"
        return "-"
    get_destinataire.short_description = 'Destinataire'

admin.site.register(Courrier, CourrierAdmin)

