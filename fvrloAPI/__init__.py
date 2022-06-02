__name__= 'fvrloAPI'
__doc__ = 'Saving my fingers by building a library of common codes.'
__all__ = [
    'debug',
    'autoDebug',
    'block',
    'getConcat',
    'getNewlines',
    'regGet',
    'regOut',
    'edidGet',
    'edidOut',
    'listGen',
    'colortest',
]
import os
import sys
import subprocess
for pkg in __all__:
    exec(f"from . import {pkg}")


# enablers section
# (basic things that need to be declared/done on import for it all to work)

#os.system('printf ""')  #doing this enables truecolor somehow? hwat
block = block()
def edidPrint(): edidOut(edidGet())
def regPrint(): regOut(regGet())






# define colorings
def color(fg=0,bg=0):
    def hexr(r,g,b):
        return str('#' + format(r, '02x') + format(g, '02x') + format(b, '02x'))
    def spef(col,fgbg):
        if fgbg == 'fg':
            coron = 3
        elif fgbg == 'bg':
            coron = 4
        if type(col) == tuple:
            col = hexr(col[0],col[1],col[2])
        col = col.replace('#','')
        pixels,dPix = [(col[0] + col[1]),(col[2] + col[3]),(col[4] + col[5])],[]
        for x in pixels: dPix.append(str(int(x,16)))
        return f"\033[{coron}8;2;{dPix[0]};{dPix[1]};{dPix[2]}m"
    if bg != 'fg':
        if bg != 'bg':
            out = spef(fg,'fg') + spef(bg,'bg')
    if bg == 'fg': out = spef(fg,'fg')
    if bg == 'bg': out = spef(fg,'bg')
    if bg == 'hex': out = hexr(fg[0],fg[1],fg[2])
    return out

cBold = '\033[1m'
cDim = '\033[2m'
cUnderline = '\033[4m'
cInvert = '\033[7m'
cRst = '\033[0m'
cRstn = '\033[0m\n'




def bashDo(command):
    subprocess.run(str(command))

def bashPrint(args):
    basher = f"echo \"{str(args)}\""
    bashDo(basher)

def bashPrintn(args):
    basher = f"echo -ne \"{str(args)}\""
    bashDo(basher)



def trutest():
    print(cRst)
    print("Both hex:   " + color('#abcdef','#123456') + 'XXXX' + '\033[0m')
    print("Both tuple: " + color((0,0,0),(255,255,255)) + 'XXXX' + '\033[0m')
    print("FG Set:     " + color('#887766','fg') + 'XXXX' + '\033[0m')
    print("BG Set:     " + color('#887766','bg') + 'XXXX' + '\033[0m')
    print(cBold + 'Bold-ified!' + cRst)
    print(cDim + 'Dimmed!' + cRst)
    print(cUnderline + 'Underlined!' + cRst)
    print(cInvert + 'Inverted!' + cRst)
    
    
    
def trutest2():
    txt,dob1,dob2 = "Bongos",255,0
    #print("{}{}{}".format(color((dob1,dob2,dob2),(0,0,0)),txt,cRst))
    #print("{}{}{}".format(color((dob2,dob1,dob2),(0,0,0)),txt,cRst))
    #print("{}{}{}".format(color((dob2,dob2,dob1),(0,0,0)),txt,cRst))
    
    
    
    listout = []
    for x in range(255):
        #print(f"\033[38;2;{x};{x};{x}mX")
        print(f"\x1b[38;2;{x};{x};{x}mX")
        #bashPrint(f"printf '\x1b[38;2;%s;%s;%smX' ${x} ${x} ${x}")
    
    print('\n')
    print('+')
    print('+')
    bashPrint(f"Both hex:   {color('#abcdef','#123456')}XXXX{cRstn}")
    bashPrint('donkahonka\n')
    
    xpr = ''
    ranger = 32
    ranger2 = 8
    '''
    for x in range(ranger):
        for y in range(ranger):
            for z in range(ranger):
                xprc = format(x*ranger2, '02x') + format(y*ranger2, '02x') + format(z*ranger2, '02x')
                xpr = xpr + color(str(xprc),'bg') + '.'
    getNewlines(xpr,80)
    bashPrint(xpr + cRst)
    '''
    xpr = ''
    for x in range(256):
        xpr = xpr + f"\033[48;2;{x};{x};{x}m" + 'x'
    getNewlines(xpr,80)
    bashPrint(xpr + '\n')
    
    
    
			
			
    
    
    for x in range(255):
        subprocess.run(f"echo -ne \"\033[38;2;${x};${x};${x}m{x}\"")