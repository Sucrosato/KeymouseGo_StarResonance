from typing import Dict, Callable, Any
from Util.Parser import JsonObject
from Plugin.Interface import PluginInterface
from loguru import logger
import random

class JudgeFunction(PluginInterface):
    def __init__(self, manifest: Dict):
        super().__init__(manifest)

    def register_functions(self) -> Dict[str, Callable]:
        funcs: Dict[str, Callable] = {}

        def judge_function(jsonObject: JsonObject):
            # delay: int = jsonObject.content['delay']
            # factor = self.meta.speed
            # jsonObject.content['delay'] = int(delay / factor)
            jsonObject.content['action'] = [600, 480]

        funcs['jf'] = judge_function

        return funcs
    