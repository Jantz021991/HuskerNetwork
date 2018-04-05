import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

####
## Only for virtual ENV
####
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

####
## Only for DOCKER environment
####
# ROOT_URLCONF = 'HuskersNwProj.urls'
# WSGI_APPLICATION = 'HuskersNwProj.wsgi.application'

# DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.postgresql',
#             'NAME': 'postgres',
#             'USER': 'postgres',
#             'HOST': 'db',
#             'PORT': 5432,
#         }
#     }

DEBUG = True

