from rest_framework import generics

from . import models, serializers


class AccountRetrieve(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.AccountSerializer

    def get_queryset(self):
        """
        This view should return a list of all the accounts for
        the user as determined by the user portion of the URL.
        """
        uaid = self.kwargs['uaid']
        return models.Account.objects.get(uaid=uaid)


class UserAccountList(generics.ListCreateAPIView):
    serializer_class = serializers.AccountSerializer
    user = None

    def get_queryset(self):
        """
        This view should return a list of all the accounts for
        the user as determined by the user portion of the URL.
        """
        if self.request and hasattr(self.request, "user"):
            self.user = self.request.user
        return models.Account.objects.user_accounts(user=self.user).order_by('-created_on')
