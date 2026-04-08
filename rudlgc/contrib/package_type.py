from typing import *
import moderngl
import sdl2
import PIL
import glm


class _Settings:
    DEBUG: bool
    VSYNC: bool

    WINDOW_WIDTH: int
    WINDOW_HEIGHT: int
    WINDOW_MINWIDTH: int|None
    WINDOW_MINHEIGHT: int|None
    WINDOW_MAXWIDTH: int|None
    WINDOW_MAXHEIGHT: int|None

    FULLSCREEN: bool
    BORDERLESS: bool
    RESIZABLE: bool

    PPS: float
    FPS: float

    SHOW_FPS: bool
    SHOW_INFO: bool
    SHOW_PROMPT: bool

    START_SCENE: str

    GAME_NAME: str
    GAME_VERSION: str
    GAME_DESCRIPTION: str

    FILE_VERSION: str
    GAME_RIGHT: str

    TITLE: str

    MUSIC_VOLUME: float
    SOUND_VOLUME: float

    POINT_SIZE: float
    LINE_SIZE: float


class _RequirementsType:
    sdl2 = sdl2
    pyglm = glm
    moderngl = moderngl
    pillow = PIL


class _RequestType:
    def closeGame(self) -> None: ...

    def updateSettings(self) -> None: ...

    def redirectScene(self, scene) -> str: ...
    def restartScene(self): ...

    def setWindowPosition(self, x: int, y: int): ...
    def setWindowSize(self, w: int, h: int): ...
    


class _LoggerType:
    @staticmethod
    def trace(message: str) -> None: ...
    @staticmethod
    def _system_log(tag: str, message: str) -> None: ...



class GameType(Protocol):
    request: _RequestType
    requirements: _RequirementsType
    settings: _Settings
    paths: Any
    logger: _LoggerType

    johnson: Any
    xmllion: Any


    delta_time: float
    pelta_time: float

    def getFps(self) -> float: ...
    def getCurrentScene(self) -> str: ...





class AbstractScene:
    def __init__(self, game: GameType):
        pass

    def onUpdate(self):
        pass

    def onEvent(self, event):
        pass

    def onRender(self):
        pass
    
    def onSave(self):
        pass

