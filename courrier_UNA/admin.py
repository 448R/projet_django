
# Register your models here.
from django.contrib import admin
from .models import TypeCourrier, Partenaire, Direction, Service, Destinataire, Courrier

admin.site.register(TypeCourrier)
admin.site.register(Partenaire)
admin.site.register(Direction)
admin.site.register(Service)
admin.site.register(Destinataire)
admin.site.register(Courrier)
admin.site.site_header="ADMINISTRATION"
admin.site.index_title="GESTION DES COURRIERS"
admin.site.site_title="ADMINISTRATION"