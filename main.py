import pyautogui
import webbrowser
from time import sleep

if __name__ == "__main__":

    url = "https://tinder.com/app/recs"
    webbrowser.open_new_tab(url)
    sleep(5)
    counter = 0
    increment = 2.5
    reload_page_increment = 5
    reload_page = 100
    try:
        while True:
            pyautogui.moveTo(1318,798)
            pyautogui.click()
            print(f'Liked {counter}, {reload_page} ')
            sleep(2.5)
            if reload_page == counter:
                pyautogui.moveTo(254,989)
                pyautogui.click()
                sleep(5)
                reload_page = reload_page + reload_page_increment
                print('Reload')
            counter = counter + increment
    except KeyboardInterrupt:
        print('\n')
    
    # print('Press Ctrl-C to quit.')
    # try:
    #     while True:
    #         x, y = pyautogui.position()
    #         positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
    #         print(positionStr, end='')
    #         print('\b' * len(positionStr), end='', flush=True)
    # except KeyboardInterrupt:
    #     print('\n')

    # term = 'Hola'
    # url = "https://www.google.com.tr/search?q={}".format(term)
    # webbrowser.open_new_tab(url)