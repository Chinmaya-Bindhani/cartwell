from .base import  *
from pathlib import  Path
import environ

PROJECT_ROOT = Path(__file__).resolve().parents[2]
environ.Env.read_env(PROJECT_ROOT / ".env")

# CONFIGURATIONS OF LOCAL DATABASE FOR DEVELOPMENT AND TESTING PURPOSE OF AUTHENTICATION SERVICE

from os import  getenv
DATABASES = {
    'default': {
        'ENGINE': f'django.db.backends.{getenv('WHICH_DB')}',
        'NAME': getenv('DB_NAME'),
        'USER': getenv('DB_USER'),
        'PASSWORD': getenv('DB_PASSWORD'),
    }
}