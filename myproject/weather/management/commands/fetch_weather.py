from django.core.management.base import BaseCommand, CommandError
from weather.views import fetch_weather_data

class Command(BaseCommand):
    help = 'Fetches weather data for a given city'

    def add_arguments(self, parser):
        parser.add_argument('city', type=str, help='The city to fetch weather data for')

    def handle(self, *args, **options):
        city = options['city']
        try:
            fetch_weather_data(city)
            self.stdout.write(self.style.SUCCESS(f'Successfully fetched weather data for {city}'))
        except Exception as e:
            raise CommandError(f'Error fetching weather data for {city}: {e}')