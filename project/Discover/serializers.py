from rest_framework import serializers
from .models import Discover


class DiscoverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discover
        fields = "__all__"
