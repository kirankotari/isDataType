from distutils.util import strtobool
import logging
from .check_datatype import isListInt, isListFloat, isListString, isBool

def toBool(arg):
    if isBool(arg):
        return bool(strtobool(arg))
    else:
        logging.error("Invalid input, Error: {}".format(e))

def toInt(argList, remove_decimals=False):
    if isListInt(argList, remove_decimals):
        return map(int, argList)
    else:
        logging.error("Invlaid input, Error: Couldn't able to convert")

def toFloat(argList, allow_zeros=True):
    if isListFloat(argList, allow_zeros):
        return map(float, argList)
    else:
        logging.error("Invlaid input, Error: Couldn't able to convert")

def toDynamicTypeCast(argList):
    pass