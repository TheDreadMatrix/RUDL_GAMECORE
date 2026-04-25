import os
import traceback
from importlib import import_module

from rudlgc.core import _getOs






class GameMetaData:
    class Meta:
        def __init__(self, GAME_METADATA: dict):
            self.GAME_TITLE = GAME_METADATA.get("GAME_TITLE") or "NOT-FOUND-TITLE"
            self.GAME_DESCRIPTION = GAME_METADATA.get("GAME_DESCRIPTION") or "NOT-FOUND-DESCRIPTION"
            self.GAME_ICON = GAME_METADATA.get("GAME_ICON") or "NOT-FOUND-ICON"
            self.GAME_VERSION = GAME_METADATA.get("GAME_VERSION") or "NOT-FOUND-GAME-VERSION"
            self.COMPANY = GAME_METADATA.get("COMPANY") or "NOT-FOUND-COMPANY"
            self.FILE_VERSION = GAME_METADATA.get("FILE_VERSION") or "NOT-FOUND-FILE-VERSION"

    def __init__(self, GAME_METADATA: dict):
        self.APP_FOLDER = GAME_METADATA.get("APP_FOLDER") or "NOT-FOUND-FOLDER" 
        self.META = self.Meta(GAME_METADATA.get("META") or {})
    


class SettingsCore:
    _DEFAULTS = {
        "DEBUG": False,

        "WINDOW_WIDTH": 800,
        "WINDOW_HEIGHT": 600,
        "WINDOW_MINWIDTH": 799,
        "WINDOW_MINHEIGHT": 599,

        "GAME_METADATA": None,

        "VSYNC": 0,
        "FULLSCREEN": False,
        "BORDERLESS": False,
        "RESIZABLE": True,

       
        "SHOW_INFO": True,

        "MUSIC_VOLUME": 1.0,
        "SOUND_VOLUME": 1.0,

        "FPS": 240,
        

        "POINT_SIZE": 10,
        "LINE_SIZE": 10,

        "OS_PLATFORM": _getOs(),
        


        
    }

    def __init__(self, game):
        try: 
            self.__settings_module = import_module(os.getenv("RUDLGC_PROJECT_SETTINGS", ""))
        except ModuleNotFoundError:
            game.logger._system_log("ERROR", traceback.format_exc())
            game.logger._system_log("ERROR", "Game failure exit")
            exit(1)


        self.__game = game

        self.DEBUG = getattr(self.__settings_module, "DEBUG", True)
        self._hasInRequiredSettings(self.DEBUG, "DEBUG")

        self.WINDOW_WIDTH = getattr(self.__settings_module, "WINDOW_WIDTH", self._DEFAULTS.get("WINDOW_WIDTH"))
        self.WINDOW_HEIGHT = getattr(self.__settings_module, "WINDOW_HEIGHT", self._DEFAULTS.get("WINDOW_HEIGHT"))

        self.WINDOW_MINWIDTH = getattr(self.__settings_module, "WINDOW_MINWIDTH", self._DEFAULTS.get("WINDOW_MINWIDTH"))
        self.WINDOW_MINHEIGHT = getattr(self.__settings_module, "WINDOW_MINHEIGHT", self._DEFAULTS.get("WINDOW_MINHEIGHT"))

        self.VSYNC = getattr(self.__settings_module, "VSYNC", self._DEFAULTS.get("VSYNC"))
        self.FULLSCREEN = getattr(self.__settings_module, "FULLSCREEN", self._DEFAULTS.get("FULLSCREEN"))
        self.BORDERLESS = getattr(self.__settings_module, "BORDERLESS", self._DEFAULTS.get("BORDERLESS"))
        self.RESIZABLE = getattr(self.__settings_module, "RESIZABLE", self._DEFAULTS.get("RESIZABLE"))

        self.GAME_METADATA = getattr(self.__settings_module, "GAME_METADATA", None)
        self._hasInRequiredSettings(self.GAME_METADATA, "GAME_METADATA")
        self.GAME_METADATA = GameMetaData(self.GAME_METADATA)


        self.FPS = getattr(self.__settings_module, "FPS", self._DEFAULTS.get("FPS"))
        
        self.SHOW_INFO = getattr(self.__settings_module, "SHOW_INFO", self._DEFAULTS.get("SHOW_INFO"))

        self.MUSIC_VOLUME = getattr(self.__settings_module, "MUSIC_VOLUME", self._DEFAULTS.get("MUSIC_VOLUME"))
        self.SOUND_VOLUME = getattr(self.__settings_module, "SOUND_VOLUME", self._DEFAULTS.get("SOUND_VOLUME"))

        self.POINT_SIZE = getattr(self.__settings_module, "POINT_SIZE", self._DEFAULTS.get("POINT_SIZE"))
        self.LINE_SIZE = getattr(self.__settings_module, "LINE_SIZE", self._DEFAULTS.get("LINE_SIZE"))

        self.OS_PLATFORM = _getOs()
        

        for attr in dir(self.__settings_module):
            if attr not in SettingsCore._DEFAULTS and not attr.startswith("__") and attr.isupper():
                value = getattr(self.__settings_module, attr)
                setattr(self, attr, value)


    def _hasInRequiredSettings(self, VARS, his_name):
        if VARS is None:
            self.__game.logger._system_log("ERROR", f"{his_name} is not declarated in {os.getenv("RUDLGC_PROJECT_SETTINGS")}/settings.py")
            self.__game.logger._system_log("ERROR", "Game failure exit")
            exit(1)

    