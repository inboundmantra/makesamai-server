from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from . import models


class ClientRegistrationForm(UserCreationForm):
    """
    A form that creates a user, with no privileges, from the given email and
    password.
    """

    def __init__(self, *args, **kargs):
        super(ClientRegistrationForm, self).__init__(*args, **kargs)

    class Meta:
        model = models.Client
        fields = ("username", "email", "first_name", "last_name",)


class ClientUpdateForm(UserChangeForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    def __init__(self, *args, **kargs):
        super(ClientUpdateForm, self).__init__(*args, **kargs)

    class Meta:
        model = models.Client
        fields = ("username", "email", "first_name", "last_name",)
