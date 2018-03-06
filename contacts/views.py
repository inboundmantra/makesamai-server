from rest_framework import generics
from . import models, serializers


class AddressDetail(generics.RetrieveUpdateAPIView):
    serializer_class = serializers.AddressSerializer

    def get_queryset(self):
        id = self.kwargs['address']
        return models.Address.objects.get(id=id)


class ContactList(generics.ListAPIView):
    serializer_class = serializers.ContactSerializer

    def get_queryset(self):
        """
        This view should return a list of all the contact for
        the user as determined by the account portion of the URL.
        """
        account = self.kwargs['account']
        return models.Contact.objects.filter(account=account).order_by('-created_on')
