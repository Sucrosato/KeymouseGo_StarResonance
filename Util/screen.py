import pyautogui
import pytesseract

def ocr_num(region):
    
    custom_config = r'--oem 3 --psm 7 -c tessedit_char_whitelist=0123456789,'
    
    filename = 'data/screenshot.png'
    screenshot = pyautogui.screenshot(region=region, )
    screenshot.save(filename)
    result = pytesseract.image_to_string(screenshot, config=custom_config)
    result = result.replace(',', '').replace('\n', '')
    
    return result
