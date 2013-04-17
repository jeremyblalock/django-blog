from models import *

#TODO: Check if this is necessary
from django.forms import widgets

from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    body = serializers.Field()
    slug = serializers.Field()
    posted = serializers.Field(source='relative_time')
    class Meta:
        model = Post


