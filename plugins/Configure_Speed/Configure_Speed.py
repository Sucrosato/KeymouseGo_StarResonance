from typing import Dict, Callable, Any
from Util.Parser import JsonObject
from Plugin.Interface import PluginInterface
from loguru import logger


class ConfigureSpeed(PluginInterface):
    def __init__(self, manifest: Dict):
        super().__init__(manifest)

    def register_functions(self) -> Dict[str, Callable]:
        funcs: Dict[str, Callable] = {}

        def change_speed(jsonObject: JsonObject):
            delay: int = jsonObject.content['delay']
            factor = self.meta.speed
            jsonObject.content['delay'] = int(delay / factor)

        funcs['cs'] = change_speed

        return funcs