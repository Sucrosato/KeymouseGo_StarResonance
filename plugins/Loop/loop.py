from typing import Dict, Callable, Any
from Util.Parser import JsonObject
from Plugin.Interface import PluginInterface
from loguru import logger
import pyautogui
import time
# 参数说明：["find"/"lose"/"times", times/[goal, region], sleep_time, press/click, key/position]
class Loop(PluginInterface):
    def __init__(self, manifest: Dict):
        super().__init__(manifest)
    
    def register_functions(self) -> Dict[str, Callable]:
        funcs: Dict[str, Callable] = {}

        def loop(jsonObject: JsonObject):
            stop_condition = jsonObject.content['variable'][0]
            condition_data = jsonObject.content['variable'][1]
            sleep_time = 1
            action_type, action = None, None
            try:
                sleep_time = jsonObject.content['variable'][2]
                action_type = jsonObject.content['variable'][3]
                action = jsonObject.content['variable'][4]
            except:
                pass

            def do_action(action_type, action):
                if action_type == 'press':
                    pyautogui.press(action)
                elif action_type == 'click':
                    pyautogui.click(*action)

            def locate(goal, region):
                try:
                    location = pyautogui.locateOnScreen(
                                    'E:/Apps/git_repos/KeymouseGo/dist/data/pics/'+goal+'.png',
                                    region=region,
                                    confidence=0.8,
                                    grayscale=True
                                )
                    return True
                except:
                    return False
                
            match stop_condition:
                case 'times':
                    for i in range(condition_data):
                        do_action(action_type, action)
                        time.sleep(sleep_time)
                case 'find':
                    times = 0
                    while not locate(*condition_data):
                        do_action(action_type, action)
                        time.sleep(sleep_time)
                        times += 1
                        if times > 100:
                            raise RuntimeError()
                case 'lose':
                    times = 0
                    while locate(*condition_data):
                        do_action(action_type, action)
                        time.sleep(sleep_time)
                        times += 1
                        if times > 100:
                            raise RuntimeError()



        funcs['loop'] = loop

        return funcs
    