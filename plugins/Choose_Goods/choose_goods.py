from typing import Dict, Callable, Any
from Util.Parser import JsonObject
from Plugin.Interface import PluginInterface
from loguru import logger
import pyautogui
import pytesseract

class ChooseGoods(PluginInterface):
    def __init__(self, manifest: Dict):
        super().__init__(manifest)
    
    def register_functions(self) -> Dict[str, Callable]:
        funcs: Dict[str, Callable] = {}

        regions = [(200, 500, 100, 50),
            (480, 500, 100, 50),
            (760, 500, 100, 50),
            (1040, 500, 100, 50),
            (200, 838, 100, 50),
            (480, 838, 100, 50),
            (760, 838, 100, 50),
            (1040, 838, 100, 50)]
        
        pos = [[200, 500],
            [480, 500],
            [760, 500],
            [1040, 500],
            [200, 838],
            [480, 838],
            [760, 838],
            [1040, 838]]
        
        def get_prices(regions):
            prices = []
            # reader=easyocr.Reader(['en'], gpu=False, verbose=False)    # 少废话
            custom_config = r'--oem 3 --psm 7 -c tessedit_char_whitelist=0123456789'
            for i, region in enumerate(regions):
                filename = str(i) + '.png'
                screenshot = pyautogui.screenshot(region=region)
                result = pytesseract.image_to_string(screenshot, config=custom_config)

                # result = ocr.classification(screenshot)
                # screenshot.save(filename)
                # result = reader.readtext(filename, allowlist='0123456789', detail=0)
                if result:
                    prices.append(result.strip())
                else:
                    prices.append('-1')
            return prices

        def decide_target(prices):
            target_price = '225'
            for i, price in enumerate(prices):
                if price == target_price:
                    return i
            return -1

        def choose_goods(jsonObject: JsonObject):
            target = decide_target(get_prices(regions))
            # delay: int = jsonObject.content['delay']
            # factor = self.meta.speed
            if target != -1:
                jsonObject.content['action'] = pos[target]
            else:
                jsonObject.content['type'] = "goto"
                jsonObject.content['tolabel'] = "esc"
                
        funcs['cg'] = choose_goods

        return funcs
    