from django.conf.urls import include
from django.urls import path,include
from django.contrib import admin

urlpatterns = [
    # path('chat/', include('chat.urls')),
    path('', include('chat.urls')),
    path('admin/', admin.site.urls),
]