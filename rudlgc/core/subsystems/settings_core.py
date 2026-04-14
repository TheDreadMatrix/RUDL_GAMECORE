import os
import platform
import traceback
from importlib import import_module
from rudlgc.johnson import Joshua


def _get_os():
    system = platform.system().lower()
    machine = platform.machine().lower()

    if system == "windows":
        return "Windows"
    
    if system == "darwin":
        if "iphone" in machine or "ipad" in machine:
            return "iOS"
        return "macOS"

    if system == "linux":
        if ("ANDROID_ROOT" in os.environ or "ANDROID_DATA" in os.environ or "ANDROID_BOOTLOGO" in os.environ):
            return "Android"
        return "Linux"
    


class SettingsCore:
    _DEFAULTS = {
        "DEBUG": True,

        "WINDOW_WIDTH": 800,
        "WINDOW_HEIGHT": 600,
        "WINDOW_MINWIDTH": 799,
        "WINDOW_MINHEIGHT": 599,

        "APPNAME": ".rudlgcGameData",
        "JSON_SETTINGS": None,

        "GAME_NAME": "RUDLGC game!!!",
        "GAME_ICON": None,
        "GAME_DESCRIPTION": "RUDL Game Core Engine!!!",
        "GAME_VERSION": "0.1.0",
        "GAME_RIGHT": "NONE",
        "FILE_VERSION": "1.0.0.0",

        "VSYNC": 0,
        "FULLSCREEN": False,
        "BORDERLESS": False,
        "RESIZABLE": False,

        "START_SCENE": "empty-rudlgc",
        "SHOW_FPS": True,
        "SHOW_INFO": True,

        "MUSIC_VOLUME": 1.0,
        "SOUND_VOLUME": 1.0,

        "FPS": 240,
        "PPS": 240,

        "POINT_SIZE": 10,
        "LINE_SIZE": 10,

        "OS_PLATFORM": str(_get_os()).upper()


        
    }

    def __init__(self, game):
        try: 
            self.__settings_module = import_module(os.getenv("RUDLGC_PROJECT_SETTINGS", ""))
        except ModuleNotFoundError:
            game.logger._system_log("ERROR", traceback.format_exc())
            game.logger._system_log("ERROR", "Game failure exit")
            exit(1)

        self._JSON_SETTINGS = getattr(self.__settings_module, "JSON_SETTINGS", None)
        if self._JSON_SETTINGS:
           self._joshua_settings = Joshua(game.paths.getSavesPath(*self._JSON_SETTINGS["FOLDERS"], file=self._JSON_SETTINGS["FILE"]))
        else:
            self._joshua_settings = {}

        self.DEBUG = getattr(self.__settings_module, "DEBUG", True)
        self.APPNAME = getattr(self.__settings_module, "APPNAME", ".rudlgcGameData")

        self.WINDOW_WIDTH = getattr(self.__settings_module, "WINDOW_WIDTH", 800)
        self.WINDOW_HEIGHT = getattr(self.__settings_module, "WINDOW_HEIGHT", 600)

        self.WINDOW_MINWIDTH = getattr(self.__settings_module, "WINDOW_MINWIDTH", 799)
        self.WINDOW_MINHEIGHT = getattr(self.__settings_module, "WINDOW_MINHEIGHT", 599)

        self.VSYNC = getattr(self.__settings_module, "VSYNC", False)
        self.FULLSCREEN = getattr(self.__settings_module, "FULLSCREEN", False)
        self.BORDERLESS = getattr(self.__settings_module, "BORDERLESS", False)
        self.RESIZABLE = getattr(self.__settings_module, "RESIZABLE", False)

        self.GAME_ICON = getattr(self.__settings_module, "GAME_ICON", None)
        self.GAME_NAME = getattr(self.__settings_module, "GAME_NAME", "RUDLGC game!!!")
        self.GAME_DESCRIPTION = getattr(self.__settings_module, "GAME_DESCRIPTION", "RUDL Game Core Engine!!!")
        self.GAME_VERSION = getattr(self.__settings_module, "GAME_VERSION", "0.1.0")

        self.GAME_RIGHT = getattr(self.__settings_module, "GAME_RIGHT", "NONE")
        self.FILE_VERSION = getattr(self.__settings_module, "FILE_VERSION", "1.0.0.0")

        self.FPS = getattr(self.__settings_module, "FPS", 240)
        self.PPS = getattr(self.__settings_module, "PPS", 240)

        self.START_SCENE = getattr(self.__settings_module, "START_SCENE", "empty-rudlgc")
        self.SHOW_FPS = getattr(self.__settings_module, "SHOW_FPS", True)
        self.SHOW_INFO = getattr(self.__settings_module, "SHOW_INFO", True)

        self.MUSIC_VOLUME = getattr(self.__settings_module, "MUSIC_VOLUME", 1.0)
        self.SOUND_VOLUME = getattr(self.__settings_module, "SOUND_VOLUME", 1.0)

        self.POINT_SIZE = getattr(self.__settings_module, "POINT_SIZE", 10)
        self.LINE_SIZE = getattr(self.__settings_module, "LINE_SIZE", 10)

        self.OS_PLATFORM = str(_get_os()).upper()

        for attr in dir(self.__settings_module):
            if attr not in SettingsCore._DEFAULTS and not attr.startswith("__") and attr.isupper():
                value = getattr(self.__settings_module, attr)
                setattr(self, attr, value)

    def _getSettings(self, key, default, category=""):
        

        return default
    