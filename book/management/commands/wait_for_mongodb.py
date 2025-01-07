import time
from pymongo import MongoClient
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Espera a que MongoDB esté disponible'

    def handle(self, *args, **kwargs):
        self.stdout.write('Esperando la conexión con MongoDB...')
        connected = False
        while not connected:
            try:
                client = MongoClient(
                    host='db',
                    port=27017,
                    serverSelectionTimeoutMS=1000
                )
                client.server_info()
                connected = True
            except Exception as e:
                self.stdout.write(f'Error conectando a MongoDB: {e}')
                self.stdout.write('Reintentando en 1 segundo...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('¡MongoDB está disponible!'))
