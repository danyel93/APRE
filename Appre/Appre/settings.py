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

SITE_ID=1
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
    'Aplicaciones.Perfil',
    'Aplicaciones.Principal',
    # Requerido por django-allouth
    'django.contrib.sites',
    # Django-allauth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
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



# Iniciando django-allauth
TEMPLATE_CONTEXT_PROCESSORS = (
    
    # Required by allauth template tags
    "django.core.context_processors.request",
    # allauth specific context processors
    "allauth.account.context_processors.account",
    "allauth.socialaccount.context_processors.socialaccount",
    "django.contrib.auth.context_processors.auth",
    'django.core.context_processors.debug', 
    'django.core.context_processors.i18n', 
    'django.core.context_processors.media', 
    'django.core.context_processors.static', 
    'django.core.context_processors.tz', 
    'django.contrib.messages.context_processors.messages'

)

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)
 
# auth and allauth settings
LOGIN_REDIRECT_URL = '/'
SOCIALACCOUNT_QUERY_EMAIL = True
SOCIALACCOUNT_PROVIDERS = {
    
    'facebook': {
        'SCOPE': ['email', 'publish_stream'],
        'METHOD': 'js_sdk',  # instead of 'oauth2'
        'VERIFIED_EMAIL': False

    },
    'google': {
        'SCOPE': ['profile', 'email'],
        'AUTH_PARAMS': { 'access_type': 'online' }

    },
}
# Cuenta de correo electronico

EMAIL_HOST='mail.grupocanton.com'
EMAIL_HOST_USER='arturo@grupocanton.com'
EMAIL_HOST_PASSWORD='J2ns392(sd_)skl'
EMAIL_PORT=587
EMAIL_USE_TLS = True
# auth and allauth settings
LOGIN_REDIRECT_URL = '/'
SOCIALACCOUNT_QUERY_EMAIL = True 
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_AUTHENTICATION_METHOD = "username_email"
ACCOUNT_USERNAME_MIN_LENGTH = 10
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_SUBJECT_PREFIX ="Tu Aviso"
SOCIALACCOUNT_EMAIL_VERIFICATION =  "optional"
SOCIALACCOUNT_EMAIL_REQUIRED =  False 