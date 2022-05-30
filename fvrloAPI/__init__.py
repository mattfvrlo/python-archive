from . import debug
from . import block

from . import getConcat
from . import getNewlines

from . import edidGet
from . import edidOut

from . import regGet
from . import regOut

def edidPrint():
    edidOut(edidGet())

def regPrint():
    regOut(regGet())

__all__ = [
    'debug',
    'block',
    'getConcat',
    'getNewlines',
    'regGet',
    'regOut',
    'edidGet',
    'edidOut',
]
__name__= 'fvrloAPI'
__doc__ = 'Saving my fingers by building a library of common codes.\n\
List of commands:\n\
debug\n\
block\n\
getConcat\n\
getNewlines\n\
\n\
edidPrint\n\
edidGet\n\
\n\
regPrint\n\
regGet\n\
'