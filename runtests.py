from django.conf import settings

settings.configure(
    INSTALLED_APPS=[
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.admin',
        'banners',
    ],
    DATABASES={
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": ":memory:",
        }
    },
)

from django.core.management import call_command
call_command("test", "django_ses")
