from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, CreateView, FormView
from ..forms.main_forms import JoinRoomForm

class test(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        join_form = JoinRoomForm()
        return render(request, 'main/Home.html', context={"join_room": join_form})

    def post(self, request, *args, **kwargs):
        join_form = JoinRoomForm(request.POST)
        if(join_form.is_valid):
            code = join_form.cleaned_data.get('code')


class create_room(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        join_form = JoinRoomForm()
        return render(request, 'main/rooms/CreateRoom.html', context={"join_room": join_form})

class join_room(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, 'main/rooms/JoinRoom.html')

    
