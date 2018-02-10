#####################################################################
#                                                                   #
#        This program will automatically run the run dialog and     #
#           check if any undocumented computers are online          #
#                                                                   #
#####################################################################

import pyautogui

# This is a template for our workstation names
cpuName = '\\\\wpsws%d\\c$'

# Open 'run'
pyautogui.hotkey('winleft', 'r')
# Type the intended PC names
pyautogui.typewrite('\\\\OXOFFICEADMIN\\c$')
# Click okay
pyautogui.click(172, 997)

pyautogui.hotkey('winleft', 'r')
pyautogui.typewrite('\\\\TONYM-LT\\c$')
pyautogui.click(172, 997)

pyautogui.hotkey('winleft', 'r')
pyautogui.typewrite('\\\\WPS-SAFE\\c$')
pyautogui.click(172, 997)

pyautogui.hotkey('winleft', 'r')
pyautogui.typewrite(cpuName % (15))
pyautogui.click(172, 997)

pyautogui.hotkey('winleft', 'r')
pyautogui.typewrite(cpuName % (155))
pyautogui.click(172, 997)

pyautogui.hotkey('winleft', 'r')
pyautogui.typewrite(cpuName % (17))
pyautogui.click(172, 997)

pyautogui.hotkey('winleft', 'r')
pyautogui.typewrite(cpuName % (41))
pyautogui.click(172, 997)

pyautogui.hotkey('winleft', 'r')
pyautogui.typewrite(cpuName % (59))
pyautogui.click(172, 997)

pyautogui.hotkey('winleft', 'r')
pyautogui.typewrite(cpuName % (60))
pyautogui.click(172, 997)

pyautogui.hotkey('winleft', 'r')
pyautogui.typewrite(cpuName % (10))
pyautogui.click(172, 997)

pyautogui.hotkey('winleft', 'r')
pyautogui.typewrite(cpuName % (13))
pyautogui.click(172, 997)

pyautogui.hotkey('winleft', 'r')
pyautogui.typewrite(cpuName % (14))
pyautogui.click(172, 997)

pyautogui.hotkey('winleft', 'r')
pyautogui.typewrite(cpuName % (19))
pyautogui.click(172, 997)

pyautogui.hotkey('winleft', 'r')
pyautogui.typewrite(cpuName % (25))
pyautogui.click(172, 997)

pyautogui.hotkey('winleft', 'r')
pyautogui.typewrite(cpuName % (28))
pyautogui.click(172, 997)

pyautogui.hotkey('winleft', 'r')
pyautogui.typewrite(cpuName % (29))
pyautogui.click(172, 997)

pyautogui.hotkey('winleft', 'r')
pyautogui.typewrite(cpuName % (61))
pyautogui.click(172, 997)

pyautogui.hotkey('winleft', 'r')
pyautogui.typewrite(cpuName % (73))
pyautogui.click(172, 997)

pyautogui.hotkey('winleft', 'r')
pyautogui.typewrite('\\\\BARBARAK_LATITU\\c$')
pyautogui.click(172, 997)

pyautogui.hotkey('winleft', 'r')
pyautogui.typewrite('\\\\RENATO-LAPTOP\\c$')
pyautogui.click(172, 997)

pyautogui.hotkey('winleft', 'r')
pyautogui.typewrite(cpuName % (26))
pyautogui.click(172, 997)

pyautogui.hotkey('winleft', 'r')
pyautogui.typewrite(cpuName % (36))
pyautogui.click(172, 997)

pyautogui.hotkey('winleft', 'r')
pyautogui.typewrite(cpuName % (37))
pyautogui.click(172, 997)

pyautogui.hotkey('winleft', 'r')
pyautogui.typewrite(cpuName % (38))
pyautogui.click(172, 997)

pyautogui.hotkey('winleft', 'r')
pyautogui.typewrite(cpuName % (39))
pyautogui.click(172, 997)

pyautogui.hotkey('winleft', 'r')
pyautogui.typewrite(cpuName % (46))
pyautogui.click(172, 997)

pyautogui.hotkey('winleft', 'r')
pyautogui.typewrite(cpuName % (69))
pyautogui.click(172, 997)

pyautogui.hotkey('winleft', 'r')
pyautogui.typewrite('\\\\wpsws01\\c$')
pyautogui.click(172, 997)

pyautogui.hotkey('winleft', 'r')
pyautogui.typewrite(cpuName % (146)) #THIS IS MY PC, DON'T DELETE IT
pyautogui.click(172, 997)

pyautogui.hotkey('winleft', 'r')
pyautogui.typewrite(cpuName % (20))
pyautogui.click(172, 997)

pyautogui.hotkey('winleft', 'r')
pyautogui.typewrite(cpuName % (47))
pyautogui.click(172, 997)

pyautogui.hotkey('winleft', 'r')
pyautogui.typewrite(cpuName % (48))
pyautogui.click(172, 997)

pyautogui.hotkey('winleft', 'r')
pyautogui.typewrite(cpuName % (49))
pyautogui.click(172, 997)

pyautogui.hotkey('winleft', 'r')
pyautogui.typewrite(cpuName % (52))
pyautogui.click(172, 997)
