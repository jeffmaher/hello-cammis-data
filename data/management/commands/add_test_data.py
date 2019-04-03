from django.core.management.base import BaseCommand
from data.models import Greeting

class Command(BaseCommand):
    help = "Loads test data into the configured database"

    def _create_greetings(self):
        Greeting(name="cammis", greeting="Hi CA-MMIS!").save()
        Greeting(name="deborah", greeting="Hi Deborah!").save()
        Greeting(name="dave", greeting="Sup Dave!?").save()
        Greeting(name="robert", greeting="Howdy Robert!").save()

    def handle(self, *args, **options):
        self._create_greetings()