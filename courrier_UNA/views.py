from django.shortcuts import render, get_object_or_404, redirect
from .models import Courrier, Partenaire, Destinataire, Service, Direction, TypeCourrier
from .forms import (CourrierForm, PartenaireForm, DestinataireForm,
                    ServiceForm, DirectionForm, TypeCourrierForm)

# --- Accueil + courriers (déjà vus) ---
def home(request):
    return render(request, 'home.html')

def index(request):
    courriers = Courrier.objects.all()
    return render(request, 'index.html', {'courriers': courriers})

def ajouter_courrier(request):
    if request.method == 'POST':
        form = CourrierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CourrierForm()
    return render(request, 'ajouter_courrier.html', {'form': form})

# --- PARTENAIRES ---
def partenaires_list(request):
    items = Partenaire.objects.all()
    return render(request, 'partenaires/list.html', {'items': items})

def partenaires_create(request):
    if request.method == 'POST':
        form = PartenaireForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('partenaires_list')
    else:
        form = PartenaireForm()
    return render(request, 'partenaires/form.html', {'form': form, 'title': 'Ajouter un partenaire'})

def partenaires_update(request, pk):
    obj = get_object_or_404(Partenaire, pk=pk)
    if request.method == 'POST':
        form = PartenaireForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('partenaires_list')
    else:
        form = PartenaireForm(instance=obj)
    return render(request, 'partenaires/form.html', {'form': form, 'title': 'Modifier le partenaire'})

def partenaires_delete(request, pk):
    obj = get_object_or_404(Partenaire, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('partenaires_list')
    return render(request, 'confirm_delete.html', {'object': obj, 'return_url': 'partenaires_list'})

# --- DESTINATAIRES ---
def destinataires_list(request):
    items = Destinataire.objects.select_related('service').all()
    return render(request, 'destinataires/list.html', {'items': items})

def destinataires_create(request):
    if request.method == 'POST':
        form = DestinataireForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('destinataires_list')
    else:
        form = DestinataireForm()
    return render(request, 'destinataires/form.html', {'form': form, 'title': 'Ajouter un destinataire'})

def destinataires_update(request, pk):
    obj = get_object_or_404(Destinataire, pk=pk)
    if request.method == 'POST':
        form = DestinataireForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('destinataires_list')
    else:
        form = DestinataireForm(instance=obj)
    return render(request, 'destinataires/form.html', {'form': form, 'title': 'Modifier le destinataire'})

def destinataires_delete(request, pk):
    obj = get_object_or_404(Destinataire, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('destinataires_list')
    return render(request, 'confirm_delete.html', {'object': obj, 'return_url': 'destinataires_list'})

# --- SERVICES ---
def services_list(request):
    items = Service.objects.select_related('direction').all()
    return render(request, 'services/list.html', {'items': items})

def services_create(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('services_list')
    else:
        form = ServiceForm()
    return render(request, 'services/form.html', {'form': form, 'title': 'Ajouter un service'})

def services_update(request, code):
    obj = get_object_or_404(Service, code_service=code)
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('services_list')
    else:
        form = ServiceForm(instance=obj)
    return render(request, 'services/form.html', {'form': form, 'title': 'Modifier le service'})

def services_delete(request, code):
    obj = get_object_or_404(Service, code_service=code)
    if request.method == 'POST':
        obj.delete()
        return redirect('services_list')
    return render(request, 'confirm_delete.html', {'object': obj, 'return_url': 'services_list'})

# --- DIRECTIONS ---
def directions_list(request):
    items = Direction.objects.all()
    return render(request, 'directions/list.html', {'items': items})

def directions_create(request):
    if request.method == 'POST':
        form = DirectionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('directions_list')
    else:
        form = DirectionForm()
    return render(request, 'directions/form.html', {'form': form, 'title': 'Ajouter une direction'})

def directions_update(request, code):
    obj = get_object_or_404(Direction, code_direction=code)
    if request.method == 'POST':
        form = DirectionForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('directions_list')
    else:
        form = DirectionForm(instance=obj)
    return render(request, 'directions/form.html', {'form': form, 'title': 'Modifier la direction'})

def directions_delete(request, code):
    obj = get_object_or_404(Direction, code_direction=code)
    if request.method == 'POST':
        obj.delete()
        return redirect('directions_list')
    return render(request, 'confirm_delete.html', {'object': obj, 'return_url': 'directions_list'})

# --- TYPES COURRIERS (optionnel) ---
def types_list(request):
    items = TypeCourrier.objects.all()
    return render(request, 'types/list.html', {'items': items})

def types_create(request):
    if request.method == 'POST':
        form = TypeCourrierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('types_list')
    else:
        form = TypeCourrierForm()
    return render(request, 'types/form.html', {'form': form, 'title': 'Ajouter un type de courrier'})



from django.shortcuts import render
from .models import Courrier

def home(request):
    return render(request, "home.html")

from django.shortcuts import render, redirect
from .forms import CourrierForm

def ajouter_courrier(request):
    if request.method == "POST":
        form = CourrierForm(request.POST)
        if form.is_valid():
            form.save()  # Enregistre le courrier en base
            return redirect('liste_courriers')  # redirige vers la liste
    else:
        form = CourrierForm()
    return render(request, "ajouter_courrier.html", {"form": form})


def liste_courriers(request):
    return render(request, "liste.html")
def liste_courriers(request):
    courriers = Courrier.objects.all()  # récupère tous les courriers
    return render(request, "liste.html", {"courriers": courriers})

def gerer(request):
    return render(request, "gerer.html")



