from django.shortcuts import render
from .models import   NeighbourHood


# Create your views here.

def hoods(request):
    """View Functionality for getting all hoods"""
    all_hoods = NeighbourHood.objects.all()
    all_hoods = all_hoods[::-1]
    params = {
        'all_hoods': all_hoods,
    }
    return render(request, 'home.html', params)
