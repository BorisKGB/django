import os
from dotenv import load_dotenv

load_dotenv()

try:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoproject.settings')
    from django.core.management import call_command
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()
except ImportError as exc:
    raise ImportError("Couldn't import Django.") from exc

call_command('runserver', '0.0.0.0:8000')
