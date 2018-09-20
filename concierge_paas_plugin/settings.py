import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'concierge_paas_plugin.settings')

INSTALLED_APPS = [
    # 'django.contrib.admin',
    # 'django.contrib.auth',
    # 'django.contrib.contenttypes',
    # 'oidc_provider',
    'concierge_paas_plugin',
]

SECRET_KEY = os.getenv('SECRET_KEY')