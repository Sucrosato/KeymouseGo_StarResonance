from typing import Dict, Callable, Any
from Util.Parser import JsonObject
from Plugin.Interface import PluginInterface
from loguru import logger
import pyautogui
import sys

class Locate(PluginInterface):
    def __init__(self, manifest: Dict):
        super().__init__(manifest)
    
    def register_functions(self) -> Dict[str, Callable]:
        funcs: Dict[str, Callable] = {}

        
        def locate(jsonObject: JsonObject):
            sys.stderr = open('error.log', 'w', encoding='utf-8')

            goal = jsonObject.content['variable'][0]
            region = tuple(jsonObject.content['variable'][1])
            target = None
            #try:
            location = pyautogui.locateOnScreen(
                            'E:/Apps/git_repos/KeymouseGo/dist/plugins/Locate/pics/'+goal+'.png',
                            region=region,
                            confidence=0.8,
                            grayscale=True
                        )
            point = pyautogui.center(location)
            target = [int(point.x), int(point.y)]
            #except:
            #    target = None


            # target = decide_target(get_prices(regions))
            # delay: int = jsonObject.content['delay']
            # factor = self.meta.speed
            if target:
                jsonObject.content['action'] = target
            else:
                pass
                # jsonObject.content['type'] = "goto"
                # jsonObject.content['tolabel'] = "exit_market"
        funcs['lct'] = locate

        return funcs
    