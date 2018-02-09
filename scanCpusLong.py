#####################################################################
#                                                                   #
#        This program will automatically run 'run' and check        #
#             if any undocumented computers are online              #
#                                                                   #
#             THIS VERSION WILL TAKE ABOUT 17 MINUTES               #
#          DO NOT USE UNLESS YOU ARE LEAVING THE PC ALONE           #
#                                                                   #
#####################################################################

# This tells the interpreter to use Python 3
#!python3

import pyautogui
import time

# This is a template for our workstation names
cpuName = '\\\\wpsws{}\\c$'

# Open 'run'
pyautogui.hotkey('winleft', 'r')
# Type the intended PC names
pyautogui.typewrite('\\\\OXOFFICEADMIN\\c$')
# Click okay
pyautogui.click(172, 997)
# Wait 30 seconds for the folder to be found/not found
time.sleep(30)

pyautogui.hotkey('winleft', 'r')
pyautogui.typewrite('\\\\TONYM-LT\\c$')
pyautogui.click(172, 997)
time.sleep(30)

pyautogui.hotkey('winleft', 'r')
pyautogui.typewrite('\\\\WPS-SAFE\\c$')
pyautogui.click(172, 997)
time.sleep(30)

pyautogui.hotkey('winleft', 'r')
pyautogui.typewrite(cpuName.format(15))
pyautogui.click(172, 997)
time.sleep(30)

pyautogui.hotkey('winleft', 'r')
pyautogui.typewrite(cpuName.format(155))
pyautogui.click(172, 997)
time.sleep(30)

pyautogui.hotkey('winleft', 'r')
pyautogui.typewrite(cpuName.format(17))
pyautogui.click(172, 997)
time.sleep(30)

pyautogui.hotkey('winleft', 'r')
pyautogui.typewrite(cpuName.format(41))
pyautogui.click(172, 997)
time.sleep(30)

pyautogui.hotkey('winleft', 'r')
pyautogui.typewrite(cpuName.format(59))
pyautogui.click(172, 997)
time.sleep(30)

pyautogui.hotkey('winleft', 'r')
pyautogui.typewrite(cpuName.format(60))
pyautogui.click(172, 997)
time.sleep(30)

pyautogui.hotkey('winleft', 'r')
pyautogui.typewrite(cpuName.format(10))
pyautogui.click(172, 997)
time.sleep(30)

pyautogui.hotkey('winleft', 'r')
pyautogui.typewrite(cpuName.format(13))
pyautogui.click(172, 997)
time.sleep(30)

pyautogui.hotkey('winleft', 'r')
pyautogui.typewrite(cpuName.format(14))
pyautogui.click(172, 997)
time.sleep(30)

pyautogui.hotkey('winleft', 'r')
pyautogui.typewrite(cpuName.format(19))
pyautogui.click(172, 997)
time.sleep(30)

pyautogui.hotkey('winleft', 'r')
pyautogui.typewrite(cpuName.format(25))
pyautogui.click(172, 997)
time.sleep(30)

pyautogui.hotkey('winleft', 'r')
pyautogui.typewrite(cpuName.format(28))
pyautogui.click(172, 997)
time.sleep(30)

pyautogui.hotkey('winleft', 'r')
pyautogui.typewrite(cpuName.format(29))
pyautogui.click(172, 997)
time.sleep(30)

pyautogui.hotkey('winleft', 'r')
pyautogui.typewrite(cpuName.format(61))
pyautogui.click(172, 997)
time.sleep(30)

pyautogui.hotkey('winleft', 'r')
pyautogui.typewrite(cpuName.format(73))
pyautogui.click(172, 997)
time.sleep(30)

pyautogui.hotkey('winleft', 'r')
pyautogui.typewrite('\\\\BARBARAK_LATITU\\c$')
pyautogui.click(172, 997)
time.sleep(30)

pyautogui.hotkey('winleft', 'r')
pyautogui.typewrite('\\\\RENATO-LAPTOP\\c$')
pyautogui.click(172, 997)
time.sleep(30)

pyautogui.hotkey('winleft', 'r')
pyautogui.typewrite(cpuName.format(26))
pyautogui.click(172, 997)
time.sleep(30)

pyautogui.hotkey('winleft', 'r')
pyautogui.typewrite(cpuName.format(36))
pyautogui.click(172, 997)
time.sleep(30)

pyautogui.hotkey('winleft', 'r')
pyautogui.typewrite(cpuName.format(37))
pyautogui.click(172, 997)
time.sleep(30)

pyautogui.hotkey('winleft', 'r')
pyautogui.typewrite(cpuName.format(38))
pyautogui.click(172, 997)
time.sleep(30)

pyautogui.hotkey('winleft', 'r')
pyautogui.typewrite(cpuName.format(39))
pyautogui.click(172, 997)
time.sleep(30)

pyautogui.hotkey('winleft', 'r')
pyautogui.typewrite(cpuName.format(46))
pyautogui.click(172, 997)
time.sleep(30)

pyautogui.hotkey('winleft', 'r')
pyautogui.typewrite(cpuName.format(69))
pyautogui.click(172, 997)
time.sleep(30)

pyautogui.hotkey('winleft', 'r')
pyautogui.typewrite('\\\\wpsws01\\c$')
pyautogui.click(172, 997)
time.sleep(30)

pyautogui.hotkey('winleft', 'r')
pyautogui.typewrite(cpuName.format(146)) #THIS IS MY PC, DON'T DELETE IT
pyautogui.click(172, 997)
time.sleep(30)

pyautogui.hotkey('winleft', 'r')
pyautogui.typewrite(cpuName.format(20))
pyautogui.click(172, 997)
time.sleep(30)

pyautogui.hotkey('winleft', 'r')
pyautogui.typewrite(cpuName.format(47))
pyautogui.click(172, 997)
time.sleep(30)

pyautogui.hotkey('winleft', 'r')
pyautogui.typewrite(cpuName.format(48))
pyautogui.click(172, 997)
time.sleep(30)

pyautogui.hotkey('winleft', 'r')
pyautogui.typewrite(cpuName.format(49))
pyautogui.click(172, 997)
time.sleep(30)

pyautogui.hotkey('winleft', 'r')
pyautogui.typewrite(cpuName.format(52))
pyautogui.click(172, 997)
time.sleep(30)
