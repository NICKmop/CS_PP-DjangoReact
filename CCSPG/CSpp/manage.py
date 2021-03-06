#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os, sys
from pathlib import Path


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CSpp_backend.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # execute_from_command_line(sys.argv)

    try:
        if sys.argv[2] == 'react':
            project_root = os.getcwd();
            os.chdir(os.path.join(project_root, "CSpp_frontend"));
            os.system("npm run build");
            os.chdir(project_root);
            sys.argv.pop(2);
    except IndexError:
        print("1")
        execute_from_command_line(sys.argv);
    else:
        print("2")
        execute_from_command_line(sys.argv);


if __name__ == '__main__':
    main()
