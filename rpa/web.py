import pyautogui
from dotenv import load_dotenv
from time import sleep
import webbrowser
import os

load_dotenv()

def timer():
    sleep(int(os.getenv('timer')))

def open_url(site, new):
    pyautogui.hotkey('ctrlleft', 'f4')
    webbrowser.open_new_tab(os.getenv(site))
    timer()

def passport():
    pyautogui.moveTo(int(os.getenv('passport_x')),int(os.getenv('passport_y')))
    pyautogui.click()
    pyautogui.click()

def likeable():
    counter = 0.0
    increment = float(os.getenv('increment'))
    reload_page = float(os.getenv('reload_page'))
    try:
        while True:
            pyautogui.moveTo(int(os.getenv('like_x')),int(os.getenv('like_y')))
            pyautogui.click()
            print(f'Liked {counter}, {reload_page} ')
            sleep(1)
            if reload_page == counter/2:
                pyautogui.moveTo(int(os.getenv('reload_x')),int(os.getenv('reload_y')))
                pyautogui.click()
                timer()
                break
            counter = counter + increment
    except KeyboardInterrupt:
        print('\n')