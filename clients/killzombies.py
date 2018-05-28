from django.core.management.base import BaseCommand

from clients.models import Client


class Command(BaseCommand):
    help = "Deletes Unconfirmed Users"

    def handle(self, *args, **options):
        for user in Client.objects.all().filter(date_joined__gte=7):
            if not user.is_confirmed:
                user.delete()

            self.stdout.write(self.style.SUCCESS('Successfully Killed Zombie "%s"' % user.email))
