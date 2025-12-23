from typing import Dict, Callable, Any
from Util.Parser import JsonObject
from Plugin.Interface import PluginInterface
from loguru import logger
from utils import update_daily_report

class BalanceReport(PluginInterface):
    def __init__(self, manifest: Dict):
        super().__init__(manifest)
    
    def register_functions(self) -> Dict[str, Callable]:
        funcs: Dict[str, Callable] = {}

        def balance_report(jsonObject: JsonObject):
            update_daily_report()


        funcs['br'] = balance_report

        return funcs
    