


from django.shortcuts import render


def index(request):
    return render(request, 'gestion_des_courriers.html')