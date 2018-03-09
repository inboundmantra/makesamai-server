from rest_framework import generics

from . import models, serializers


class AccountCreate(generics.CreateAPIView):
    serializer_class = serializers.AccountSerializer


class AccountRetrieve(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.AccountSerializer

    def get_queryset(self):
        """
        This view should return a list of all the accounts for
        the user as determined by the user portion of the URL.
        """
        uaid = self.kwargs['uaid']
        return models.Account.objects.get(uaid=uaid)


class UserAccountList(generics.ListAPIView):
    serializer_class = serializers.AccountSerializer

    def get_queryset(self):
        """
        This view should return a list of all the accounts for
        the user as determined by the user portion of the URL.
        """
        user = self.kwargs['user']
        return models.Account.objects.user_accounts(user=user).order_by('-created_on')
