from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from . import models, serializers


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


class ContactList(generics.ListCreateAPIView):
    serializer_class = serializers.ContactSerializer

    def get_queryset(self):
        """
        This view should return a list of all the contact for
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


class AddressCreate(generics.CreateAPIView):
    queryset = models.Address.objects.all()
    serializer_class = serializers.AddressSerializer
    permission_classes = (AllowAny,)


class ContactRetrieve(MultipleFieldLookupMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Contact.objects.all()
    serializer_class = serializers.ContactSerializer
    lookup_fields = ('ucid', 'account')


class AddressRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Address.objects.all()
    serializer_class = serializers.AddressSerializer
    lookup_field = 'address'
