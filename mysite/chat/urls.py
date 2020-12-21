from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('chat/<str:room_name>/', views.room, name='room'),
    path('create/',views.register,name='register'),
    path('eye_exercise/', views.eye_exercise,name='eye_exercise'),
    path('stretching/', views.stretching,name='stretching')
]