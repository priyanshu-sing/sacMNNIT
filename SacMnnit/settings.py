# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os 
from unipath import Path
from decouple import Csv,config
import dj_database_url
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PROJECT_DIR = Path(__file__).parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/


#for local

SECRET_KEY = '(&yn&vabv-*qok27b=^m7xq5)o29!vitm%+$utrp300*ua+crj'#os.environ['SECRET_KEY']
DEBUG = True # if you set it False then the allowed host must be saved to som port like 4 7 etc or just set it to all like ['*']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': PROJECT_DIR.child('db.sqlite3'),
    }
} 
ALLOWED_HOSTS = ['172.31.102.250','210.212.49.51', 'sac.mnnit.ac.in', 'localhost']

#for local

#for heroku
# SECRET_KEY = config('SECRET_KEY')
# DEBUG = config('DEBUG', default=False, cast=bool)
# DATABASES = {
#     'default': dj_database_url.config(
#         default=config('DATABASE_URL'),
#     )
# }
# ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())   
#end heroku

ADMINS = (   
    ('WOC','wocmnnit@gmail.com'),
    ('Deepak Bharti','deepakbharti823@gmail.com'),
    ('Priyanshu Singh', 'priyanshusingh@mnnit.ac.in'),
    )
      
  
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587

''' 
If using gmail, you will need to
unlock Captcha to enable Django 
to  send for you:
https://accounts.google.com/displayunlockcaptcha
'''

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #custom apps
    'Technical',
    'Cultural',
    'Athletics',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'SacMnnit.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [PROJECT_DIR.child('templates'),
                PROJECT_DIR.child('templates','templates'),
                ],
        'APP_DIRS': True, 
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'SacMnnit.wsgi.application'

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
# https://docs.djangoproject.com/en/1.8/topics/i18n/

# DATE_INPUT_FORMATS = ('%d-%m-%Y','%Y-%m-%d')

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
# USE_I18N = True
USE_L10N = True
USE_TZ = True

IPRESTRICT_GEOIP_ENABLED = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = '/home/sac-dev/Desktop/sacPortal/SacMnnit/static_root/'
# static_root is the server outside our project wher e static files are sent to store

STATICFILES_DIRS = (
    PROJECT_DIR.child('static'),
    #'/var/www/static/',
    )

MEDIA_URL = '/media/'
MEDIA_ROOT = '/home/sac-dev/Desktop/sacPortal/SacMnnit/media_root/'

#Crispy forms tags settings
CRISPY_TEMPLATE_PACK = 'bootstrap3'


SITE_ID = 1
# added on 15_jan
LOGIN_URL = '/'
LOGIN_REDIRECT_URL = '/'
 
ALLOWED_SIGNUP_DOMAINS = ['*']
 
FILE_UPLOAD_TEMP_DIR = '/tmp/'
FILE_UPLOAD_PERMISSIONS = 0o644

#added to host on heroku
# STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

import netifaces

# Find out what the IP addresses are at run time
# This is necessary because otherwise Gunicorn will reject the connections
def ip_addresses():
    ip_list = []
    for interface in netifaces.interfaces():
        addrs = netifaces.ifaddresses(interface)
        for x in (netifaces.AF_INET, netifaces.AF_INET6):
            if x in addrs:
                ip_list.append(addrs[x][0]['addr'])
    return ip_list

# Discover our IP address
ALLOWED_HOSTS += ip_addresses()
