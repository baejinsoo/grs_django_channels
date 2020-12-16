#-*- coding: utf-8 -*-
from django.shortcuts import render,redirect
from .forms import UserForm
from .models import User
from .upload_s3 import handle_upload_file

# Create your views here.
def index(request):
    return render(request, 'chat/index.html')

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })


def register(request):
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            user = User.objects.create(
                user_id=form.cleaned_data['user_id'],
                user_name=form.cleaned_data['user_name'],
                user_email=form.cleaned_data['user_email'],
                user_rank=form.cleaned_data['user_rank'],
                task=form.cleaned_data['task'],
                birth=form.cleaned_data['birth'],
                user_pic=form.cleaned_data['user_pic'],
                thumbnail='https://grs-img.s3.amazonaws.com/'+str(form.cleaned_data['user_pic'])
            )
            print(str(form.cleaned_data['user_pic']), type(str(form.cleaned_data['user_pic'])))
            handle_upload_file(str(form.cleaned_data['user_pic']))
            return redirect('index')
    form=UserForm
    return render(request, 'chat/register.html', {'form': form})   
