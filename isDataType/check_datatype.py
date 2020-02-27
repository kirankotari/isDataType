from distutils.util import strtobool
import logging

def isInt(arg, remove_decimals=False):
    try:
        float(arg)
    except ValueError:
        return False
    else:
        return float(arg).is_integer() if remove_decimals == False else True

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
    return True

def isListInt(argList, remove_decimals=False):
    return all(isInt(each_arg, remove_decimals) for each_arg in argList)

def isListFloat(argList, allow_zeros=True):
    return all(isFloat(each_arg, allow_zeros) for each_arg in argList)

def isListString(argList):
    return all(isString(each_arg) for each_arg in argList)

