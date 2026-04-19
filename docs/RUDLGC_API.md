



# API
self.game.api:

self.game.api.openUrl( url: str) - open browser url
self.game.api.closeGame( ) - close a game

self.game.api.setScreenColor( r: float, g: float, b: float) - set clear color
self.game.api.setWindowPosition( x: int, y: int) - set window position
self.game.api.setWindowTitle( title: str) - set window title
self.game.api.setWindowGrap( flag: bool) - set window grab
self.game.api.setWindowRelative( flag: bool) - set rel for mouse using in 3D

self.game.api.redirectScene( scene: str) - switching current scene to new
self.game.api.restartScene( ) - restart a current scene

self.game.api.updateSettings( ) - its not working yet

# SETTINGS

self.game.settings:

self.game.settings.DEBUG: bool

self.game.settings.WINDOW_WIDTH: int
self.game.settings.WINDOW_HEIGHT: int
self.game.settings.WINDOW_MINWIDTH: int
self.game.settings.WINDOW_MINHEIGHT: int

self.game.settings.VSYNC: int
self.game.settings.FULLSCREEN: bool
self.game.settings.BORDERLESS: bool
self.game.settings.RESIZABLE: bool

self.game.settings.FPS: float

self.game.settings.SHOW_FPS: bool
self.game.settings.SHOW_INFO: bool

self.game.settings.GAME_METADATA: _GameMetaType
self.game.settings.GAME_METADATA.APP_FOLDER: str
self.game.settings.GAME_METADATA.GAME_VERSION: str
self.game.settings.GAME_METADATA.GAME_TITLE: str
self.game.settings.GAME_METADATA.GAME_ICON: None|str
self.game.settings.GAME_DESCRIPTION: str
self.game.settings.GAME_METADATA.COMPANY: str
self.game.settings.GAME_METADATA.FILE_VERSION: str

self.game.settings.START_SCENE: str
self.game.settings.OS_PLATFORM: str
self.game.settings.GRAPHICS_API: str

self.game.settings.MUSIC_VOLUME: float
self.game.settings.SOUND_VOLUME: float

self.game.settings.POINT_SIZE: float
self.game.settings.LINE_SIZE: float



# LOGGER TRACE
self.game.logger:

self.game.logger.trace( message: str, as_error: bool=False) - print message in console as "[h:m:s]-[TRACE-USER]: {message}"
self.game.logger.traceMagenta( message: str) - also working but console color is peorple

# KEYBOARD AND MOUSE
self.game.keyboard:

self.game.keyboard.isPressed( key: int) -> bool  - return True if we press the Key

self.game.mouse:

self.game.mouse.isLeft( ) -> bool - return True if press left button
self.game.mouse.isMiddle( ) -> bool - return True if press middle button
self.game.mouse.isRight( ) -> bool - return True if press right button

self.game.mouse.getPos( ) -> tuple(x, y) - return current [X, Y] mouse cursor position
self.game.mouse.getRel( ) -> tuple(x, y) - return current [X, Y] mouse rel (Need for 3D games)


# PATHS 

self.game.paths:

self.game.paths.getConfigPath( *folder, file: str) -> str - return current path of PROJECT_NAME/.config
self.game.paths.getSavesPath( *folder, file: str) -> str - return current path of PROJECT_NAME/.saves
self.game.paths.getMusicsPath( *folder, file: str) -> str - return current path of PROJECT_NAME/musics
self.game.paths.getSoundsPath( *folder, file: str) -> str - return current path of PROJECT_NAME/sounds
self.game.paths.getAssetsPath( *folder, file: str) -> str - return current path of PROJECT_NAME/assets
self.game.paths.getFontsPath( *folder, file: str) -> str - return current path of PROJECT_NAME/fonts
self.game.paths.getShadersPath( *folder, file: str) -> str - return current path of PROJECT_NAME/shaders

# GAME ATTRIBUTES

self.game.delta_time: float - FPS time
self.game.tick_time: float - TPS time

self.game.PROJECT_NAME: str - your project name
self.game.ERROR: str - error message

self.game.getFps( ) -> float - return FPS
self.game.getCurrentScene( ) -> return current scene




# JOHNSON DATA

from rudlgc.johnson import Joshua, Xmlion

Joshua - for JSON:

.readData() -> dict - returns dict of data
.saveData(data: dict) - saves data to json file


Xmlion - for XML:
.readXml() -> dict - returns dict of data
.saveXml(data: dict) - saves data to xml file


//EXAMPLE:
my_data = Joshua(json_path: str)

//LOADING
my_data_read = my_data.readData()

//CHANGING
my_data_read["some-var"] = 10

//SAVING
my_data.saveData(my_data_read)


Xmlion also working as Joshua but with some attributes in dict

# RUDLUMS (RUDL ENUMS)

//WARNING THAT MODULE WILL BE DELETED AND WRITES INTO ENGINE CORE

from rudlgc.rudlums import Evalent, Keysym

Evalent - enums of Event

Evalent.KEY_DOWN - var

//EXAMPLE

def onEvent(self, event):
    if event.type == Evalent.KEY_DOWN:
        self.game.logger.trace("We pressed the key")


Keysym - enums of Keys Keyboard

Keysym.A - var

//EXAMPLE

if self.game.keyboard.isPressed(Keysym.A):
    self.game.logger.trace("We pressed Key A")






# CONTRIBUTION SCENE|GAMETYPE|ANOTATIONS

from rudlgc.contrib.package_type import AbstractScene, GameType
from rudlgc.contrib.package_scenes import SceneEmpty, SceneError
from rudlgc.contrib.package_model import SceneModel


AbstractScene - its interface to our scenes 

//EXAMPLE

class Menu(AbstractScene): ...

Btw its not neccesary you can not using them. Its need for anotation


GameType - game type anotation

Shows all variable, classes, methods.


SceneEmpty - game scene stubs

//EXAMPLE
self.registerScene('stub-scene', lambda: SceneEmpty(game=game, text_title: str="My empty scene", text_about_scene: str="Nothing...", scene_switching: str="example-scene"))

text_title - for window title
text_about_scene - text in game about future scene your dreams your notes
scene_switching - you can return to your scene


SceneError - game error scene

But you must register the engine build that scene to shows traceback error but you customizing them by inheritance

MyNewEmptyScene(SceneEmpty): ...
MyNewErrorScene(SceneError): ...

self.registerScene('error-scene', lambda: MyNewErrorScene(game=game)) - building core scene
