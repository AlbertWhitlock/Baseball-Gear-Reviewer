from django.shortcuts import render, redirect

from .models import Bats, Gloves, Balls, Helmets
from .forms import Bats_Review_Form, Gloves_Review_Form, Balls_Review_Form, Helmets_Review_Form


# Create your views here.
def all_gear_list(request):
    # decadesResult = Decade.objects.all()
    return render(request, 'all_gear_list.html')

def bat_list(request):
    batsResult = Bats.objects.all()
    return render(request, 'bat_list.html', {'bats': batsResult})

def bat_detail(request, id):
    batDetailResult = Bats.objects.get(id=id)
    return render(request, 'bat_detail.html', {'batDetails': batDetailResult})

def glove_list(request):
    glovesResult = Gloves.objects.all()
    return render(request, 'glove_list.html', {'gloves': glovesResult})

def glove_detail(request, id):
    gloveDetailResult = Gloves.objects.get(id=id)
    return render(request, 'glove_detail.html', {'gloveDetails': gloveDetailResult})


def ball_list(request):
    ballsResult = Balls.objects.all()
    return render(request, 'ball_list.html', {'balls': ballsResult})

def ball_detail(request, id):
    ballDetailResult = Balls.objects.get(id=id)
    return render(request, 'ball_detail.html', {'ballDetails': ballDetailResult})

def helmet_list(request):
    helmetsResult = Helmets.objects.all()
    return render(request, 'helmet_list.html', {'helmets': helmetsResult})

def helmet_detail(request, id):
    helmetDetailResult = Helmets.objects.get(id=id)
    return render(request, 'helmet_detail.html', {'helmetDetails': helmetDetailResult})