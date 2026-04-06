from typing import *
from abc import abstractmethod, ABC


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



class GameType(Protocol):
    request: Any
    requirements: Any
    settings: _Settings
    paths: Any

    johnson: Any
    xmllion: Any


    delta_time: float
    physic_time: float

    def getFps(self) -> float: ...
    def getScene(self) -> str: ...




class AbstractScene(ABC):
    @abstractmethod
    def __init__(self, game: GameType):
        pass

    @abstractmethod
    def onUpdate(self):
        pass

    @abstractmethod
    def onEvent(self, event):
        pass

    @abstractmethod
    def onRender(self):
        pass

    
    def onSave(self):
        pass

