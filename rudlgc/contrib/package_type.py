from typing import *


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

    PPS: float
    FPS: float

    SHOW_FPS: bool
    SHOW_INFO: bool

    GAME_ICON: str
    GAME_NAME: str
    GAME_VERSION: str
    GAME_DESCRIPTION: str

    APPNAME: str
    JSON_SETTINGS: str
    FILE_VERSION: str
    GAME_RIGHT: str

    TITLE: str
    START_SCENE: str
    OS_PLATFORM: str

    MUSIC_VOLUME: float
    SOUND_VOLUME: float

    POINT_SIZE: float
    LINE_SIZE: float



class _RequestType:
    def closeGame(self) -> None: ...

    def updateSettings(self) -> None: ...

    def redirectScene(self, scene) -> None: ...
    def restartScene(self) -> None: ...


    def setScreenColor(self, r: float, g: float, b: float) -> None: ...
    def setWindowPosition(self, x: int, y: int) -> None: ...
    def setWindowSize(self, w: int, h: int) -> None: ...
    def setWindowTitle(self, title: str) -> None: ...
    def setWindowGrab(self, flag: bool) -> None: ...
    def setWindowRelative(self, flag: bool) -> None: ...



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



class _Keyboard:
    def isPressed(self, key: int) -> bool: ...

class _Mouse:
    def isLeft(self) -> bool: ...
    def isMiddle(self) -> bool: ...
    def isRight(self) -> bool: ...

    def getPos(self) -> tuple[float, float]: ...
    def getRel(self) -> tuple[float, float]: ...



class GameType(Protocol):
    api: _RequestType
    settings: _Settings
    paths: _PathsType
    logger: _LoggerType

    delta_time: float
    tick_time: float

    keyboard: _Keyboard
    mouse: _Mouse

    PROJECT_NAME: str
    ERROR: str

    def getFps(self) -> float: ...
    def getCurrentScene(self) -> str: ...





class AbstractScene:
    def __init__(self, game: GameType):
        pass

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

    

