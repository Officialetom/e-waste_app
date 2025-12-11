from django.shortcuts import render, redirect, get_object_or_404
from .models import EWasteItem

def home(request):
    items = EWasteItem.objects.all().order_by('-id')
    return render(request, 'home.html', {'items': items})

def create_item(request):
    if request.method == "POST":
        EWasteItem.objects.create(
            name=request.POST['name'],
            category=request.POST['category'],
            address=request.POST['address'],
            pickup_date=request.POST['pickup_date'],
        )
        return redirect('home')
    return render(request, 'create.html')

def update_item(request, id):
    item = get_object_or_404(EWasteItem, id=id)
    if request.method == "POST":
        item.name = request.POST['name']
        item.category = request.POST['category']
        item.address = request.POST['address']
        item.pickup_date = request.POST['pickup_date']
        item.status = request.POST['status']
        item.save()
        return redirect('home')
    return render(request, 'update.html', {'item': item})

def delete_item(request, id):
    item = get_object_or_404(EWasteItem, id=id)
    item.delete()
    return redirect('home')
