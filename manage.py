#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import datetime
import os
import sys

from components import update_information_time


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gr_project.settings')
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
    cur_time = datetime.datetime.now()
    update_information_time(cur_time.hour - 1, cur_time.minute, cur_time.second)
    main()
