"""
Django settings for Appre project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Importando Unipath
from unipath import Path
RUTA_PROYECTO = Path.cwd()
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*(xh=qj(!$9nrj42bz742k*75hv$^x==m)zc@3rc21i4mw_qy@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Aplicaciones del Sistema "Aplicaciones(carpeta)"."alumno(carpeta)"
    'Aplicaciones.Alumno',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'Appre.urls'

WSGI_APPLICATION = 'Appre.wsgi.application'

# Templates a utilizar
TEMPLATE_DIRS = (
    RUTA_PROYECTO.child('templates'),
)
# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'Appre.db'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'es-MX'

TIME_ZONE = 'America/Mexico_City'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
# MEDIA RUTA (PARA GUARDAR IMAGENES)
MEDIA_ROOT = RUTA_PROYECTO.child('Imagenes')
# Para mostrar la Imagen en el Template
MEDIA_URL = 'http://127.0.0.1:8000/Imagenes/'
STATIC_URL = '/static/'

# Ruta de los archivos estaticos
STATICFILES_DIRS = (
    RUTA_PROYECTO.child('static'),
)
