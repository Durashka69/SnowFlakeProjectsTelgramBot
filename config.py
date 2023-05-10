import os
import django

from dotenv import load_dotenv


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()


from django.conf import settings


load_dotenv()
API_TOKEN = os.getenv("TOKEN")
