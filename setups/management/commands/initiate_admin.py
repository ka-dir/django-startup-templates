from django.core.management.base import BaseCommand
import os
from django.conf import settings
from dotenv import load_dotenv

from setups.models import CustomUser as User

env_path = os.path.join(settings.BASE_DIR, ".env")
load_dotenv(dotenv_path=env_path)


class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Creating superuser admin account')
        if not User.objects.all().exists():
            User.objects.create_superuser(
                email=os.environ.get('DJANGO_SU_EMAIL'),
                username=os.environ.get('DJANGO_SU_NAME'),
                password=os.environ.get('DJANGO_SU_PASSWORD'))
            print('Superuser admin account created successfully')
        else:
            print("Admin already exists")
