from typing import *
import PIL
import glm
import moderngl
import sdl2

class _GameMetaType:
    class _Meta:
        GAME_ICON: str
        GAME_TITLE: str
        GAME_VERSION: str
        GAME_DESCRIPTION: str
        FILE_VERSION: str
        COMPANY: str

    APP_FOLDER: str
    META: _Meta


class _Settings:
    DEBUG: bool

    WINDOW_WIDTH: int
    WINDOW_HEIGHT: int
    WINDOW_MINWIDTH: int
    WINDOW_MINHEIGHT: int

    VSYNC: int
    FULLSCREEN: bool
    BORDERLESS: bool
    RESIZABLE: bool

    FPS: float

    SHOW_FPS: bool
    SHOW_INFO: bool

    GAME_METADATA: _GameMetaType

    START_SCENE: str
    OS_PLATFORM: str
    GRAPHICS_API: str

    MUSIC_VOLUME: float
    SOUND_VOLUME: float

    POINT_SIZE: float
    LINE_SIZE: float



class _RequestType:
    def closeGame(self) -> None: ...

    def redirectScene(self, scene: str) -> None: ...
    def restartScene(self) -> None: ...


class _WindowApiType:
    pass


class _EventApiType:
    pass
    



class _PathsType:
    def getConfigPath(self, *folder: str, file: str) -> str: ...
    def getSavesPath(self, *folder: str, file: str) -> str: ...
    def getMusicsPath(self, *folder: str, file: str) -> str: ...
    def getSoundsPath(self, *folder: str, file: str) -> str: ...
    def getAssetsPath(self, *folder: str, file: str) -> str: ...
    def getFontsPath(self, *folder: str, file: str) -> str: ...
    def getShadersPath(self, *folder: str, file: str) -> str: ...
    


class _LoggerType:
    @staticmethod
    def trace(message: str, as_error: bool=False) -> None: ...
    @staticmethod
    def traceMagenta(message: str) -> None: ...


class _RequirementsType:
    mgl: moderngl
    sdl: sdl2
    pillow: PIL
    glm5: glm


class _Gamepad:
    NOT_WORKING: int


class _Keyboard:
    def isPressDown(self, key: int, event) -> bool: ...
    def isPressUp(self, key: int, event) -> bool: ...
    def isPress(self, key: int) -> bool: ...

class _Mouse:
    def mouseEnter(self, event) -> bool: ...
    def mouseLeave(self, event) -> bool: ...
    def mouseButtonDown(self, button: int, event) -> bool: ...
    def mouseButtonUp(self, button: int, event) -> bool: ...

    def isLeft(self) -> bool: ...
    def isMiddle(self) -> bool: ...  
    def isRight(self) -> bool: ...

    def getPos(self) -> tuple[float, float]: ...
    def getRel(self) -> tuple[float, float]: ...
    def getWheel(self) -> float: ...



class GameType(Protocol):
    config_api: _RequestType
    window_api: _WindowApiType
    event_api: _EventApiType

    settings: _Settings
    paths: _PathsType
    logger: _LoggerType

    delta_time: float
    tick_time: float

    keyboard: _Keyboard
    gamepad: _Gamepad
    mouse: _Mouse

    PROJECT_NAME: str
    ERROR: str

    _requirements: _RequirementsType

    def getFps(self) -> float: ...
    def getTps(self) -> float: ...
    def getCurrentScene(self) -> str: ...





class PackageScene:
    def __init__(self, game: GameType):
        self.game = game

        self.keyboard = game.keyboard
        self.mouse = game.mouse

        self.window_api = game.window_api
        self.event_api = game.event_api
        self.config_api = game.config_api

        self.settings = game.settings
        self.paths = game.paths
        self.logger = game.logger

        self._requirements = game._requirements

    def onFixedUpdate(self):
        pass

    def onUpdate(self): 
        pass

    def onEvent(self, event):
        pass

    def onRender(self):
        pass
    
    def onSave(self):
        pass

    

