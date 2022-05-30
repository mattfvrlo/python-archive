import sys

class mod_call:
    def __call__(self,item):
        from . import debug
        
        inType = type(item)
        
        strs = [str]
        numeric = [int,float,complex]
        sequence = [list, tuple, range]
        dicts = [dict]
        sets = [set,frozenset]
        bools = [bool]
        binaries = [bytes, bytearray, memoryview]
        NoneTypes = [None]
        
        if inType in strs:
            debug('Text:',item)
        elif inType in numeric:
            debug('Number:',item)
        elif inType in sequence:
            if inType is list:
                debug('Type:','List')
                debug('Length:',len(item))
                if len(item) == 1:
                    debug('int','Inner Item')
                    debug('Type:',str(type(item[0])))
                else:
                    debug('Contents:',type(item[0]))
                    debug('')
                    debug('int','Values')
                    for x in item:
                        debug('int',str(x))
                    debug('')
            elif inType is tuple:
                debug('Type:','Tuple')
                debug('Length:',len(item))
                if len(item) == 1:
                    debug('int','Inner Item')
                    debug('Type:',str(type(item[0])))
                else:
                    debug('Contents:',type(item[0]))
                    debug('')
                    debug('int','Values')
                    for x in item:
                        debug('int',str(x))
                    debug('')
            elif inType is range:
                import numpy as np
                debug('Type:','Range')
                debug('')
                debug('First:',item[0])
                debug('Last:',item[-1])
                debug('')
                debug('Length:',len(item))
        elif inType in dicts:
            debug('Type:','Dictionary')
            debug('Length:',len(item))
            debug('')
            debug('int','Values')
            for x in item.keys():
                debug('Key:',x)
                debug('Value:',str(item.get(x)))
                debug('')
        elif inType in sets:
            debug('Type:','Set')
            debug('int','Values')
            for x in item:
                debug('int',str(x))
        elif inType in bools:
            debug('Type:','Boolean')
            if item == True:
                debug('Value:','True')
            else:
                debug('Value:','False')
        elif inType in binaries:
            print()
        elif inType in NoneTypes:
            print()
# eof
sys.modules[__name__] = mod_call()