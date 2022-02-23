from email import parser
from lib2to3.pytree import Base
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

class Command(BaseCommand):
    help = "Create Random users"

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of users to be created')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        # print(total)
        for i in range(total):
            User.objects.create_user(username=get_random_string(5), email='', password='123')

