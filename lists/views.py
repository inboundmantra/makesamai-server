from rest_framework import generics

from . import serializers, models


class ListList(generics.ListCreateAPIView):
    serializer_class = serializers.ListSerializer

    def get_queryset(self):
        """
        This view should return a list of all the Lists for
        the user as determined by the account portion of the URL.
        """
        uaid = self.kwargs['account']
        return models.List.objects.filter(account=uaid).order_by('-created_on')


class ListRetrieve(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.ListSerializer

    def get_queryset(self):
        uaid = self.kwargs['account']
        ugid = self.kwargs['list']
        return models.List.objects.get(account=uaid, ugid=ugid)
