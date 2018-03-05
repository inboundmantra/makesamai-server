from django.db import models


class AccountQuerySet(models.QuerySet):
    def user_accounts(self, user):
        return self.filter(owner=user)


class AccountManager(models.Manager):
    def get_queryset(self):
        return AccountQuerySet(self.model, using=self._db)

    def user_accounts(self, user):
        return self.get_queryset().user_accounts(user)
