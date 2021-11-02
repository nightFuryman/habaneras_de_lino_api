import django_on_heroku
# import dj-database-url
from .base import *



django_on_heroku.settings(locals())


DEBUG = False

SECRET_KEY= os.environ["SECRET_KEY"]


CORS_ALLOWED_ORIGINS = [
    # Frontend
]

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.environ['CLOUD_NAME'],
    'API_KEY': os.environ['CLOUD_API_KEY'],
    'API_SECRET': os.environ['CLOUD_API_SECRET'],
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ["DB_NAME"],
        'USER': os.environ["DB_USER"],
        'PASSWORD': os.environ["DB_PASSWORD"],
        'HOST': os.environ["DB_HOST"],
        'PORT': 5432,
    }
}

STRIPE_PUBLISHABLE_KEY=os.environ["STRIPE_PUBLISHABLE_KEY"]
STRIPE_SECRET_KEY=os.environ["STRIPE_SECRET_KEY"]

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_USE_TLS = True
# EMAIL_PORT = 587
# EMAIL_HOST_USER = os.environ["EMAIL_HOST_USER"]
# EMAIL_HOST_PASSWORD = os.environ["EMAIL_HOST_PASSWORD"]