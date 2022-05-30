import sys
from . import debug

class mod_call:
    def __call__(self, *args):
        for item in args:
            debug('Display:',(item[0])['DISPLAY'],10,40)
            ID_LIST = (item[0])['ID_LIST']
            print(f'Stored EDIDs: {len(ID_LIST)}')
            EDID_count = 1
            for data in ID_LIST:
                print(f"EDID #{EDID_count}:")
                EDID_count = EDID_count + 1
        
                byteData = data         # byteData is format:bytes, 128 long
                byteList = []           # byteList is a list of bytes, 128 long
                for i in range(0, len(byteData), 1):
                    byteList.append(byteData[i:i+1])
        
                hexData = data.hex()    # hexData is format:string, 256 long
                hexList = []            # hexList is a list of hex as string, 128 long
                for i in range(0, len(hexData), 2):
                    hexList.append(hexData[i:i+2])

                edid_Header = hexList[0:7]
                edid_MFG = byteData[8:9]
                print(edid_Header)
                print(edid_MFG)
                print(byteData[8])
                print(byteData[9])

sys.modules[__name__] = mod_call()