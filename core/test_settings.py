from core.base_settings import *
from dotenv import load_dotenv

load_dotenv()  # Ensure this loads your local .env file appropriate for development

# Adjust the DATABASES setting to your local development database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',  # Or use your local MySQL configuration
    }
}

DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'www.onlyworlds.com']  # Adding local hosts for development

# You may uncomment and adjust the EMAIL_BACKEND and related settings for local development testing if needed

# Similarly, adjust other settings as required for your local development environment