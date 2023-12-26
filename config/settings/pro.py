from .base import *


SECRET_KEY = (get_secret('SECRET_KEY'),
              'django-insecure-w1q2!*29ja2_oaj=&!-stm8a5q7!3ymq!knx78h@)%v1-y80fl')


DEBUG = False

ALLOWED_HOSTS = []

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'ptdb',
#         'USER': 'ptdbuser',
#         'PASSWORD': get_secret('PGRESS_PASSWORD'),
#         'HOST': 'localhost',
#         'PORT': '5432'
#     }
# }
