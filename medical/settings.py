from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4ft5p-6o)2e+9mxsm-wy4urqxyd_78v4npobmf9gh(j*+roa5_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'medical_equipments',
    
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

ROOT_URLCONF = 'medical.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/ 'template'],
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

WSGI_APPLICATION = 'medical.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
"""

DATABASES = {
    'default':{
       'ENGINE':'django.db.backends.postgresql_psycopg2',
       'NAME':'tarragon_myshop',
       'USER':'tarragon_adminuser',
       'PASSWORD':',mVg7^m2Ro_F',
       'HOST':'localhost',
       'PORT':'5432',
      
    }
}

#django.db.backends.postgresql_psycopg2
#django.db.backends.postgresql
 

 """
 # Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True

USE_L10N = True

USE_TZ = True


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  
#EMAIL_BACKEND = 'django_ses.SESBackend'
EMAIL_HOST = 'mail.tarragonhub.co.ke'
EMAIL_HOST_USER = 'client@tarragonhub.co.ke'
EMAIL_HOST_PASSWORD = ".TkEbCFr0oG~"
DEFAULT_FROM_EMAIL = ""
EMAIL_PORT = 26
#EMAIL_PORT = 143
EMAIL_USE_TLS = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS=[
    (BASE_DIR/ 'static')
]

#after informing django where to get the static files, then we inform it where to store the files 
#assets is a random name we have given that folder

STATIC_ROOT=(BASE_DIR/ 'assets')



MEDIA_URL='/media/'
MEDIA_ROOT = (BASE_DIR/ 'media')



"""


AWS_ACCESS_KEY_ID = 'AKIAY4D4KK6WUBMZAD5K'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = "techdemo5115"
#AWS_STORAGE_BUCKET_NAME = "dtechnologies"
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_LOCATION = 'static'
AWS_DEFAULT_ACL='public-read'
#AWS_DEFAULT_ACL = None


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
#DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
DEFAULT_FILE_STORAGE = 'shopping.storage_backends.MediaStorage'





<?xml version="1.0" encoding="UTF-8"?>
<CORSConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
   <CORSRule>
        <AllowedOrigin>*</AllowedOrigin>
        <AllowedMethod>GET</AllowedMethod>
        <AllowedMethod>POST</AllowedMethod>
        <AllowedMethod>PUT</AllowedMethod>
        <AllowedHeader>*</AllowedHeader>
    </CORSRule>
</CORSConfiguration>


"""
