from rest_framework import generics
from rest_framework.permissions import AllowAny

from MakeSamai.mixins import MultipleFieldLookupMixin
from . import serializers, models


class FormList(generics.ListCreateAPIView):
    serializer_class = serializers.FormSerializer

    def get_queryset(self):
        """
        This view should return a list of all the forms for
        the user as determined by the account portion of the URL.
        """
        uaid = self.kwargs['account']
        return models.Form.objects.filter(account=uaid).order_by('-created_on')


class FormRetrieve(MultipleFieldLookupMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Form.objects.all()
    serializer_class = serializers.DashboardFormSerializer
    lookup_fields = ('ufid', 'account')


class FormRender(MultipleFieldLookupMixin, generics.RetrieveAPIView):
    queryset = models.Form.objects.all()
    serializer_class = serializers.FormSerializer
    permission_classes = (AllowAny,)
    lookup_fields = ('ufid', 'account')
