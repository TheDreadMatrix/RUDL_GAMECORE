import traceback
from importlib import import_module

from rudlgc.core import _getOs





class GameMetaData:
    def __init__(self, GAME_METADATA: dict):
        self.GAME_TITLE = GAME_METADATA.get("GAME_TITLE") or "NOT-FOUND-TITLE"
        self.GAME_DESCRIPTION = GAME_METADATA.get("GAME_DESCRIPTION") or "NOT-FOUND-DESCRIPTION"
        self.GAME_ICON = GAME_METADATA.get("GAME_ICON") or "NOT-FOUND-ICON"
        self.GAME_ICON_TRUE = GAME_METADATA.get("GAME_ICON_TRUE") or "NOT-FOUND-ICON-TRUE"
        self.GAME_VERSION = GAME_METADATA.get("GAME_VERSION") or "NOT-FOUND-GAME-VERSION"
        self.COMPANY = GAME_METADATA.get("COMPANY") or "NOT-FOUND-COMPANY"
    


class SettingsCore:
    _DEFAULTS = {
        "WIDTH": 800, "HEIGHT": 600, "MIN_WIDTH": 799, "MIN_HEIGHT": 599,

        "GAME_METADATA": None, "RUDLGC_JOSEPH": None, "RUDLGC_APP_FOLDER": None,

        "VSYNC": -1, "WINDOW_MODE": 0,

        "DEBUG": False, "SHOW_INFO": True,

        "FPS": 60,

        "RUDLGC_RENDER_BACKEND": 0,
        
        "POINT_SIZE": 10, "LINE_WIDTH": 10,

        "OS_PLATFORM": _getOs(), 
    }


    def __init__(self, game):
        try: 
            __settings_module = import_module(f"{game.PROJECT_NAME}.settings")
        except ModuleNotFoundError:
            game.logger._system_log("ERROR", traceback.format_exc())
            game.logger._system_log("ERROR", "Game failure exit")
            exit(1)



        # RUDLGC
        self._JOSEPH = getattr(__settings_module, "RUDLGC_JOSEPH", self._DEFAULTS.get("RUDLGC_JOSEPH"))
        self._RENDER_BACKEND = getattr(__settings_module, "RUDLGC_RENDER_BACKEND", self._DEFAULTS.get("RUDLGC_RENDER_BACKEND"))

        self._APP_FOLDER = getattr(__settings_module, "RUDLGC_APP_FOLDER", None)    
        self._hasInRequiredSettings(self._APP_FOLDER, "APP_FOLDER", game)


        # WINDOW SIZES
        self._WINDOW_WIDTH = getattr(__settings_module, "WIDTH", self._DEFAULTS.get("WIDTH"))
        self._WINDOW_HEIGHT = getattr(__settings_module, "HEIGHT", self._DEFAULTS.get("HEIGHT"))

        self._WINDOW_MINWIDTH = getattr(__settings_module, "MIN_WIDTH", self._DEFAULTS.get("MIN_WIDTH"))
        self._WINDOW_MINHEIGHT = getattr(__settings_module, "MIN_HEIGHT", self._DEFAULTS.get("MIN_HEIGHT"))

        # WINDOW ATTR
        self._VSYNC = getattr(__settings_module, "VSYNC", self._DEFAULTS.get("VSYNC"))
        self._WINDOW_MODE = getattr(__settings_module, "WINDOW_MODE", self._DEFAULTS.get("WINDOW_MODE"))
        self._FPS = getattr(__settings_module, "FPS", self._DEFAULTS.get("FPS"))


        # META
        self._GAME_METADATA = getattr(__settings_module, "GAME_METADATA", None)
        self._hasInRequiredSettings(self._GAME_METADATA, "GAME_METADATA", game)
        self._GAME_METADATA = GameMetaData(self._GAME_METADATA)


        # READ-WRITE
        self.SHOW_INFO = getattr(__settings_module, "SHOW_INFO", True)
        self.DEBUG = getattr(__settings_module, "DEBUG", None)
        self._hasInRequiredSettings(self.DEBUG, "DEBUG", game)


        # RENDER CROSSPLATFORM
        self._POINT_SIZE = getattr(__settings_module, "POINT_SIZE", self._DEFAULTS.get("POINT_SIZE"))
        self._LINE_WIDTH = getattr(__settings_module, "LINE_WIDTH", self._DEFAULTS.get("LINE_WIDTH"))

        self._OS_PLATFORM = _getOs()
        

        for attr in dir(__settings_module):
            if attr not in SettingsCore._DEFAULTS and not attr.startswith("__") and attr.isupper():
                value = getattr(__settings_module, attr)
                setattr(self, attr, value)


    def _hasInRequiredSettings(self, VARS, his_name, game):
        if VARS is None:
            game.logger._system_log("ERROR", f"{his_name} is not declarated in {game.PROJECT_NAME}/settings.py")
            game.logger._system_log("ERROR", "Game failure exit")
            exit(1)

    


    @property
    def OS_PLATFORM(self):
        return self._OS_PLATFORM
    

    @property
    def JOSEPH(self):
        return self._JOSEPH
    

    

    

    



    

    
