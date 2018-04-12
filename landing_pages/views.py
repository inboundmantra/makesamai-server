from rest_framework import generics
from rest_framework.permissions import AllowAny

from MakeSamai.mixins import MultipleFieldLookupMixin
from . import serializers, models


class LandingPageList(generics.ListCreateAPIView):
    serializer_class = serializers.LandingPageSerializer

    def get_queryset(self):
        """
        This view should return a list of all the LPs for
        the user as determined by the account portion of the URL.
        """
        uaid = self.kwargs['account']
        return models.LandingPage.objects.filter(account=uaid).order_by('-created_on')


class LandingPageRetrieve(MultipleFieldLookupMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = models.LandingPage.objects.all()
    serializer_class = serializers.LandingPageSerializer
    lookup_fields = ('ulid', 'account')


class LandingPageRender(MultipleFieldLookupMixin, generics.RetrieveAPIView):
    queryset = models.LandingPage.objects.all()
    serializer_class = serializers.LandingPageSerializer
    permission_classes = (AllowAny,)
    lookup_fields = ('slug', 'account')
