from django.conf import settings
from django.core.mail import send_mail
from rest_framework import status, generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from . import serializers


class CreateClient(APIView):
    """
    Creates the user.
    """
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format='json'):
        serializer = serializers.ClientSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            send_mail(
                "Welcome To Make Samai!",
                "Hi " + user.first_name + ",\n We are glad to have you onboard Make Samai. Get Started With Superpowered Marketing Today.",
                'notification-noreply@makesamai.com',
                [user.email],
                fail_silently=True,
                html_message="Hi " + user.first_name + ",<br> We are glad to have you onboard <strong>MakeSamai</strong>. Get Started With Superpowered Marketing Today.<br><br>Regards,<br>Team MakeSamai",
            )
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserView(generics.RetrieveUpdateAPIView):
    """
    Use this endpoint to retrieve/update user.
    """
    model = settings.AUTH_USER_MODEL
    serializer_class = serializers.ClientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, *args, **kwargs):
        return self.request.user
