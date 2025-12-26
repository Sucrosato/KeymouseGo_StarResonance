import pyautogui
import pytesseract
import pandas as pd
from datetime import datetime
import os
import time

def ocr_num(region):
    
    custom_config = r'--oem 3 --psm 7 -c tessedit_char_whitelist=0123456789,'
    
    filename = 'data/screenshot.png'
    screenshot = pyautogui.screenshot(region=region)
    screenshot.save(filename)
    result = pytesseract.image_to_string(screenshot, config=custom_config)
    result = result.replace(',', '').replace('\n', '')
    
    return result

def get_id_balance():
    region_id = (650, 1362, 108, 27)
    balance_id = (1917, 52, 154, 33)
    click_pos = (2060, 330)

    id = ocr_num(region_id)
    pyautogui.click(click_pos[0], click_pos[1])
    time.sleep(1)
    balance = int(ocr_num(balance_id))
    pyautogui.press('esc')
    return id, balance

def update_daily_report():
    DATA_FILE = "data/daily_balance_report.csv"
    """
    更新报表：行索引为日期，列名为账号ID
    """
    account_id, balance = get_id_balance()

    today_str = datetime.now().strftime("%Y-%m-%d")
    
    # 1. 读取现有数据
    if os.path.exists(DATA_FILE):
        # 将日期列设为索引，方便定位
        df = pd.read_csv(DATA_FILE, index_col='date')
    else:
        # 如果文件不存在，创建一个空的 DataFrame
        df = pd.DataFrame(columns=['date']).set_index('date')

    # 2. 转换数据类型（确保余额是数字，日期是字符串）
    # 如果该账号（列）还没出现过，Pandas 会自动增加这一列
    if account_id not in df.columns:
        df[account_id] = None

    # 3. 定位到“今天”这一行并更新对应的“账号”列
    # 如果今天还没记录过，.loc 会自动创建新行
    df.loc[today_str, account_id] = balance

    # 4. 排序（可选：按日期由近到远排序，或者按账号ID排序）
    df.sort_index(ascending=False, inplace=True) # 最近日期在最上面

    # 5. 保存回 CSV
    # index=True 会把“日期”这一列写进去
    df.to_csv(DATA_FILE, encoding='utf-8-sig')
    print(f"已更新报表：{today_str} | {account_id} | 余额: {balance}")

if __name__=='__main__':
    update_daily_report()