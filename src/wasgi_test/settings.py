from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DEBUG = False
SECRET_KEY = 'django-insecure-@p2u(jav)b988lh+$=b9(03s)zmg6*vq5r*+h*!n1=6)zf=m8@'
ALLOWED_HOSTS = ['*']
INSTALLED_APPS = []
MIDDLEWARE = []
ROOT_URLCONF = 'wasgi_test.urls'
TEMPLATES = []
WSGI_APPLICATION = 'wasgi_test.wsgi.application'
ASGI_APPLICATION = 'wasgi_test.asgi.application'
DATABASES = {}
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_URL = '/static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
