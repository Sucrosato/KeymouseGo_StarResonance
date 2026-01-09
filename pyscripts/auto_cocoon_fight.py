import pyautogui
from time import sleep

def get_cocoon_marker_pos(delay=0):
    sleep(delay)
    location = pyautogui.locateOnScreen(
                    'data/pics/cocoon_marker.png',
                    region=[63, 40, 240, 240],
                    confidence=0.7,
                    grayscale=True
                )
    point = pyautogui.center(location)
    return [int(point.x), int(point.y)]

def move_to_cocoon(pos):
    offset_x = pos[0] - 138.5
    offset_y = pos[1] - 169
    if offset_x < 0:
        pyautogui.keyDown('a')
        sleep(max(abs(offset_x)/8, 0.5))
        pyautogui.keyUp('a')
    elif offset_x > 0:
        pyautogui.keyDown('d')
        sleep(max(offset_x/8, 0.5))
        pyautogui.keyUp('d')
    sleep(0.5)
    if offset_y < 0:
        pyautogui.keyDown('w')
        sleep(max(abs(offset_y)/8, 0.5))
        pyautogui.keyUp('w')
    elif offset_y > 0:
        pyautogui.keyDown('s')
        sleep(max(offset_y/8, 0.5))
        pyautogui.keyUp('s')

def down():
    pyautogui.keyDown('altleft')
    pyautogui.mouseDown(1280, 0)
    pyautogui.moveTo(1280, 1440)
    pyautogui.mouseUp()
    pyautogui.keyUp('altleft')

def locate(goal, region):
    location = pyautogui.locateOnScreen(
                    'E:/Apps/git_repos/KeymouseGo/dist/plugins/Locate/pics/'+goal+'.png',
                    region=region,
                    confidence=0.8,
                    grayscale=True
                )
    if location:
        return True
    else:
        return False
    
def close_ads():
    while not locate("shezhi", [2440, 130, 94, 117]):
        pyautogui.keyDown('esc')
        sleep(0.1)
        pyautogui.keyUp('esc')
        sleep(1)

def sequence(period_1=2400, period_2=1200):
    close_ads()
    pyautogui.press('esc')
    sleep(1)
    region = [1939, 743, 132, 25]
    while not pyautogui.locateOnScreen(
                    'E:/Apps/git_repos/KeymouseGo/dist/data/pics/jinrunimengzhidi.png',
                    region=region,
                    confidence=0.8,
                    grayscale=True
                ):
        move_to_cocoon(get_cocoon_marker_pos(1))
    sleep(1)
    pyautogui.press('f')
    sleep(1)
    down()
    sleep(1)
    pyautogui.press('h')
    sleep(period_1)
    pyautogui.press('h')
    sleep(period_2)



if __name__ == "__main__":
    sleep(2)
    while True:
        sequence()
