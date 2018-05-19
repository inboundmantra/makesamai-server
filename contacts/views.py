from django.core.mail import send_mail
from rest_framework import generics, permissions, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from MakeSamai.mixins import MultipleFieldLookupMixin
from . import models, serializers
import logging

logger = logging.getLogger(__name__)


class ContactList(generics.ListCreateAPIView):
    serializer_class = serializers.ContactSerializer

    def get_queryset(self):
        """
        This view should return a list of all the Lists for
        the user as determined by the account portion of the URL.
        """
        uaid = self.kwargs['account']
        return models.Contact.objects.filter(account=uaid).order_by('-created_on')


class ContactCreate(APIView):
    """
    Creates the contact.
    """
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format='json'):
        serializer = serializers.ContactSerializer(data=request.data)
        if serializer.is_valid():
            contact = serializer.save()
            try:
                send_mail(
                    "Thank You For Submitting Your Details",
                    "Hi " + contact.first_name + ",\n Thank You For Submitting Your Details.",
                    'notification-noreply@makesamai.com',
                    [contact.email],
                    fail_silently=True,
                    html_message="Hi " + contact.first_name + ",<br><br> Thank you for filling " + contact.form.title + " on " + contact.landing_page.title + " ! <br><br><br><br>From,<br>" + contact.account.name,
                )
                send_mail(
                    "New Contact Created: " + contact.first_name + " " + contact.last_name,
                    "Hi ,\n New Contact Was Created \nName: " + contact.first_name + " " + contact.last_name,
                    'notification-noreply@makesamai.com',
                    [contact.account.owner.email],
                    fail_silently=True,
                    html_message="Hi " + contact.account.owner.first_name + ",<br><br> New Contact was created from " + contact.form.title + " on " + contact.landing_page.title + " !<br> Name: " + contact.first_name + " " + contact.last_name + " <br><br><br><br>From,<br>Team MakeSamai",
                )
            except:
                logger.error('Mail Send Error: ', exc_info=True)
            if contact:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContactRetrieve(MultipleFieldLookupMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Contact.objects.all()
    serializer_class = serializers.ContactSerializer
    lookup_fields = ('ucid', 'account')


class AddressCreate(generics.CreateAPIView):
    queryset = models.Address.objects.all()
    serializer_class = serializers.AddressSerializer
    permission_classes = (AllowAny,)


class AddressRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Address.objects.all()
    serializer_class = serializers.AddressSerializer
    lookup_field = 'address'
