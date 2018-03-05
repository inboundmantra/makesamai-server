from rest_framework import generics

from . import models, serializers


class UserAccountList(generics.ListAPIView):
    serializer_class = serializers.AccountSerializer

    def get_queryset(self):
        """
        This view should return a list of all the accounts for
        the user as determined by the user portion of the URL.
        """
        user = self.kwargs['user']
        return models.Account.account_list.user_accounts(user=user).order_by('-created_on')
