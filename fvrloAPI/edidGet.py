import sys
import winreg

class mod_call:
    def __call__(self):
        # EDID is stored in the registry at:
        #   HKEY_LOCAL_MACHINE
        #       \SYSTEM
        #           \CurrentControlSet
        #               \Enum
        #                   \DISPLAY
        #                       \$NAME
        #                          \$ID
        #                               \Device Parameters
        #   Where:
        #       $NAME = "$1$2"
        #           $1 = ID Manufacturer Name
        #           $2 = ID Product Code
        #       $ID = Unknown (Can be more than one per monitor)
        OpenKey_display = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,r"SYSTEM\CurrentControlSet\Enum\DISPLAY")
        EDID_list = [{"DISPLAY": '',"ID_LIST": []} for x in range(winreg.QueryInfoKey(OpenKey_display)[0])]
        z = 0
        for i in EDID_list:
            i['DISPLAY'] = winreg.EnumKey(OpenKey_display, z)
            idList = i['ID_LIST']
            OpenKey_IDList = winreg.OpenKey(OpenKey_display,i['DISPLAY'])
            for ID in range(winreg.QueryInfoKey(OpenKey_IDList)[0]):
                idList.append(winreg.EnumKey(OpenKey_IDList, ID))
            idTemp = []
            for ID in idList:
                parameters_key = winreg.OpenKey(OpenKey_IDList,r"%s\%s" % (ID, r"Device Parameters"))
                n, v, t = winreg.EnumValue(parameters_key, 0)
                if n == "EDID" and t == winreg.REG_BINARY and v not in idTemp:
                    idTemp.append(v)
                parameters_key.Close()
            i['ID_LIST'] = idTemp
            OpenKey_IDList.Close()
            z = z + 1
        OpenKey_display.Close()
        return EDID_list

sys.modules[__name__] = mod_call()