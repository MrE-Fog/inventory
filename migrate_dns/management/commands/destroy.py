from django.core.management.base import BaseCommand
from mdns.destructo import destroy


class Command(BaseCommand):
    args = ''
    def handle(self, *args, **options):
        destroy()  # Whipe the db
