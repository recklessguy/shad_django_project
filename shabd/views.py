
from django.contrib.auth import decorators
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from .forms import newghazalform
from django.utils.decorators import method_decorator

# Create your views here.
from .models import ghazals_home, new_ghazals, famous_ghazals


def home(request):
    shayari=ghazals_home.objects.all()
    return render(request,'home.html',{'shayari':shayari})

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request, "contact.html")

def newghazals(request):
    shayari=new_ghazals.objects.all()
    return render(request, "new_ghazals.html", {'shayari':shayari})

def famousghazals(request):
    shayari=famous_ghazals.objects.all()
    return render(request, "famous_ghazals.html", {'shayari':shayari})

def search_for(request):
    if request.method=="POST":
        searched = request.POST['searched']
        shayari = new_ghazals.objects.filter(tags__contains=searched)
        return render(request,"search.html",
        {'searched':searched,
        'shayari':shayari})

    else:
        return render(request,"search.html")

def admin(request):
    return render(request, "admin.html")

# @login_required(login_url='login')

class addwriting(CreateView):
    model = new_ghazals
    form_class = newghazalform
    template_name = 'add_writings.html'