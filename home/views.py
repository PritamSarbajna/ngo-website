from django.shortcuts import render, HttpResponse
from .models import contactModel

# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def explore(request):
    return render(request, 'home/explore.html')

def contact(request):
    return render(request, 'home/contact.html')

def contact_saved(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        city=request.POST.get('city')
        message=request.POST.get('message')
        data=contactModel(name=name, email=email, city=city, message=message)
        data.save()
    return render(request, 'home/contact.html')
