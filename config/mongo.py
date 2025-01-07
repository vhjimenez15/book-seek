from pymongo import MongoClient
from django.conf import settings


class MongoDB:
    def __init__(self):
        self.client = MongoClient(
            host=settings.MONGO_DB_SETTINGS['HOST'],
            port=int(settings.MONGO_DB_SETTINGS['PORT']),
            username=settings.MONGO_DB_SETTINGS.get('USERNAME'),
            password=settings.MONGO_DB_SETTINGS.get('PASSWORD'),
            authSource=settings.MONGO_DB_SETTINGS.get('AUTH_SOURCE', 'admin'),
        )
        self.db = self.client[settings.MONGO_DB_SETTINGS['NAME']]

    def get_collection(self, collection_name):
        return self.db[collection_name]


# Instancia global para el proyecto
mongodb = MongoDB()
