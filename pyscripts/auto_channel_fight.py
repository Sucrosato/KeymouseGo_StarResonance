from time import sleep
import pynput
from pynput.mouse import Button, Controller
import pyautogui
mouse = Controller()
def left():
    pyautogui.keyDown('altleft')
    pyautogui.mouseDown(1280, 720)
    pyautogui.moveTo(700, 700)
    pyautogui.mouseUp()
    pyautogui.keyUp('altleft')

def down():
    pyautogui.keyDown('altleft')
    pyautogui.mouseDown(1280, 720)
    pyautogui.moveTo(1280, 1440)
    pyautogui.mouseUp()
    pyautogui.keyUp('altleft')


def v1(times=80, period=10, channel_buffer=10, max_channel=25, start_channel=1):
    for i in range(times):
        channel = (i + start_channel - 1) % max_channel + 1
        mouse.click(Button.x1, 1)
        sleep(1)
        pyautogui.click(1991, 1336)
        sleep(1)
        pyautogui.write(str(channel))
        sleep(1)
        pyautogui.click(2375, 1343)
        sleep(1)
        pyautogui.press('esc')
        sleep(channel_buffer)
        down()
        pyautogui.press('H')
        # pyautogui.mouseDown(1280, 720)
        sleep(period)
        # pyautogui.mouseUp(1280, 720)

if __name__ == '__main__':
    sleep(3)
    v1(start_channel=21, period=15, times=65, max_channel=80, channel_buffer=15)