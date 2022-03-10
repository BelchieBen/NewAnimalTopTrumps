from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, CreateView, FormView
from django.http.response import HttpResponse
from ..forms.main_forms import JoinRoomForm
from ..models import Room, Animal
import random
import string
import requests
import json

class test(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        join_form = JoinRoomForm()
        return render(request, 'main/Home.html', context={"join_room": join_form})

    def post(self, request, *args, **kwargs):
        code = self.request.POST.get('code')
        try:
            room = Room.objects.get(code=code)
        except:
            return HttpResponse('It looks like that room doesnt exist :(')

        if room is not None:
            return redirect('join_room', code=code)


class create_room(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        room = Room.objects.create(
            code = ''.join(random.choice(string.ascii_uppercase) for i in range(4)),
            host = self.request.user
        )
        room.save();
        return render(request, 'main/rooms/RoomPage.html', context={"room": room})

class join_room(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        code = self.kwargs.get('code')
        room = Room.objects.get(code = code)
        return render(request, 'main/rooms/RoomPage.html', context={"room": room})

    def post(self, request, *args, **kwargs):
        animal_response = requests.get('https://zoo-animal-api.herokuapp.com/animals/rand')
        animal_json = animal_response.json()
        animal = Animal(
            name = animal_json['name'],
            type =  animal_json['animal_type'],
            length =  animal_json['length_max'],
            weight =  animal_json['weight_max'],
            lifespan =  animal_json['lifespan'],
            habitat = animal_json['habitat'],
            diet =  animal_json['diet'],
            image =  animal_json['image_link'],
        )

        
        return render(request, 'main/animals/AnimalPage.html', context={"animal": animal})

    
