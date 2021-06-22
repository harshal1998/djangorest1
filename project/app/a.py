from rest_framework import serializers
from .models import *


class s(serializers.ModelSerializer):
    class Meta:
        model = demo
        fields = "__all__"
