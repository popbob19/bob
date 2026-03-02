import sys, subprocess,re
packages = ['requests','pywinauto', 'pywin32', 'comtypes', 'pyautogui', 'Pillow', 'opencv-python','pydirectinput']
subprocess.check_call([sys.executable, '-m', 'pip', 'install'] + packages)

import requests,subprocess,time,pyautogui

url="https://releases.morelogin.com/prod/client/win/x64/2.50.1/MoreLogin_window_x64_2.50.1.0.exe"
r= requests.get(url)
open("file.exe", "wb").write(r.content)

subprocess.Popen("file.exe")
time.sleep(30)
pyautogui.screenshot("1.png")
#for x in range(501, 701, 5):
screen_width, screen_height = pyautogui.size()
x = 530
for y in range(0, screen_height, 5):  # Every single pixel from top to bottom
    print(f"Clicking {x},{y}")
    pyautogui.click(x, y)
    time.sleep(3)
    pyautogui.screenshot(f"{x}_{y}.png")
