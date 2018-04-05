from django.core.mail import send_mail
from rest_framework import generics, permissions, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from MakeSamai.mixins import MultipleFieldLookupMixin
from . import models, serializers


class ContactList(generics.ListCreateAPIView):
    queryset = models.Contact.objects.all().order_by('-created_on')
    serializer_class = serializers.ContactSerializer
    lookup_field = 'account'


class ContactCreate(APIView):
    """
    Creates the contact.
    """
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format='json'):
        serializer = serializers.ContactSerializer(data=request.data)
        if serializer.is_valid():
            contact = serializer.save()
            send_mail(
                "Welcome To Make Samai!",
                "Hi " + contact.first_name + ",\n We are glad to have you onboard Make Samai. Get Started With Superpowered Marketing Today.",
                'notification-noreply@makesamai.com',
                [contact.email],
                fail_silently=True,
                html_message="Hi " + contact.first_name + ",<br><br> Welcome to <strong>MakeSamai</strong>! We're so excited that you made some samai to sign up with us. <br><br>See what we did there? ;). <br><br>Get Started With Superpowered Marketing <a href='http://www.makesamai.com/help'>here</a>. <br><br>We look forward to working with you to superpower your marketing efforts. Feel free to reach out to us at <a href='mailto:support@makesamai.com'>support@makesamai.com</a><br><br><br><br>Love,<br>Team MakeSamai",
            )
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
