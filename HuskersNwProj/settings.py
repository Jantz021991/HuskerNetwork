"""
Django settings for HuskersNwProj project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'rjd^l47*sjsc4-oh-%el*0pm6$67osqi82*4g1dp7pw@-o&ikr'

# SECURITY WARNING: don't run with debug turned on in production!
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
DEBUG = True

ALLOWED_HOSTS = ['*']
try:
    from .local_settings import *
except ImportError:
    pass



# Application definition

INSTALLED_APPS = [

    'django.contrib.auth',
    'HuskersApp',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social.apps.django_app.default',
    'social_django',
    'rest_framework',
    'widget_tweaks',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'HuskersNwProj.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]


WSGI_APPLICATION = 'HuskersNwProj.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
#
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dbdauaas1adeai',
        'USER': 'dxpuhdpwhcslvx',
        'PASSWORD': 'fffd7ceb6fae2d092afcc358c7c089a3da319fb6c6095ffeaecb0ca262429c1f',
        'HOST': 'ec2-107-21-126-193.compute-1.amazonaws.com',
        'PORT': 5432,
    }

}



# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


LOGIN_REDIRECT_URL = '/home'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),)




EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '587'
EMAIL_HOST_USER = 'msdfall2017team3@gmail.com'
EMAIL_HOST_PASSWORD = 'hlmoijelwgikzkrz'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'Huskers Network< msdfall2017team3@gmail.com>'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Update database configuration with $DATABASE_URL.
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/home/'
SOCIAL_AUTH_LOGIN_URL = '/'

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'


SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.debug.debug',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',
    'social.pipeline.debug.debug',
)

 # python-social-auth settings
AUTHENTICATION_BACKENDS = (
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.open_id.OpenIdAuth',  # for Google authentication
    # 'social_core.backends.google.GoogleOpenId',
    # 'social_core.backends.google.GoogleOpenId',  # for Google authentication
    'social_core.backends.google.GoogleOAuth2',  # for Google authentication
    'social_core.backends.twitter.TwitterOAuth',
    'django.contrib.auth.backends.ModelBackend',
    # 'HuskersApp.authentication.EmailAuthBackend',
)
SOCIAL_AUTH_GOOGLE_OAUTH2_IGNORE_DEFAULT_SCOPE = True
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
'https://www.googleapis.com/auth/userinfo.email',
'https://www.googleapis.com/auth/userinfo.profile'
]
# Google+ SignIn (google-plus)
SOCIAL_AUTH_GOOGLE_PLUS_IGNORE_DEFAULT_SCOPE = True
SOCIAL_AUTH_GOOGLE_PLUS_SCOPE = [
'https://www.googleapis.com/auth/plus.login',
'https://www.googleapis.com/auth/userinfo.email',
'https://www.googleapis.com/auth/userinfo.profile'
]
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

LOGIN_URL = 'login'
LOGOUT_URL = 'logout'


SOCIAL_AUTH_FACEBOOK_KEY = '2013601705575950'
SOCIAL_AUTH_FACEBOOK_SECRET = '93fefcfaf39ced0fe2dfda1b619a0ad2'


SOCIAL_AUTH_TWITTER_KEY = 'NHuZqTxNdEHZqlIRToTgyG9oO'
SOCIAL_AUTH_TWITTER_SECRET = 'b8JN998u3FbuocGBZ2fTAcjo7dB2sB6wuTOYeGZRmXBDzS5imN'

SOCIAL_AUTH_GITHUB_KEY = '5849bb0630de8d4e5768'
SOCIAL_AUTH_GITHUB_SECRET = '74fe946ee95b2c788ba516150639d346248506c4'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '159732030567-t5cnlqgtj7glpdr4r866o399ij3oh1cp.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'W17TJc3olLYImMsti1p_aQhr'