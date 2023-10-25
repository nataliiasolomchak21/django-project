# This is the shebang line specifying to use the python interpreter.
#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
# Imports the os module to interact with the operating system.
import os
# Imports the sys module to get command line arguments.
import sys


def main():
    """Run administrative tasks."""
    # Sets the DJANGO_SETTINGS_MODULE environment variable to tell Django which settings to use.
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_todo.settings')
    try:
        # Try to import the execute_from_command_line function from Django.
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # If import fails, raise an error explaining Django not properly installed.
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # If no errors, call the function to execute admin commands.
    execute_from_command_line(sys.argv)

# Python trick to run main() if executed directly.
if __name__ == '__main__':
    main()
