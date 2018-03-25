from rest_framework import serializers
from . import models


class LandingPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LandingPage
        fields = (
            'ulid',
            'account',
            'created_by',
            'created_on',
            'title',
            'slug',
            'description',
            'brand_name',
            'form',
            'thank_you_message',
        )
