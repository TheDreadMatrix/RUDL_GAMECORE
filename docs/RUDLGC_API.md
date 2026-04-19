# RUDLGC API

# SETTINGS

self.game.settings || self.settings ::
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

    GAME_METADATA: _GameMetaType ::

        GAME_METADATA.APP_FOLDER: str
        GAME_METADATA.META: dict
        GAME_METADATA.ICON: str
        GAME_METADATA.META.GAME_TITLE: str
        GAME_METADATA.META.GAME_VERSION: str
        GAME_METADATA.META.GAME_DESCRIPTION: str
        GAME_METADATA.META.FILE_VERSION: str
        GAME_METADATA.META.COMPANY: str

    START_SCENE: str
    OS_PLATFORM: str
    GRAPHICS_API: str

    MUSIC_VOLUME: float
    SOUND_VOLUME: float

    POINT_SIZE: float
    LINE_SIZE: float


# API

self.game.api || self.api ::

    def closeGame(self) -> None: ...  \\Closes a game

    def updateSettings(self) -> None: ...  \\Not working

    def redirectScene(self, scene: str) -> None: ...  \\Switching the scene.
    def restartScene(self) -> None: ...                \\Restart the current scene

    def openUrl(self, url: str) -> None: ...            \\Open url in your browser
    def chooseFile(self, message: str) -> str: ...      \\Dialog file

    def isMinimilized(self, event) -> bool: ...         \\Is window minimilized?
    def isMaximilized(self, event) -> bool: ...         \\Is window maximilized?
    def isRestored(self, event) -> bool: ...            \\Is window restored?
    def isResized(self, event) -> bool: ...             \\Is window resized?
    def isFocusLost(self, event) -> bool: ...           \\Is window unfocused now?
    def isFocusGain(self, event) -> bool: ...           \\Is window focused now?

    def createMessageBox(self, title: str, info: str, type_messagebox: int=0) -> None: ...   \\Creates small window
    def setScreenColor(self, r: float, g: float, b: float) -> None: ...                       \\Clear screen color
    def setWindowPosition(self, x: int, y: int) -> None: ...                                   \\Set Window position
    def setWindowSize(self, w: int, h: int) -> None: ...                                        \\Set Window size
    def setWindowTitle(self, title: str) -> None: ...                                            \\Set Window title
    def setWindowGrab(self, flag: bool) -> None: ...                                              \\Set Window grap mouse event flag
    def setWindowRelative(self, flag: bool) -> None: ...                                           \\Set Window mouse relative pos flag


# PATHS

self.game.paths || self.paths ::

    def getConfigPath(self, *folder: str, file: str) -> str: ...      \\Path for .config/
    def getSavesPath(self, *folder: str, file: str) -> str: ...        \\Path for .saves/
    def getMusicsPath(self, *folder: str, file: str) -> str: ...        \\Path for musics/
    def getSoundsPath(self, *folder: str, file: str) -> str: ...         \\Path for sounds/
    def getAssetsPath(self, *folder: str, file: str) -> str: ...          \\Path for assets/
    def getFontsPath(self, *folder: str, file: str) -> str: ...            \\Path for fonts/
    def getShadersPath(self, *folder: str, file: str) -> str: ...           \\Path for shaders/


# LOGGER

self.game.logger || self.logger ::

    
    def trace(message: str, as_error: bool=False) -> None: ...              \\Print message like '[h:m:s]-[TRACE-USER]: {message}'
    def traceMagenta(message: str) -> None: ...                              \\Also works but message is peorple


# MOUSE

self.game.mouse || self.mouse ::

    def mouseEnter(self, event) -> bool: ...                            \\True if mouse enters into window
    def mouseLeave(self, event) -> bool: ...                             \\True if mouse leaves from window
    def mouseButtonDown(self, button: int, event) -> bool: ...            \\If button its down by [LEFT, MIDDLE, RIGHT]
    def mouseButtonUp(self, button: int, event) -> bool: ...               \\Also works but realese

    def isLeft(self) -> bool: ...                                       \\Is mouse pressed left button
    def isMiddle(self) -> bool: ...                                      \\Is mouse pressed middle button
    def isRight(self) -> bool: ...                                        \\Is mouse pressed right button

    def getPos(self) -> tuple[float, float]: ...                            \\Get current cursor pos
    def getRel(self) -> tuple[float, float]: ...                             \\Get current rel cursor
    def getWheel(self) -> float: ...                                          \\Get current wheel by middle 


# KEYBOARD

self.game.keyboard || self.keyboard ::

    def isPressDown(self, key: int, event) -> bool: ...                 \\Is keyboard pressed down
    def isPressUp(self, key: int, event) -> bool: ...                    \\Is keyboard pressed up
    def isPress(self, key: int) -> bool: ...                              \\Is keyboard also pressed


# GAMEPAD

BUT ITS NOT WORKING YET....



# GAME ATTRIBUTES AND METHODS

self.game ::

    delta_time: float
    tick_time: float

    PROJECT_NAME: str
    ERROR: str

    def getFps(self) -> float: ...                  \\Shows current FPS
    def getTps(self) -> float: ...                   \\Shows current TPS
    def getCurrentScene(self) -> str: ...             \\Shows current scene



# IMPORTS

rudlgc.johnson ::

    Joshua -> JSON
    Xmlion -> Xmlion