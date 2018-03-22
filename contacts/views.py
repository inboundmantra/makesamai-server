from rest_framework import generics
from rest_framework.permissions import AllowAny

from . import models, serializers


class ContactList(generics.ListAPIView):
    serializer_class = serializers.ContactSerializer

    def get_queryset(self):
        """
        This view should return a list of all the contact for
        the user as determined by the account portion of the URL.
        """
        uaid = self.kwargs['account']
        return models.Contact.objects.filter(account=uaid).order_by('-created_on')


class ContactCreate(generics.CreateAPIView):
    queryset = models.Contact.objects.all()
    serializer_class = serializers.ContactSerializer
    permission_classes = (AllowAny,)


class AddressCreate(generics.CreateAPIView):
    queryset = models.Address.objects.all()
    serializer_class = serializers.AddressSerializer
    permission_classes = (AllowAny,)


class ContactRetrieve(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.ContactSerializer

    def get_queryset(self):
        """
                This view should return a list of all the contact for
                the user as determined by the account portion of the URL.
                """
        uaid = self.kwargs['account']
        return models.Contact.objects.filter(account=uaid)


class AddressRetrieve(generics.RetrieveUpdateAPIView):
    serializer_class = serializers.AddressSerializer

    def get_queryset(self):
        id = self.kwargs['address']
        return models.Address.objects.get(id=id)
