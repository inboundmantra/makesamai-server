from rest_framework import serializers

from . import models


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Address
        fields = (
            'id',
            'address_line',
            'street',
            'city',
            'state',
            'postcode',
            'country'
        )


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Contact
        fields = (
            'ucid',
            'source',
            'title',
            'first_name',
            'last_name',
            'company',
            'website_url',
            'phone',
            'address',
            'status',
            'stage',
            'description',
            'created_by',
            'created_on',
            'is_active'
        )
