from rest_framework import serializers
from .models import PublicServant


class PublicServantSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicServant
        fields = "__all__"
