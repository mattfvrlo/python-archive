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
from colorama import init,Fore,Back,Style,reinit
for pkg in __all__:
    exec(f"from . import {pkg}")

os.system('color')
init(autoreset=True)
block = block()

cColors = {        # for calling colorama colors
    'Fore.BLACK'   : 'fBlack',
    'Fore.RED'     : 'fRed',
    'Fore.GREEN'   : 'fGreen',
    'Fore.YELLOW'  : 'fYellow',
    'Fore.BLUE'    : 'fBlue',
    'Fore.MAGENTA' : 'fMagenta',
    'Fore.CYAN'    : 'fCyan',
    'Fore.WHITE'   : 'fWhite',
#
    'Style.DIM'    : 'sDim',
    'Style.NORMAL' : 'sNormal',
    'Style.BRIGHT' : 'sBright',
#
    'Back.BLACK'   : 'bBlack',
    'Back.RED'     : 'bRed',
    'Back.GREEN'   : 'bGreen',
    'Back.YELLOW'  : 'bYellow',
    'Back.BLUE'    : 'bBlue',
    'Back.MAGENTA' : 'bMagenta',
    'Back.CYAN'    : 'bCyan',
    'Back.WHITE'   : 'bWhite',
}
cColors_list = list(cColors.keys())
for key in cColors.keys(): exec(f'{cColors.get(key)} = {key}')
def edidPrint(): edidOut(edidGet())
def regPrint(): regOut(regGet())
def colortest():
    w = int(os.get_terminal_size()[0] / 4)
    empty4 = f"{bBlack}{fWhite}{'':<{w}}"
    # Header
    print(f"{'':<{w}}{'Foreground':<{w}}{'Background':<{w}}{empty4}")
    # Black
    combo = ((fBlack + bWhite),(fWhite + bBlack))
    print(f"{'BLACK':<{w}}{combo[0]}{'TEXT':<{w}}{combo[1]}{'TEXT':<{w}}{empty4}")
    # Red
    combo = ((fRed + bBlack),(fBlack + bRed))
    print(f"{'RED':<{w}}{combo[0]}{'TEXT':<{w}}{combo[1]}{'TEXT':<{w}}{empty4}")
    # Green
    combo = ((fGreen + bBlack),(fBlack + bGreen))
    print(f"{'GREEN':<{w}}{combo[0]}{'TEXT':<{w}}{combo[1]}{'TEXT':<{w}}{empty4}")
    # Yellow
    combo = ((fYellow + bBlack),(fBlack + bYellow))
    print(f"{'YELLOW':<{w}}{combo[0]}{'TEXT':<{w}}{combo[1]}{'TEXT':<{w}}{empty4}")
    # Blue
    combo = ((fBlue + bBlack),(fBlack + bGreen))
    print(f"{'BLUE':<{w}}{combo[0]}{'TEXT':<{w}}{combo[1]}{'TEXT':<{w}}{empty4}")
    # Magenta
    combo = ((fMagenta + bBlack),(fBlack + bMagenta))
    print(f"{'MAGENTA':<{w}}{combo[0]}{'TEXT':<{w}}{combo[1]}{'TEXT':<{w}}{empty4}")
    # Cyan
    combo = ((fCyan + bBlack),(fBlack + bCyan))
    print(f"{'CYAN':<{w}}{combo[0]}{'TEXT':<{w}}{combo[1]}{'TEXT':<{w}}{empty4}")
    # White
    combo = ((fWhite + bBlack),(fBlack + bWhite))
    print(f"{'WHITE':<{w}}{combo[0]}{'TEXT':<{w}}{combo[1]}{'TEXT':<{w}}{empty4}")
    print('')
    print(f"{'DIM:':<{w}}{sDim}{'TEXT':<{w}}{sNormal}{'BRIGHT:':<{w}}{sBright}{'TEXT':<{w}}")
    print('')
    print(f'block, {block}, block')

def colorama():
    # Official Colorama Demo
    spacer = 9
    sSpacer = 8
    styleCycle = f"{sDim}x{block}X{sNormal}x{block}X{sBright}x{block}X"
    process = f"{fRed}{styleCycle}{fGreen}{styleCycle}{fYellow}{styleCycle}{fBlue}{styleCycle}{fMagenta}{styleCycle}{fCyan}{styleCycle}{fWhite}{styleCycle}"
    print(f"{'':^{sSpacer}}{fRed}{'red':^{spacer}}{fGreen}{'green':^{spacer}}{fYellow}{'yellow':^{spacer}}{fBlue}{'blue':^{spacer}}{fMagenta}{'magent':^{spacer}}{fCyan}{'cyan':^{spacer}}{fWhite}{'white':^{spacer}}")
    print(bBlack   + fWhite + f"{'Black':<{sSpacer}}" + process)
    print(bRed     + fWhite + f"{'Red':<{sSpacer}}" + process)
    print(bGreen   + fWhite + f"{'Green':<{sSpacer}}" + process)
    print(bYellow  + fWhite + f"{'Yellow':<{sSpacer}}" + process)
    print(bBlue    + fWhite + f"{'Blue':<{sSpacer}}" + process)
    print(bMagenta + fWhite + f"{'Magenta':<{sSpacer}}" + process)
    print(bCyan    + fWhite + f"{'Cyan':<{sSpacer}}" + process)
    print(bWhite   + fWhite + f"{'White':<{sSpacer}}" + process)