from django.shortcuts import render,get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm
from .models import   Post, User,NeighbourHood,Business,Profile
from .forms import  NeighbourHoodForm,PostForm,UpdateProfileForm,BusinessForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def hoods(request):
    """View Functionality for getting all hoods"""
    all_hoods = NeighbourHood.objects.all()
    all_hoods = all_hoods[::-1]
    params = {
        'all_hoods': all_hoods,
    }
    return render(request, 'home.html', params)
