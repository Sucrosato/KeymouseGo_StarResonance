import keyboard
import pandas as pd
import pytesseract
import pyautogui
from time import sleep
from datetime import datetime
import cv2
from pathlib import Path
coords = [
    [(521, 432, 262, 33),(659, 372),(540, 344, 85, 25),(601, 204)]
]
reso=0

def get_name():
    screenshot = pyautogui.screenshot(region=coords[reso][0])
    screenshot.save('sc.png')
    screenshot = cv2.imread('sc.png')
    gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

    # 2. 二值化（让黑白对比度极大化）
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

    # 3. 放大图片（Tesseract 识别中文字符时，图片太小识别率会极低）
    # 建议放大到原来的 2-3 倍
    resized = cv2.resize(thresh, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    custom_config = r'-l chi_sim --psm 7'
    d = pytesseract.image_to_string(resized, config=custom_config)
    return d

def get_amount():
    screenshot = pyautogui.screenshot(region=coords[reso][2])
    custom_config = r'--psm 7 -c tessedit_char_whitelist=0123456789+'
    d = pytesseract.image_to_string(screenshot, config=custom_config)
    return d

    

if __name__=='__main__':
    name = get_name().strip()
    print(name)
    start_time = datetime.now().strftime("%Y-%m-%d,%H:%M:%S")
    df = pd.DataFrame(columns=['time', 'amount']).set_index('time')

    while(True):
        if keyboard.is_pressed('pause'):
            print("检测到终止指令，正在保存数据并退出...")
            break
        pyautogui.click(*coords[reso][1])
        sleep(1)
        amount = int(get_amount())
        time = datetime.now().strftime("%Y-%m-%d,%H:%M:%S")
        df.loc[time, 'amount'] = amount
        pyautogui.click(*coords[reso][3])
        sleep(1)
    
    DATA_FILE = "data/monitor/"
    path = Path(DATA_FILE)
    path.mkdir(parents=True, exist_ok=True)
    df.to_csv(DATA_FILE+"test.csv", encoding='utf-8-sig')
