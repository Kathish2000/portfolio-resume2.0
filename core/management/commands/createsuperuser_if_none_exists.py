import os
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Create a superuser if none exists'

    def handle(self, *args, **options):
        username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
        email = os.environ.get('DJANGO_SUPERUSER_EMAIL')
        password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')

        if not username or not password:
            self.stdout.write(self.style.WARNING('Superuser credentials not found in environment variables. Skipping creation.'))
            return

        user, created = User.objects.get_or_create(username=username)
        if created:
            self.stdout.write(f'Creating superuser for {username}...')
            user.email = email
            user.set_password(password)
            user.is_superuser = True
            user.is_staff = True
            user.save()
            self.stdout.write(self.style.SUCCESS('Superuser created successfully.'))
        else:
            self.stdout.write(f'Superuser {username} already exists. Updating password and email...')
            user.email = email
            user.set_password(password)
            user.save()
            self.stdout.write(self.style.SUCCESS('Superuser updated successfully.'))
