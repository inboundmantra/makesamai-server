from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny

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
    lookup_fields = ('ulid', 'account')