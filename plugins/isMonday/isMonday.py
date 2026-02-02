from typing import Dict, Callable, Any
from Util.Parser import JsonObject
from Plugin.Interface import PluginInterface
from loguru import logger
from datetime import datetime, timedelta

class IsMonday(PluginInterface):
    def __init__(self, manifest: Dict):
        super().__init__(manifest)

    def register_functions(self) -> Dict[str, Callable]:
        funcs: Dict[str, Callable] = {}

        def isMonday(jsonObject: JsonObject):
            shifted_time = datetime.now() - timedelta(hours=5)
            return shifted_time.weekday() == 0

        funcs['isMonday'] = isMonday

        return funcs
    