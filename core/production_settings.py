from core.base_settings import *
from dotenv import load_dotenv

load_dotenv()  # loads the configs from .env
print("Database password is:", os.getenv("DB_PASSWORD"))
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'tmo$worlddata',
        'USER': 'tmo',
        'PASSWORD': os.getenv("DB_PASSWORD"),
        'HOST': 'tmo.mysql.pythonanywhere-services.com',
        'PORT': '3306',
    }
}

DEBUG = False
ALLOWED_HOSTS = ['tmo.pythonanywhere.com']


# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True  # Use TLS (True for Gmail)
# # EMAIL_HOST_USER = 'morganmcknight@gmail.com'  # Your Gmail email address
# # EMAIL_HOST_PASSWORD = 'rkjxohiawwncphgp'  # Your Gmail password or an app password
# EMAIL_USE_SSL = False
#
# FOOTER_MESSAGE = "Production Version"