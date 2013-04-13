from models import *

#TODO: Check if this is necessary
from django.forms import widgets

from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    body = serializers.Field()
    slug = serializers.Field()
    class Meta:
        model = Post


