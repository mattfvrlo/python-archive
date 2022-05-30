import os,sys,importlib
__name__= 'fvrloAPI'
__doc__ = 'Saving my fingers by building a library of common codes.'
__all__ = [
    'debug',
    'autoDebug',
    'block',
    'getConcat',
    'getNewlines',
    'regGet',
    'regOut',
    'edidGet',
    'edidOut',
    'listGen',
    'colortest',
]

for pkg in __all__:
    exec(f"from . import {pkg}")

# dependency check for required requirements that I require to be required
os.system('color')                      # require color
fvRequired = ['termcolor','numpy']      # require list
for package in fvRequired:
    try: importlib.import_module(package)
    except ImportError:
        print(f"Missing requirement {x}, autoinstalling...")
        import subprocess
        try: subprocess.check_call([sys.executable, "-m", "pip", "install", x])
        except Exception as e: print(f"Can't install {x}: {e}")
    finally: globals()[package] = importlib.import_module(package)

block = block()

def edidPrint():
    edidOut(edidGet())

def regPrint():
    regOut(regGet())

def colortest():
    irange = list(range(10))
    jrange = list(range(30, 38))
    krange = list(range(40, 48))
    for i,j,k in irange,jrange,krange:
        print("%d;%d;%d: \33[%d;%d;%dm Hello, World! \33[m \n" % (i, j, k, i, j, k,) + "\n")