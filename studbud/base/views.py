from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import RoomForm
from .models import Room

    # rooms = [
    #     {'id':1 , "name" : 'Lets Learn Django!'},
    #     {'id':2 , "name" : 'For Python!'},
    #     {'id':3 , "name" : 'For Mysql!'},
    #     ]
# Create your views here.
def home(request):

    rooms = Room.objects.all()
    context = {'rooms': rooms}

    return render(request , 'base/home.html',context)



def room(request, pk):
    room = Room.objects.get(id=int(pk))
    # for i in rooms:
    #     if i['id'] == int(pk):
    #         room = i
    context = {"room" : room}
    return render(request, 'base/room.html' , context)


def createRoom(request):

    form = RoomForm()

    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

        print(request.POST)
    context = {'form':form}
    return render(request, 'base/room_form.html',context)

def updateRoom(request, pk):

    room = Room.objects.get(id=pk)
    form = RoomForm(isinstance= room)

    context = {}
    return render(request, 'bash/room_from.html', context)