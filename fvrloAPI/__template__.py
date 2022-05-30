import sys

class mod_call:
    def __call__(self):
        # code goes here
		# don't forget to add *args if you're using them!

sys.modules[__name__] = mod_call()