from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from . import models


class AccountSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    slug = serializers.SlugField(
        required=True,
        validators=[UniqueValidator(queryset=models.Account.objects.all())]
    )

    class Meta:
        model = models.Account
        fields = ('id', 'uid', 'owner', 'name', 'slug', 'created_on')
