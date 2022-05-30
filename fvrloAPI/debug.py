import sys
import os

class mod_call:
    def __call__(self, *args):
        help_prompt = "---- HELP ----\n" \
"There are three positions for variables, D1, D2, and LEN.\n" \
"If a position is left empty, it's set to empty (D2) or set to default (LEN).\n" \
"To make a single item on the right, set D1=\'ind\' and your data to D2.\n\n" \
"Character space per item presets for LEN ('mid' by default):\n" \
"'short' (15), 'mid' (20), and 'long' (30)"
        if 'UTF' in os.getenv('LC_CTYPE'):
            block = "█"
        else:
            block = "X"
        try: D1 = args[0]
        except: D1 = ''
        try: D2 = args[1]
        except: D2 = ''
        try: LEN = args[2]
        except: LEN = 'mid'
    
        if D1 == 'help':
            print(help_prompt)
            return
        elif D1 == 'fill':
            print("--------------------------------------------")
            return
        elif 'ind' in D1:
            D2 = D1
            D1 = ''
    
        if LEN == 'short':
            LEN = 15
        elif LEN == 'mid':
            LEN = 20
        elif LEN == 'long':
            LEN = 30
        L2 = LEN * 2

        if LEN <= len(D1):
            print(f"LEN TOO SHORT: {LEN} VS {len(D1)}")
            print(f"--{''.join([char*LEN for char in block])}")
            print(f"-'{D1}'\n")
        print((f"{{:<{LEN}}}{{:<{L2}}}").format(D1, D2))

sys.modules[__name__] = mod_call()