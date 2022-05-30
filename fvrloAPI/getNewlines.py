import sys

class mod_call:
    def __call__(self, string, every=64):
        lines = []
        for i in range(0, len(string), every):
            lines.append(string[i:i+every])
        return '\n'.join(lines)

sys.modules[__name__] = mod_call()










