from rest_framework import serializers
from . import models


class EmailCampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EmailCampaign
        fields = (
            'cmid',
            'form',
            'account',
            'list',
            'campaign_title',
            'subject',
            'message_template',
            'timestamp'
        )
