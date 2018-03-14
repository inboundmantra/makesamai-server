from rest_framework import serializers
from . import models


class DashboardFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Form
        fields = (
            'ufid',
            'account',
            'created_by',
            'title',
            'description',
            'created_on',
            'title_enabled',
            'title_required',
            'fname_enabled',
            'fname_required',
            'lname_enabled',
            'lname_required',
            'email_enabled',
            'email_required',
            'company_enabled',
            'company_required',
            'website_enabled',
            'website_required',
            'phone_enabled',
            'phone_required',
            'address_line_enabled',
            'address_line_required',
            'street_enabled',
            'street_required',
            'city_enabled',
            'city_required',
            'state_enabled',
            'state_required',
            'postcode_enabled',
            'postcode_required',
            'country_enabled',
            'country_required'
        )


class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Form
        fields = (
            'ufid',
            'account',
            'title',
            'created_on',
            'title_enabled',
            'title_required',
            'fname_enabled',
            'fname_required',
            'lname_enabled',
            'lname_required',
            'email_enabled',
            'email_required',
            'company_enabled',
            'company_required',
            'website_enabled',
            'website_required',
            'phone_enabled',
            'phone_required',
            'address_line_enabled',
            'address_line_required',
            'street_enabled',
            'street_required',
            'city_enabled',
            'city_required',
            'state_enabled',
            'state_required',
            'postcode_enabled',
            'postcode_required',
            'country_enabled',
            'country_required'
        )
