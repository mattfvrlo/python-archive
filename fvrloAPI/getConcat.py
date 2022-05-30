import sys

class mod_call:
    def __call__(self, *args):
        if type(args) == tuple:
            listData = list(args)
        else:
            listData = args
        if listData[-1] == 'nospace':
            src = ''
            for i in range(len(listData) - 1):
                infor = str(listData[i])
                src = src + infor
        else:
            src = str(listData[0])
            for i in range(1,len(listData)):
                infor = str(listData[i])
                src = src + ' ' + infor
        return src

sys.modules[__name__] = mod_call()