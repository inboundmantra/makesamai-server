from rest_framework import serializers
from . import models


class EmailCampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EmailCampaign
        fields = (
            'cmid',
            'created_by',
            'account',
            'list',
            'campaign_title',
            'subject',
            'message_template',
            'timestamp'
        )


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        models = models.Email
        fields = (
            'umid',
            'campaign',
            'account',
            'to_email',
            'from_email',
            'subject',
            'message',
            'timestamp',
            'status'
        )
