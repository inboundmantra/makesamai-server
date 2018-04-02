from rest_framework import generics
from rest_framework.permissions import AllowAny

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


class FormRetrieve(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.DashboardFormSerializer
    lookup_url_kwarg = 'ufid'

    def get_queryset(self):
        uaid = self.kwargs['account']
        ufid = self.kwargs['form']
        return models.Form.objects.get(account=uaid, ufid=ufid)


class FormRender(generics.RetrieveAPIView):
    serializer_class = serializers.FormSerializer
    permission_classes = (AllowAny,)
    lookup_url_kwarg = 'ufid'

    def get_queryset(self):
        uaid = self.kwargs['account']
        ufid = self.kwargs['form']
        return models.Form.objects.get(account=uaid, ufid=ufid)
