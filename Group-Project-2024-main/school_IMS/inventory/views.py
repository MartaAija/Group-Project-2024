from django.shortcuts import render
from .models import Equipment

def all_equipment(request):
    equipments = Equipment.objects.all()
    return render(request, 'inventory/inventory.html', {'equipments': equipments})

