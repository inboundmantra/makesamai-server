from rest_framework import serializers
from . import models


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.List
        fields = (
            'ugid',
            'account',
            'created_by',
            'created_on',
            'title',
            'description',
            'assigned_contacts',
        )
