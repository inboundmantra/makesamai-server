from rest_framework import generics

from MakeSamai.mixins import MultipleFieldLookupMixin
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


class ListRetrieve(MultipleFieldLookupMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = models.List.objects.all()
    serializer_class = serializers.ListSerializer
    lookup_fields = ('ugid', 'account')
