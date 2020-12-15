from django.shortcuts import render,redirect
from .forms import UserForm
from .models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from rest_framework import status

# Create your views here.
def index(request):
    return render(request, 'chat/index.html')

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })

def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = User.objects.create(user_id= form.cleaned_data['user_id'],
            user_name = form.cleaned_data['user_name'],
            user_email = form.cleaned_data['user_email'],
            thumbnail = 'https://grs-img.s3.amazonaws.com/'+user_name+'.jpg',
            user_rank = form.cleaned_data['user_rank'],
            birth = form.cleaned_data[ 'birth']
            )
            return redirect('index')
    form = UserForm()
    return render(request, 'chat/register.html', {'form': form})    

class Image(APIView):
    def post(self, request, format=None):
        serializers = PhotoSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=stauts.HTTP_201_CREATED)
        return Response(serializers.errors, status=stauts.HTTP_400_BAD_REQUEST)
