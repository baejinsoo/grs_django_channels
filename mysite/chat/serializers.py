from rest_framework import serializers
from .models import *


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = photo
        fields = ('__all__')
