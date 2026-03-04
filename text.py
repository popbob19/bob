import sys, subprocess,re,os
packages = ['requests','pywinauto', 'pywin32', 'comtypes', 'pyautogui', 'Pillow', 'opencv-python','pydirectinput']
subprocess.check_call([sys.executable, '-m', 'pip', 'install'] + packages)

import requests,time ,pyautogui

url="https://releases.morelogin.com/prod/client/win/x64/2.50.2/MoreLogin_window_x64_2.50.2.0_AAA4NRhdrXcILb1MmLb3QFuQ.exe"
r = requests.get(url)
file_path = os.path.join("D:\\", "file.exe")
file_path ="file.exe"
with open(file_path, "wb") as f:
    f.write(r.content)

subprocess.Popen("file.exe")
time.sleep(30)
pyautogui.screenshot("1.png")
pyautogui.click(510, 494)
pyautogui.click(510, 499)
pyautogui.screenshot("2.png")
