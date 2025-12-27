import os
import dj_database_url # Necesario para la base de datos de Render
from pathlib import Path

# Directorio Base
BASE_DIR = Path(__file__).resolve().parent.parent

# Seguridad
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-ww9j7_=ac%06&-rvo27ci!8f)0^2)+o-m8@1+i^bxys)=%l0@2')
DEBUG = os.environ.get('DEBUG', 'True') == 'True'

# Render Hostnames
# Cambia esto temporalmente para descartar errores de host
ALLOWED_HOSTS = ['*']
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

# Aplicaciones
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic', # Manejo de CSS en producción
    'django.contrib.staticfiles',
    'storages', # Librería para Azure
    'Perfil',
]

# Middlewares
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # Debe ir después de security
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ProyectoHojaDeVida.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], 
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'ProyectoHojaDeVida.wsgi.application'

# BASE DE DATOS: Usa Postgres si existe DATABASE_URL, si no SQLite local
DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///db.sqlite3',
        conn_max_age=600
    )
}

# CONFIGURACIÓN DE ARCHIVOS ESTÁTICOS (CSS, JS)
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# CONFIGURACIÓN DE ALMACENAMIENTO (Azure para Media, Whitenoise para Static)
AZURE_STORAGE_CONNECTION_STRING = os.environ.get('AZURE_STORAGE_CONNECTION_STRING')

if AZURE_STORAGE_CONNECTION_STRING:
    AZURE_CONTAINER = 'media'
    STORAGES = {
        "default": {
            "BACKEND": "storages.backends.azure_storage.AzureStorage",
        },
        "staticfiles": {
            "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
        },
    }
else:
    # Si no hay Azure configurado, guardamos localmente
    MEDIA_URL = '/media/'
    MEDIA_ROOT = BASE_DIR / 'media'
    STORAGES = {
        "default": {
            "BACKEND": "django.core.files.storage.FileSystemStorage",
        },
        "staticfiles": {
            "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
        },
    }

# Idioma y Hora
LANGUAGE_CODE = 'es-ec'
TIME_ZONE = 'America/Guayaquil' 
USE_I18N = True
USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Permite cargar PDFs en iframes (Vital para tu visor)
X_FRAME_OPTIONS = 'SAMEORIGIN'

# Esto evita el error si la variable no está en Render
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-valor-por-defecto-para-que-no-de-error-500')