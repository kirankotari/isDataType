from distutils.util import strtobool
import logging

def isInt(arg):
    try:
        float(arg)
    except ValueError:
        return False
    else:
        return float(arg).is_integer()

def isFloat(arg, allow_zeros=True):
    try:
        float(arg)
    except ValueError:
        return False
    else:
        if allow_zeros == False:
            return True if float(arg).is_integer() == False else False
        return True

def isString(arg):
    if type(arg) == str:
        return True
    return False

def isBool(arg):
    try:
        strtobool(arg)
    except ValueError:
        return False
    # TODO: need to use this on convertion bool(strtobool(arg))
    return True

def isList(arg):
    pass

def isDict(arg):
    pass

def isSet(arg):
    pass

def isTuple(arg):
    pass

def isComplex(arg):
    pass

def isListInt(arg):
    pass

def isListFloat(arg):
    pass

def isListString(arg):
    pass

def isListDict(arg):
    pass

