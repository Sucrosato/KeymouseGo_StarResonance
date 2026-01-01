import pyautogui
from time import sleep
import pytesseract
from pynput.mouse import Button, Controller

mouse = Controller()

def acirc():
    period = 1.2
    pyautogui.press('Q')
    sleep(1.2)
    pyautogui.mouseDown()
    sleep(period-1)
    pyautogui.mouseUp()
    sleep(1)
    pyautogui.mouseDown()
    sleep(period-1)
    pyautogui.mouseUp()
    sleep(1)
    pyautogui.mouseDown()
    sleep(period-1)
    pyautogui.mouseUp()
    sleep(1)

def locate():

    goal = 'ice'
    region = (995, 109, 26, 29)
    try:
        location = pyautogui.locateOnScreen(
                        'E:/Apps/git_repos/KeymouseGo/dist/plugins/Locate/pics/'+goal+'.png',
                        region=region,
                        confidence=0.8,
                        grayscale=True
                    )
        return True
    except:
        return False

def fight():
    pyautogui.press('F')
    sleep(1)
    pyautogui.mouseUp()
    sleep(1)
    pyautogui.mouseDown()
    sleep(3)
    while(locate()):
        # sleep(0.1)
        acirc()

def get_cur_channel():
    region = (253, 315, 27, 22)
    custom_config = r'--oem 3 --psm 7 -c tessedit_char_whitelist=0123456789'
    img = pyautogui.screenshot(region=region)
    channel = pytesseract.image_to_string(img, config=custom_config)
    return channel

def switch(cur_chan, reverse=False):
    max_channel = 80
    if reverse:
        cur_chan -= 1
        if cur_chan == 0:
            cur_chan = max_channel
    else:
        cur_chan += 1
        if cur_chan == max_channel:
            cur_chan = 1

    mouse.click(Button.x1, 1)
    sleep(1)
    pyautogui.click(1991, 1336)
    pyautogui.click(1991, 1336)
    sleep(1)
    pyautogui.write(str(cur_chan))
    sleep(1)
    pyautogui.click(2375, 1343)
    sleep(15)

    return cur_chan

if __name__=='__main__':
    pyautogui.FAILSAFE = True 
    reverse = False
    sleep(2)
    cur_chan = 39
    print(cur_chan)
    while(True):
        fight()
        cur_chan = switch(cur_chan, reverse)
