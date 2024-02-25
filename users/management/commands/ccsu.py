import os
from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@admin.pro',
            first_name='Admin',
            last_name='Admin',
            is_active=True,
            role='admin'
        )

        user.set_password(os.getenv('CSU_PASSWORD'))
        user.save()
