import sys, subprocess,re,os
packages = ['requests','pywinauto', 'pywin32', 'comtypes', 'pyautogui', 'Pillow', 'opencv-python','pydirectinput']
subprocess.check_call([sys.executable, '-m', 'pip', 'install'] + packages)

import requests,time ,pyautogui

url="https://releases.morelogin.com/prod/client/win/x64/2.50.2/MoreLogin_window_x64_2.50.2.0_AAA4NRhdrXcILb1MmLb3QFuQ.exe"
r = requests.get(url)
file_path = os.path.join("D:\\", "file.exe")
#file_path ="file.exe"
with open(file_path, "wb") as f:
    f.write(r.content)

# subprocess.Popen("file.exe")
# time.sleep(30)
# pyautogui.screenshot("1.png")
# x = 510
# for y in range(419, 719, 5):  # Top (219) to Bottom (419), positive step
#     print(f"Clicking {x},{y}")
#     pyautogui.click(x, y)
#     time.sleep(3)
#     pyautogui.screenshot(f"{x}_{y}.png")
