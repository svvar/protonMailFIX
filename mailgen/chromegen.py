#! python3
# Michi4
import pyautogui
import time
import random
import webbrowser
import ctypes
import re

kernel32 = ctypes.windll.kernel32
kernel32.GlobalLock.argtypes = [ctypes.c_void_p]
kernel32.GlobalLock.restype = ctypes.c_void_p
kernel32.GlobalUnlock.argtypes = [ctypes.c_void_p]
user32 = ctypes.windll.user32
user32.GetClipboardData.restype = ctypes.c_void_p


def getClip6digit():
    site_text = ""
    if user32.OpenClipboard(None):
        data = user32.GetClipboardData(13)
        site_text = ctypes.wstring_at(kernel32.GlobalLock(data))
        kernel32.GlobalUnlock(data)
        user32.CloseClipboard()

    code = re.findall(r"\d{6}", site_text)[0]
    return code


def getMail():
    site_text = ""
    if user32.OpenClipboard(None):
        data = user32.GetClipboardData(13)
        site_text = ctypes.wstring_at(kernel32.GlobalLock(data))
        kernel32.GlobalUnlock(data)
        user32.CloseClipboard()

    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    email = re.findall(email_pattern, site_text)[0]

    # Add accepted email domains here to work much faster
    if "@dropmail" in email or "@10mail.net" in email or "@emlpro.net" in email or "@emltmp.net" in email \
            or "@minimail" in email or "@flymail" in email:
        return email
    return False


webbrowser.open('https://account.proton.me/signup?plan=free')
time.sleep(6)


def randomize(option, length):
    if length > 0:

        # Options:6Ww$oRvfSVk95tyM  6Ww$oRvfSVk95tyM
        #       -p      for letters, numbers and symbols
        #       -s      for letters and numbers
        #       -l      for letters only
        #       -n      for numbers only
        #       -m      for month selection
        #       -d      for day selection
        #       -y      for year selection

        if option == '-p':
            characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+'
        elif option == '-s':
            characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
        elif option == '-l':
            characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        elif option == '-n':
            characters = '1234567890'
        elif option == '-m':
            characters = 'JFMASOND'

        if option == '-d':
            generated_info = random.randint(1, 28)
        elif option == '-y':
            generated_info = random.randint(1950, 2000)
        else:
            generated_info = ''
            for counter in range(0, length):
                generated_info = generated_info + random.choice(characters)

        return generated_info

    else:
        return 'error'


# Username
username = randomize('-s', 7) + randomize('-s', 7)
pyautogui.typewrite(username + '\t\t\t')
time.sleep(0.2)
print("Username:" + username)

# Password
password = randomize('-p', 14)
pyautogui.typewrite(password + '\t' + password + '\t')
print("Password:" + password)

pyautogui.typewrite('\n')
time.sleep(2)
pyautogui.typewrite('\t\t\t\n')

pyautogui.hotkey('ctrl', 't')

time.sleep(1)
pyautogui.typewrite('https://dropmail.me/uk/\n')
time.sleep(2)

newMail = True
while True:
    if not newMail:
        pyautogui.keyDown('ctrlleft')
        pyautogui.typewrite('r')
        pyautogui.keyUp('ctrlleft')
        time.sleep(3)

    pyautogui.hotkey('ctrlleft', 'a')
    pyautogui.hotkey('ctrlleft', 'c')

    newMail = getMail()
    if newMail:
        print("10 min mail: " + newMail)
        break

pyautogui.hotkey('shiftleft', 'ctrlleft', '\t')

time.sleep(1)
pyautogui.typewrite(newMail)
pyautogui.typewrite('\n')

time.sleep(1)

pyautogui.hotkey('ctrlleft', '\t')

time.sleep(25)

pyautogui.hotkey('ctrlleft', 'a')
pyautogui.hotkey('ctrlleft', 'c')
time.sleep(1)
pyautogui.hotkey('shiftleft', 'ctrlleft', '\t')

pyautogui.typewrite(getClip6digit() + '\n')

time.sleep(8)
pyautogui.typewrite('\n')
time.sleep(2)
pyautogui.typewrite('\t\t\t\t\n')
time.sleep(1)
pyautogui.typewrite('\t\n')

print(username + "@proton.me: " + password)

logfile = open("accLog.txt", "a")
logfile.write(username + "@proton.me:" + password + "\n")
logfile.close()
