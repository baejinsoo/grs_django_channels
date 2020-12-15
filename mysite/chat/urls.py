from django.urls import path

from . import views
from .views import Image

urlpatterns = [
    path('', views.index, name='index'),
    path('chat/<str:room_name>/', views.room, name='room'),
    path('create/',views.register,name='register'),
    path('image',views.Image.as_view(), name='image')
]