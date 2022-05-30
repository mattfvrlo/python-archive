import sys

class mod_call:
    def __call__(self):
        import os
        if 'UTF' in os.getenv('LC_CTYPE'):
            return "█"
        else:
            return "X"

sys.modules[__name__] = mod_call()