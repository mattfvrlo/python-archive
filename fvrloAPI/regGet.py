import sys
import winreg

class mod_call:
    def __call__(self):
        KEYLIST = {'CROOT': 'CLASSES_ROOT','CUSER': 'CURRENT_USER','LOCAL': 'LOCAL_MACHINE','USERS': 'USERS','PDATA': 'PERFORMANCE_DATA','CRCFG': 'CURRENT_CONFIG','DDATA': 'DYN_DATA'}
        KEYOUT = [{"name": x,"key": y,"items": [],"done": False} for x,y in KEYLIST.items()]
        for x in KEYOUT:
            KEY_items = []
            if x['done'] == True:
                break
            for i in range(1024):
                if x['name'] == 'CROOT':
                    KEY_items = winreg.EnumKey(eval(f"winreg.HKEY_{x['key']}"), i)
                    continue
                try:
                    KEY_items.append(winreg.EnumKey(eval(f"winreg.HKEY_{x['key']}"), i))
                except WindowsError:
                    break
            x["items"] = KEY_items
            x["done"] = True
        return KEYOUT

sys.modules[__name__] = mod_call()