import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'concierge_paas_plugin.settings')

INSTALLED_APPS = [
    'concierge_paas_plugin'
]

SECRET_KEY = os.getenv('SECRET_KEY')