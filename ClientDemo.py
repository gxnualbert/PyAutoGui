#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:albert.chen
@file: ClientDemo.py
@time: 2017/07/17/17:54
"""

#!usr/bin/env python

#-*- coding:utf-8 _*-
"""
@author:albert.chen
@file: drag.py
@time: 2017/07/17/16:09
"""

import pyautogui
import time
import subprocess
# distance = 200
#
# time.sleep(3)
# while distance > 0:
#     pyautogui.dragRel(distance, 0, duration=0.5)  # move right
#     distance -= 5
#     pyautogui.dragRel(0, distance, duration=0.5)  # move down
#     pyautogui.dragRel(-distance, 0, duration=0.5)  # move left
#     distance -= 5
#     pyautogui.dragRel(0, -distance, duration=0.5)  # move up

# print pyautogui.size()

p=subprocess.Popen("C:\\Program Files (x86)\\Inpor\\4UClient\\FMDesktop\\FastMeeting.exe", shell=True)

time.sleep(2)
pyautogui.click(923, 546)

pyautogui.typewrite('fm01\n',interval=0.1)

time.sleep(2)

pyautogui.typewrite('000000\n')

time.sleep(2)

pyautogui.moveTo(1095, 662)

time.sleep(2)

pyautogui.click()

time.sleep(2)

pyautogui.moveTo(188, 193)

time.sleep(1)

pyautogui.click()




