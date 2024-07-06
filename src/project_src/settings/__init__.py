import sys

try:
    from .local import *
except ImportError:
    sys.stderr.write("Unable to read project_src.settings.local.py\n")
    DEBUG = False
