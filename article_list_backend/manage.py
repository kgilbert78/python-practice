#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'article_list_backend.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()


# COMMON COMMANDS:
# python manage.py check
# python manage.py makemigrations
# python manage.py migrate

# python manage.py runserver

# python manage.py shell


# INITIAL SETUP:
# 1) create virtualenv & activate it
# 2) pip install Django
# 3) pip install djangorestframework
# 4) django-admin startproject <project-name> 
# 5) python manage.py migrate 
#     (...now you can access the default tables in Beekeeper Studio)
# 6) python manage.py startapp <app-name> 
#     (...can have multiple apps in one project)
# 7) python manage.py createsuperuser
#     (...create admin - enter username, email & password)
#     Go to http://localhost:8000/admin/ to log in with these.