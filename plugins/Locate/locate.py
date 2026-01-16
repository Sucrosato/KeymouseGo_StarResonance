from typing import Dict, Callable, Any
from Util.Parser import JsonObject
from Plugin.Interface import PluginInterface
from loguru import logger
import pyautogui
import sys
from time import sleep

class Locate(PluginInterface):
    def __init__(self, manifest: Dict):
        super().__init__(manifest)
    
    def register_functions(self) -> Dict[str, Callable]:
        funcs: Dict[str, Callable] = {}

        
        def locate(jsonObject: JsonObject):
            sys.stderr = open('error.log', 'w', encoding='utf-8')

            goal = jsonObject.content['variable'][0]
            region = None
            confidence = 0.8
            grayscale = True
            try:
                region = tuple(jsonObject.content['variable'][1])
                confidence = jsonObject.content['variable'][2]
                grayscale = jsonObject.content['variable'][3]
            except:
                pass
            target = None
            location = None

            try:
                location = pyautogui.locateOnScreen(
                                'E:/Apps/git_repos/KeymouseGo/dist/data/pics/'+goal+'.png',
                                region=region,
                                confidence=confidence,
                                grayscale=grayscale
                            )
                point = pyautogui.center(location)
                target = [int(point.x), int(point.y)]
                if jsonObject.content.get('action'):
                    jsonObject.content['action'] = target
                return True
            except:
                return False
            
        funcs['lct'] = locate

        return funcs
    