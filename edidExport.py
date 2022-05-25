import sys
import winreg
import base64
import json
import os
import requests
import settings

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

key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,r"SYSTEM\CurrentControlSet\Enum\DISPLAY")
encode, decode, displayList = [],[],[]

for i in range(1024):
    try:
        displayList.append(winreg.EnumKey(key, i))
    except WindowsError:
        break
displayNum = len(displayList)


for x in displayList:
    IDs = []
    IDs_key = winreg.OpenKey(key, x)
    for i in range(displayNum):
        IDs.append(winreg.EnumKey(IDs_key, i))
        
    for ID in IDs:
        parameters_key = winreg.OpenKey(
            IDs_key,
            r"%s\%s" % (ID, r"Device Parameters")
        )
        try:
            n, v, t = winreg.EnumValue(parameters_key, 0)
            if n == "EDID" and t == winreg.REG_BINARY:
                self.EDIDs.append(v)
        except WindowsError:
            pass
        parameters_key.Close()
    IDs_key.Close()

key.Close()



for edid in edid_list:
    encoded.append(base64.b64encode(edid))
    decode_b.append(edid)
    decode_s.append(str(base64.b64encode(edid), 'utf-8'))        

i = 0
out_en = open("edid_out_en.txt", "w")
out_de = open("edid_out_de.txt", "w")
aio = open("edid_aio.txt", "w")

for x in range(0,19):
    tit = f"\t\t\t\t\t\t      Item #{x}\n"
    eno = f"\t\t\t\t\t\t---     Raw     ---\n\n"
    deo = f"\t\t\t\t\t\t---   Decoded   ---\n\n"
    en = str(decode_s[x])
    de = str(decode_b[x])

    aio.write(f"{tit}{eno}{en}\n\n\n{deo}{de}\n\n\n\n\n\n")

    out_en.write(en + "\n")
    out_de.write(de + "\n")
aio.close()
out_en.close()
out_de.close()
return json.dumps(decode_s)




print('Starting EDID Grabber\n\n')
print('Collecting EDIDs from operating system ...')
grabber = WindowsGrabber()
grabber.grab_EDID()
print('EDID items found: %s\n' % (len(grabber.EDIDs)))

grub = len(grabber.EDIDs)

if grub > 0:
    print('Uploading EDIDs ...')
    #print(grabber.EDIDs)
    uploader = EDIDUploader()
    uploader.upload(grabber.EDIDs)
    print('Succeeded: %s, Failed: %s\n' % (uploader.succeeded, uploader.failed))
else:
    print('No EDIDs to upload.\n')

print('Aborting.')
