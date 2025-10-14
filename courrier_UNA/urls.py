from django.urls import path
from . import views

urlpatterns = [
    # page d'accueil
    path('', views.home, name='home'),

    # courriers
    path('index/', views.index, name='index'),                 # liste (utilisé par base.html / home)
    path('ajouter/', views.ajouter_courrier, name='ajouter_courrier'),
    path('liste/', views.liste_courriers, name='liste_courriers'),

    # gestion générale
    path('gerer/', views.gerer, name='gerer'),

    # partenaires
    path('partenaires/', views.partenaires_list, name='partenaires_list'),
    path('partenaires/ajouter/', views.partenaires_create, name='partenaires_create'),
    path('partenaires/<int:pk>/modifier/', views.partenaires_update, name='partenaires_update'),
    path('partenaires/<int:pk>/supprimer/', views.partenaires_delete, name='partenaires_delete'),

    # destinataires
    path('destinataires/', views.destinataires_list, name='destinataires_list'),
    path('destinataires/ajouter/', views.destinataires_create, name='destinataires_create'),
    path('destinataires/<int:pk>/modifier/', views.destinataires_update, name='destinataires_update'),
    path('destinataires/<int:pk>/supprimer/', views.destinataires_delete, name='destinataires_delete'),

    # services
    path('services/', views.services_list, name='services_list'),
    path('services/ajouter/', views.services_create, name='services_create'),
    path('services/<str:code>/modifier/', views.services_update, name='services_update'),
    path('services/<str:code>/supprimer/', views.services_delete, name='services_delete'),

    # directions
    path('directions/', views.directions_list, name='directions_list'),
    path('directions/ajouter/', views.directions_create, name='directions_create'),
    path('directions/<str:code>/modifier/', views.directions_update, name='directions_update'),
    path('directions/<str:code>/supprimer/', views.directions_delete, name='directions_delete'),

    # types courriers (optionnel)
    path('types/', views.types_list, name='types_list'),
    path('types/ajouter/', views.types_create, name='types_create'),
]


