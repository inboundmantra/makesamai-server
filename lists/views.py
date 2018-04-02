from django.shortcuts import get_object_or_404
from rest_framework import generics

from . import serializers, models


class MultipleFieldLookupMixin(object):
    """
    Apply this mixin to any view or viewset to get multiple field filtering
    based on a `lookup_fields` attribute, instead of the default single field filtering.
    """

    def get_object(self):
        queryset = self.get_queryset()  # Get the base queryset
        queryset = self.filter_queryset(queryset)  # Apply any filter backends
        filter = {}
        for field in self.lookup_fields:
            if self.kwargs[field]:  # Ignore empty fields.
                filter[field] = self.kwargs[field]
        obj = get_object_or_404(queryset, **filter)  # Lookup the object
        self.check_object_permissions(self.request, obj)
        return obj


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
