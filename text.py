import sys, subprocess,re
packages = ['requests','pywinauto', 'pywin32', 'comtypes', 'pyautogui', 'Pillow', 'opencv-python','pydirectinput']
subprocess.check_call([sys.executable, '-m', 'pip', 'install'] + packages)

import requests,subprocess,time,pyautogui

url="https://releases.morelogin.com/prod/client/win/x64/2.50.1/MoreLogin_window_x64_2.50.1.0.exe"
r= requests.get(url)
open("file.exe", "wb").write(r.content)

subprocess.Popen("file.exe")
time.sleep(20)

loc = pyautogui.locateOnScreen("button.png", confidence=0.8)
pyautogui.click(loc)
