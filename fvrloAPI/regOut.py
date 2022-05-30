import sys
from . import debug

class mod_call:
    def __call__(self, *args):
        for z in args[0]:
            debug('fill')
            if type(z['items']) == str:
                debug(f"Name: {z['name']}",f"Count: 1")
                debug('',z['items'],4,20)
            elif type(z['items']) == list:
                debug(f"Name: {z['name']}",f"Count: {len(z['items'])}")
                for y in range(len(z['items'])):
                    debug('',(z['items'])[y],4,20)
            if z['name'] == 'DDATA':
                debug('fill')

sys.modules[__name__] = mod_call()