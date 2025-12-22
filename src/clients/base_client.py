import requests
from src.config.settings import settings


class BaseClient:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update(settings.DEFAULT_HEADERS)

    def get(self, endpoint, params=None):
        return self.session.get(
            url=f"{settings.BASE_URL}{endpoint}",
            params=params,
            timeout=settings.TIMEOUT
        )

    def post(self, endpoint, json=None):
        return self.session.post(
            url=f"{settings.BASE_URL}{endpoint}",
            json=json,
            timeout=settings.TIMEOUT
        )