from django.shortcuts import render

# Create your views here.

# from django.http import HttpResponse

rooms = [
    {'id': 1, 'name': 'lets learn python'},
    {'id': 2, 'name': 'code with me'},
    {'id': 3, 'name': 'frontend developers'},
]

def home(request):
    context = {'rooms': rooms}
    return render(request, 'home.html', context)

def room(request):
    return render(request, 'room.html')
