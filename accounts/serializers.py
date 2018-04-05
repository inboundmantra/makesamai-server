from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from . import models


class AccountSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    domain = serializers.URLField(
        required=False,
        validators=[UniqueValidator(queryset=models.Account.objects.all())]
    )

    class Meta:
        model = models.Account
        fields = ('uaid', 'owner', 'name', 'domain', 'created_on')
