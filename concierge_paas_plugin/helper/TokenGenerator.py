from django.utils.crypto import get_random_string

class Generator():
    def create(self):
        return get_random_string(length=40)