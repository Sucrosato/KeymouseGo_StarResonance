import subprocess
import pyautogui
import pytesseract
import time
from pytesseract import Output


def login(target_id):
    """
    自动化登录函数
    :param target_id: 需要寻找的纯数字字符串 (str)
    """
    # 确保传入的是字符串
    target_id = str(target_id)
    
    pyautogui.FAILSAFE = True # 启用防故障功能，鼠标移到左上角可强制停止
    
    print(f"开始执行 login 流程，目标 ID: {target_id}")
    time.sleep(3)
    pyautogui.click(823, 992)
    time.sleep(1) 
    
    pyautogui.click(908, 694)
    time.sleep(1)

    #找到要登录的账号
    region_box = (768, 722, 110, 96)
    
    found = False
    max_attempts = 10  
    
    for attempt in range(max_attempts):
        print(f"正在第 {attempt + 1} 次扫描区域...")
        
        screenshot = pyautogui.screenshot(region=region_box)
        
        custom_config = r'--psm 6 -c tessedit_char_whitelist=0123456789'
        d = pytesseract.image_to_data(screenshot, config=custom_config, output_type=Output.DICT)
        
        n_boxes = len(d['text'])
        current_found = False
        
        for i in range(n_boxes):
            text = d['text'][i].strip()
            if int(d['conf'][i]) > 0 and text == target_id:
                click_x = region_box[0] + d['left'][i] + d['width'][i] / 2
                click_y = region_box[1] + d['top'][i] + d['height'][i] / 2
                
                print(f"找到目标 {target_id}，坐标: ({click_x}, {click_y})，执行点击。")
                pyautogui.click(click_x, click_y)
                found = True
                current_found = True
                break
        
        if found:
            time.sleep(1)
            break
        
        print("未找到目标，执行下滑...")
        
        # 将鼠标移动到区域中间进行滚动
        center_x = region_box[0] + region_box[2] // 2
        center_y = region_box[1] + region_box[3] // 2
        pyautogui.moveTo(center_x, center_y)
        
        pyautogui.scroll(-300) 
        time.sleep(1.5) # 等待滚动动画完成
        

    if not found:
        raise RuntimeError(f"错误：在尝试滑动 {max_attempts} 次后，仍未在指定区域找到 ID {target_id}。")

    pyautogui.click(823, 825)
    
    time.sleep(5)
    while not pyautogui.locateOnScreen(r'E:\Apps\git_repos\KeymouseGo\dist\data\pics\qidong,1695,998,44,24.png', confidence=0.8, region=(1695, 998, 44, 24)):
        pyautogui.click(1705, 1005)
        time.sleep(60) #更新检测
    pyautogui.click(1705, 1005)
    time.sleep(45)

def logout():
    time.sleep(5)
    pyautogui.click(2464, 87)
    time.sleep(1)
    pyautogui.click(1591, 1059)
    time.sleep(10)
    pyautogui.click(1718, 367)
    time.sleep(1)
    pyautogui.click(1721, 596)
    time.sleep(10)

def subrun(slow=False):
    if not slow:
        result = subprocess.run([r'E:\Apps\git_repos\KeymouseGo\dist\KeymouseGo.exe', r'E:\Apps\git_repos\KeymouseGo\dist\scripts\mainx3.json5'], capture_output=True, text=True)
    else:
        result = subprocess.run([r'E:\Apps\git_repos\KeymouseGo\dist\KeymouseGo.exe', r'E:\Apps\git_repos\KeymouseGo\dist\scripts\mainx3_slow.json5'], capture_output=True, text=True)
    print("错误信息：", result.stderr)
    print("退出状态：", result.returncode)