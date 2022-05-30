import sys

class mod_call:
    def __call__(self,filler,y):
        return [filler for x in range(y)]

sys.modules[__name__] = mod_call()