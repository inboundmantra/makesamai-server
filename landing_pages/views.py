from rest_framework import generics
from rest_framework.permissions import AllowAny

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


class LandingPageRetrieve(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.LandingPageSerializer

    def get_queryset(self):
        uaid = self.kwargs['account']
        ulid = self.kwargs['ulid']
        return models.LandingPage.objects.get(account=uaid, ulid=ulid)


class LandingPageRender(generics.RetrieveAPIView):
    serializer_class = serializers.LandingPageSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        uaid = self.kwargs['account']
        ulid = self.kwargs['ulid']
        return models.LandingPage.objects.get(account=uaid, ulid=ulid)
