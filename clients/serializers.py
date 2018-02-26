from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from . import models


class ClientSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        validators=[UniqueValidator(queryset=models.Client.objects.all())]
    )
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=models.Client.objects.all())]
    )

    password = serializers.CharField(min_length=8, write_only=True)

    def createsuperuser(self, validated_data):
        superuser = models.Client.objects.create_superuser(validated_data['username'], validated_data['first_name'],
                                                            validated_data['last_name'], validated_data['email'],
                                                            validated_data['password'])
        return superuser

    def create(self, validated_data):
        user = models.Client.objects.create_user(validated_data['username'], validated_data['first_name'],
                                                  validated_data['last_name'], validated_data['email'],
                                                  validated_data['password'])
        return user

    class Meta:
        model = models.Client
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password')
