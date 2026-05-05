import os
import json
import traceback
from pathlib import Path
from importlib import import_module

from rudlgc.core import _getOs
from rudlgc.johnson import Joshua





class GameMetaData:
    class Meta:
        def __init__(self, GAME_METADATA: dict):
            self.GAME_TITLE = GAME_METADATA.get("GAME_TITLE") or "NOT-FOUND-TITLE"
            self.GAME_DESCRIPTION = GAME_METADATA.get("GAME_DESCRIPTION") or "NOT-FOUND-DESCRIPTION"
            self.GAME_ICON = GAME_METADATA.get("GAME_ICON") or "NOT-FOUND-ICON"
            self.GAME_ICON_TRUE = GAME_METADATA.get("GAME_ICON_TRUE") or "NOT-FOUND-ICON-TRUE"
            self.GAME_VERSION = GAME_METADATA.get("GAME_VERSION") or "NOT-FOUND-GAME-VERSION"
            self.COMPANY = GAME_METADATA.get("COMPANY") or "NOT-FOUND-COMPANY"
            self.FILE_VERSION = GAME_METADATA.get("FILE_VERSION") or "NOT-FOUND-FILE-VERSION"

    def __init__(self, GAME_METADATA: dict):
        self.APP_FOLDER = GAME_METADATA.get("APP_FOLDER") or "NOT-FOUND-FOLDER" 
        self.META = self.Meta(GAME_METADATA.get("META") or {})
    


class SettingsCore:
    _DEFAULTS = {
        "WIDTH": 800, "HEIGHT": 600, "MIN_WIDTH": 799, "MIN_HEIGHT": 599,

        "GAME_METADATA": None, "RUDLGC_JOSEPH": None,

        "VSYNC": -1, "WINDOW_MODE": 0,

        "DEBUG": False, "SHOW_INFO": True,

        "FPS": 60,
        
        "POINT_SIZE": 10, "LINE_WIDTH": 10,

        "OS_PLATFORM": _getOs(), 
    }


    def __init__(self, game):
        try: 
            self.__settings_module = import_module(os.getenv("RUDLGC_PROJECT_SETTINGS", ""))
        except ModuleNotFoundError:
            game.logger._system_log("ERROR", traceback.format_exc())
            game.logger._system_log("ERROR", "Game failure exit")
            exit(1)


        self.__GAME = game
        self.JOSEPH = getattr(self.__settings_module, "RUDLGC_JOSEPH", self._DEFAULTS.get("RUDLGC_JOSEPH"))    


        self._WINDOW_WIDTH = getattr(self.__settings_module, "WIDTH", self._DEFAULTS.get("WIDTH"))
        self._WINDOW_HEIGHT = getattr(self.__settings_module, "HEIGHT", self._DEFAULTS.get("HEIGHT"))

        self._WINDOW_MINWIDTH = getattr(self.__settings_module, "MIN_WIDTH", self._DEFAULTS.get("MIN_WIDTH"))
        self._WINDOW_MINHEIGHT = getattr(self.__settings_module, "MIN_HEIGHT", self._DEFAULTS.get("MIN_HEIGHT"))

        # WINDOW ATTR
        self._VSYNC = getattr(self.__settings_module, "VSYNC", self._DEFAULTS.get("VSYNC"))
        self._WINDOW_MODE = getattr(self.__settings_module, "WINDOW_MODE", self._DEFAULTS.get("WINDOW_MODE"))


        # META
        self._GAME_METADATA = getattr(self.__settings_module, "GAME_METADATA", None)
        self._hasInRequiredSettings(self._GAME_METADATA, "GAME_METADATA")
        self._GAME_METADATA = GameMetaData(self._GAME_METADATA)


        # FPS AND DEBUG
        self._FPS = getattr(self.__settings_module, "FPS", self._DEFAULTS.get("FPS"))
        self._SHOW_INFO = getattr(self.__settings_module, "SHOW_INFO", self._DEFAULTS.get("SHOW_INFO"))


        self._DEBUG = getattr(self.__settings_module, "DEBUG", True)
        self._hasInRequiredSettings(self._DEBUG, "DEBUG")


        # RENDER CROSSPLATFORM
        self._POINT_SIZE = getattr(self.__settings_module, "POINT_SIZE", self._DEFAULTS.get("POINT_SIZE"))
        self._LINE_WIDTH = getattr(self.__settings_module, "LINE_WIDTH", self._DEFAULTS.get("LINE_WIDTH"))

        self._OS_PLATFORM = _getOs()
        

        for attr in dir(self.__settings_module):
            if attr not in SettingsCore._DEFAULTS and not attr.startswith("__") and attr.isupper():
                value = getattr(self.__settings_module, attr)
                setattr(self, attr, value)


    def _hasInRequiredSettings(self, VARS, his_name):
        if VARS is None:
            self.__GAME.logger._system_log("ERROR", f"{his_name} is not declarated in {os.getenv('RUDLGC_PROJECT_SETTINGS')}/settings.py")
            self.__GAME.logger._system_log("ERROR", "Game failure exit")
            exit(1)

    


    @property
    def OS_PLATFORM(self):
        return self._OS_PLATFORM
    

    @property
    def WINDOW_WIDTH(self):
        return self._WINDOW_WIDTH
    
        
    @property
    def WINDOW_HEIGHT(self):
        return self._WINDOW_HEIGHT
    
    @property
    def WINDOW_MINWIDTH(self):
        return self._WINDOW_MINWIDTH
    

    @property
    def WINDOW_MINHEIGHT(self):
        return self._WINDOW_MINHEIGHT
    
    @property
    def WINDOW_MODE(self):
        return self._WINDOW_MODE
    
    
    # READ-WRITE
    @property
    def DEBUG(self):
        return self._DEBUG
    

    @property
    def FPS(self):
        return self._FPS
    
        
    @property
    def VSYNC(self):
        return self._VSYNC
    


    @property
    def POINT_SIZE(self):
        return self._POINT_SIZE
    

    @property
    def LINE_WIDTH(self):
        return self._LINE_WIDTH


    

    
