import sys, subprocess,re,os
packages = ['requests']#,'pywinauto', 'pywin32', 'comtypes', 'pyautogui', 'Pillow', 'opencv-python','pydirectinput']
subprocess.check_call([sys.executable, '-m', 'pip', 'install'] + packages)

import requests,time #,pyautogui

url="https://releases.morelogin.com/prod/client/win/x64/2.50.1/MoreLogin_window_x64_2.50.1.0.exe"
r = requests.get(url)
file_path = os.path.join("D:\\", "file.exe")

with open(file_path, "wb") as f:
    f.write(r.content)

