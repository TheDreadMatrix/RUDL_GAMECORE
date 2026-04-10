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

    APPNAME: str
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

    def redirectScene(self, scene) -> None: ...
    def restartScene(self) -> None: ...


    def setScreenColor(self, r: float, g: float, b: float) -> None: ...
    def setWindowPosition(self, x: int, y: int) -> None: ...
    def setWindowSize(self, w: int, h: int) -> None: ...
    def setWindowTitle(self, title: str) -> None: ...



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
    def trace(message: str) -> None: ...
    @staticmethod
    def traceMagenta(message: str) -> None: ...



class _JoshuaType:
    def __init__(self, json_path: str): ...

    def readData(self) -> Dict[str, Any]: ...
    def saveData(self, json_data: Dict[str, Any]) -> None: ...


class _XmlionType:
    def __init__(self, xml_path: str): ...

    def readDataXml(self) -> Any: ...
    def saveDataXml(self, xml_data: Any) -> None: ...


class _JohnsonType:
    def giveJoshua(self) -> _JoshuaType: ...
    def giveXmlion(self) -> _XmlionType: ...



class GameType(Protocol):
    request: _RequestType
    requirements: _RequirementsType
    settings: _Settings
    paths: _PathsType
    logger: _LoggerType
    johnson: _JohnsonType

    delta_time: float
    pelta_time: float

    PROJECT_NAME: str

    def getFps(self) -> float: ...
    def getCurrentScene(self) -> str: ...





class AbstractScene:
    def __init__(self, game: GameType):
        self.game = game

    def onUpdate(self):
        pass

    def onEvent(self, event):
        pass

    def onRender(self):
        self.game.request.setScreenColor(0, 0, 0)
    
    def onSave(self):
        pass

