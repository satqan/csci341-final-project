from rest_framework import serializers
from .models import Specialize


class SpecializeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialize
        fields = "__all__"
