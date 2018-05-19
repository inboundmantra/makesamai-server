# Create your views here.
from rest_framework import generics

from MakeSamai.mixins import MultipleFieldLookupMixin
from . import models, serializers


class EmailCampaignList(generics.ListCreateAPIView):
    serializer_class = serializers.EmailCampaignSerializer

    def get_queryset(self):
        """
        This view should return a list of all the Email Campaigns for
        the user as determined by the account portion of the URL.
        """
        uaid = self.kwargs['account']
        return models.EmailCampaign.objects.filter(account=uaid).order_by('-timestamp')


class EmailCampaignRetrieve(MultipleFieldLookupMixin, generics.RetrieveAPIView):
    queryset = models.EmailCampaign.objects.all()
    serializer_class = serializers.EmailCampaignSerializer
    lookup_fields = ('cmid', 'account')


class EmailListRetrieve(MultipleFieldLookupMixin, generics.ListAPIView):
    queryset = models.Email.objects.all()
    serializer_class = serializers.EmailSerializer
    lookup_fields = ('cmid', 'account')
