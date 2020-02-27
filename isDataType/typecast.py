from distutils.util import strtobool
import logging

def toBool(arg):
    try:
        strtobool(arg)
    except ValueError as e:
        # TODO: need to log the messages.
        return None
    else:
        return bool(strtobool(arg))