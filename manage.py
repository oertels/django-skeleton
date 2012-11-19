#!/usr/bin/env python
import os
import sys
from django_skeleton.settings import rel

for path in ('apps', 'contrib',)[::-1]:  # reverse order
    sys.path.insert(0, rel(path))

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_skeleton.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
