import subprocess
import pyautogui
import pytesseract
import time
from pytesseract import Output

def get_accounts():
    return [
        '3151557406',
        '3610876935',
        '1597036577',
        '3220825744',
    ]

def login(target_id):
    """
    自动化登录函数
    :param target_id: 需要寻找的纯数字字符串 (str)
    """
    # 确保传入的是字符串
    target_id = str(target_id)
    
    # 设置pyautogui的默认间隔，防止操作过快，但题目有特定间隔要求，主要依靠time.sleep
    pyautogui.FAILSAFE = True # 启用防故障功能，鼠标移到左上角可强制停止
    
    print(f"开始执行 login 流程，目标 ID: {target_id}")
    time.sleep(3)
    # 1. 左键单击（823, 992）
    pyautogui.click(823, 992)
    time.sleep(1) # 步骤间隔至少1秒

    # 2. 左键单击（908, 694）
    pyautogui.click(908, 694)
    time.sleep(1)

    # === 循环查找区域 ===
    # 定义搜索区域 (left, top, width, height)
    # 左上角 (768, 722)，右下角 (878, 818)
    # 宽 = 878 - 768 = 110, 高 = 818 - 722 = 96
    region_box = (768, 722, 110, 96)
    
    found = False
    max_attempts = 10  # 防止无限死循环，假设滑到底部的最大尝试次数
    
    for attempt in range(max_attempts):
        print(f"正在第 {attempt + 1} 次扫描区域...")
        
        # 截图指定区域
        screenshot = pyautogui.screenshot(region=region_box)
        
        # 使用 image_to_data 获取详细数据（包含坐标）
        # psm 6 适合原本是单一文本块的图像，whitelist 限制只识别数字提高准确率
        custom_config = r'--psm 6 -c tessedit_char_whitelist=0123456789'
        d = pytesseract.image_to_data(screenshot, config=custom_config, output_type=Output.DICT)
        
        n_boxes = len(d['text'])
        current_found = False
        
        # 遍历识别到的所有文本
        for i in range(n_boxes):
            text = d['text'][i].strip()
            # conf 是置信度，过滤掉低置信度的噪点
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
    
    print("等待 5 秒...")
    time.sleep(5)

    pyautogui.click(1705, 1005)
    time.sleep(45)
    print("流程结束。")

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

def subrun():
    result = subprocess.run([r'E:\Apps\git_repos\KeymouseGo\dist\KeymouseGo.exe', r'E:\Apps\git_repos\KeymouseGo\dist\scripts\mainx3.json5'], capture_output=True, text=True)

    print("错误信息：", result.stderr)
    print("退出状态：", result.returncode)

if __name__ == '__main__':
    ids = get_accounts()
    for id in ids[2:]: 
        login(id)
        subrun()
        logout()

