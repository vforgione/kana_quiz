import os


# helpers
CONFIG_DIR = os.path.dirname(__file__)

BASE_DIR = os.path.dirname(CONFIG_DIR)


# debug
DEBUG = os.environ.get('DEBUG', True)

TEMPLATE_DEBUG = DEBUG


# db config
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.' + os.environ.get('DB_ENGINE', 'sqlite3'),
        'NAME': os.environ.get('DB_NAME', os.path.join(CONFIG_DIR, 'db.sqlite3')),
        'USER': os.environ.get('DB_USER', ''),
        'PASSWORD': os.environ.get('DB_PASSWORD', ''),
        'HOST': os.environ.get('DB_HOST', ''),
        'PORT': os.environ.get('DB_PORT', ''),
    }
}


# apps config
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # model migrations
    'south',

    # project apps
    'apps.kana',
)


# middleware config
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


# static config
STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = (
    os.path.join(CONFIG_DIR, 'static'),
)


# template config
TEMPLATE_DIRS = (
    os.path.join(CONFIG_DIR, 'templates'),
)


# secrets
SECRET_KEY = os.environ.get('SECRET_KEY', '3hpqj$8y=-vcs-5_he6boni-u!r6sjwoa80r0%vvlo$e5iak+j')


# project config
ROOT_URLCONF = 'kana_quiz.urls'

WSGI_APPLICATION = 'kana_quiz.wsgi.application'


# site config
ALLOWED_HOSTS = []

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
