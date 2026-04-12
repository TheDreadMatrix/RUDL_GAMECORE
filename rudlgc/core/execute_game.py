import os
import sys
import sdl2
import sdl2.ext
import time
import json
import traceback
import xml.etree
import moderngl
import platformdirs
from pathlib import Path
from datetime import datetime
from importlib import import_module



class PathCore:
    def __init__(self, game: "Game"):
        PROJECT_DIR = game.PROJECT_NAME
        if hasattr(sys, "frozen"):
            self._BASE_DATA_DIR = Path(platformdirs.user_data_dir(game.settings.APPNAME))
        else:
            self._BASE_DATA_DIR = Path.cwd() / PROJECT_DIR

        if hasattr(sys, "_MEIPASS"):
            self._RESOURCE_DIR = Path(sys._MEIPASS)
        else:
            self._RESOURCE_DIR = Path.cwd() / PROJECT_DIR
            

        self.musics_dir = self._RESOURCE_DIR / "musics"
        self.sounds_dir = self._RESOURCE_DIR / "sounds"
        self.assets_dir = self._RESOURCE_DIR / "assets"
        self.fonts_dir = self._RESOURCE_DIR / "fonts"
        self.shaders_dir = self._RESOURCE_DIR / "shaders"

        self.config_dir = self._BASE_DATA_DIR / ".config"
        self.saves_dir = self._BASE_DATA_DIR / ".saves"

    def _build_path(self, base: Path, *folders, file: str | None = None):
        path = base
        for f in folders:
            path = path / f

        if file:
            path = path / file
        
        if not path.exists():
            raise FileExistsError(f"Path not found: '{str(path)}'")
        return str(path)

    def getConfigPath(self, *folder, file):
        return self._build_path(self.config_dir, *folder, file=file)

    def getSavesPath(self, *folder, file):
        return self._build_path(self.saves_dir, *folder, file=file)

    def getMusicsPath(self, *folder, file):
        return self._build_path(self.musics_dir, *folder, file=file)

    def getSoundsPath(self, *folder, file):
        return self._build_path(self.sounds_dir, *folder, file=file)

    def getAssetsPath(self, *folder, file):
        return self._build_path(self.assets_dir, *folder, file=file)

    def getFontsPath(self, *folder, file):
        return self._build_path(self.fonts_dir, *folder, file=file)

    def getShadersPath(self, *folder, file):
        return self._build_path(self.shaders_dir, *folder, file=file)





class SettingsCore:
    _DEFAULTS = {
        "DEBUG", 
        "WINDOW_WIDTH", "WINDOW_HEIGHT", "WINDOW_MINWIDTH", "WINDOW_MINHEIGHT",
        "APPNAME", "GAME_NAME", "GAME_DESCRIPTION", "FILE_VERSION", "GAME_ICON", "GAME_RIGHT", "GAME_VERSION", "TITLE", 
        "VSYNC", "FULLSCREEN", "BORDERLESS", "RESIZABLE",
        "START_SCENE", "SHOW_FPS", "SHOW_INFO",
        "MUSIC_VOLUME", "SOUND_VOLUME",
        "FPS", "PPS",
        "POINT_SIZE", "LINE_SIZE",
        "SIX_SEVEN", "SIX_NINE", "POOR_NUMBER_68"
    }

    def __init__(self, game: "Game"):
        try: 
            self.__settings_module = import_module(os.getenv("RUDLGC_PROJECT_SETTINGS", ""))
        except ModuleNotFoundError:
            game.logger._system_log("ERROR", traceback.format_exc())
            game.logger._system_log("ERROR", "Game failure exit")
            exit(1)

        self.VSYNC = getattr(self.__settings_module, "VSYNC", False)
        self.APPNAME = getattr(self.__settings_module, "APPNAME", ".rudlgcGameData")

        self.WINDOW_WIDTH = getattr(self.__settings_module, "WINDOW_WIDTH", 800)
        self.WINDOW_HEIGHT = getattr(self.__settings_module, "WINDOW_HEIGHT", 600)

        self.WINDOW_MINWIDTH = getattr(self.__settings_module, "WINDOW_MINWIDTH", 799)
        self.WINDOW_MINHEIGHT = getattr(self.__settings_module, "WINDOW_MINHEIGHT", 599)

        self.FULLSCREEN = getattr(self.__settings_module, "FULLSCREEN", False)
        self.BORDERLESS = getattr(self.__settings_module, "BORDERLESS", False)
        self.RESIZABLE = getattr(self.__settings_module, "RESIZABLE", False)

        self.GAME_NAME = getattr(self.__settings_module, "GAME_NAME", "RUDLGC game!!!")
        self.GAME_DESCRIPTION = getattr(self.__settings_module, "GAME_DESCRIPTION", "RUDL Game Core Engine!!!")
        self.GAME_VERSION = getattr(self.__settings_module, "GAME_VERSION", "0.1.0")

        self.GAME_RIGHT = getattr(self.__settings_module, "GAME_RIGHT", "NONE")
        self.FILE_VERSION = getattr(self.__settings_module, "PRODUCT_VERSION", "1.0.0.0")

        self.TITLE = getattr(self.__settings_module, "TITLE", "RUDLGC window")
        self.DEBUG = getattr(self.__settings_module, "DEBUG", True)

        self.FPS = getattr(self.__settings_module, "FPS", 240)
        self.PPS = getattr(self.__settings_module, "PPS", 240)

        self.START_SCENE = getattr(self.__settings_module, "START_SCENE", "empty-rudlgc")
        self.SHOW_FPS = getattr(self.__settings_module, "SHOW_FPS", True)
        self.SHOW_INFO = getattr(self.__settings_module, "SHOW_INFO", True)

        self.MUSIC_VOLUME = getattr(self.__settings_module, "MUSIC_VOLUME", 1.0)
        self.SOUND_VOLUME = getattr(self.__settings_module, "SOUND_VOLUME", 1.0)

        self.POINT_SIZE = getattr(self.__settings_module, "POINT_SIZE", 10)
        self.LINE_SIZE = getattr(self.__settings_module, "LINE_SIZE", 10)

        self.SIX_SEVEN = 67
        self.POOR_NUMBER_68 = 68
        self.SIX_NINE = 69

        for attr in dir(self.__settings_module):
            if attr not in SettingsCore._DEFAULTS and not attr.startswith("__") and attr.isupper():
                value = getattr(self.__settings_module, attr)
                setattr(self, attr, value)



class Logger:
    COLORS = {
        "INFO": "\033[94m", 
        "WARNING": "\033[33m",
        "MAGENTA": "\033[35m",
        "TRACE-USER": "\033[92m",
        "ERROR": "\033[91m",
        "RESET": "\033[0m"
    }
        
    @staticmethod
    def trace(message, as_error=False):
        now = datetime.now().strftime("%H:%M:%S")
        color = Logger.COLORS["TRACE-USER"] if not as_error else Logger.COLORS["ERROR"]
        reset = Logger.COLORS["RESET"]
        print(f"{color}[{now}]-[TRACE-USER]: {message}{reset}")

    @staticmethod
    def traceMagenta(message):
        now = datetime.now().strftime("%H:%M:%S")
        color = Logger.COLORS["MAGENTA"]
        reset = Logger.COLORS["RESET"]
        print(f"{color}[{now}]-[MAGENTA]: {message}{reset}")

    @staticmethod
    def _system_log(tag, message):
        now = datetime.now().strftime("%H:%M:%S")
        color = Logger.COLORS.get(tag, "")
        reset = Logger.COLORS["RESET"]
        print(f"{color}[{now}]-[{tag}]: {message}{reset}")




class RequestCore:
    def __init__(self, game: "Game"):
        self.game = game

    def closeGame(self):
        self.game._running = False

    def updateSettings(self):
        pass

    def redirectScene(self, scene):
        self.game._current_scene_name = scene

    def restartScene(self):
        self.game._scene_router._restartScene()

    def setScreenColor(self, r, g, b):
        self.game._screen_color = (r, g, b)

    def setWindowPosition(self, x, y):
        self.game._window.position = (x, y)

    def setWindowTitle(self, title):
        self.game._window.title = title

    def setWindowSize(self, w, h):
        self.game._window.size = (w, h)
        







class Game:
    def __init__(self):
        sdl2.ext.init()
        self.PROJECT_NAME = os.environ.get("RUDLGC_PROJECT_NAME", "NOT_FOUND")
        self.ERROR = ""

        self.logger = Logger()
        self.settings = SettingsCore(self)

        #PRIVATE PROTECTED
        self._running = True
        self._current_scene_name = self.settings.START_SCENE
        self._screen_color = (0.8, 0.8, 0.8)

        self._last_time = time.perf_counter()
        self._fps = 0.0
        self._frame_count = 0
        self._fps_timer = 0.0
        self._target_fps = self.settings.FPS


        #FREE TO USE
        self.delta_time = 0
        self.pelta_time = 1 / self.settings.PPS

        self.paths = PathCore(self)
        self.request = RequestCore(self)
                
        if self.settings.DEBUG:
            self.logger._system_log("WARNING", "DEBUG mode is enabled")
        self.logger._system_log("INFO", "RUDL Game Core build with SDL2 && OpenGL 3.3.0")
        

        #SETTINGS OF THE WINDOW AND CONTEXT
        sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_CONTEXT_MAJOR_VERSION, 3)
        sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_CONTEXT_MINOR_VERSION, 3)
        sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_CONTEXT_PROFILE_MASK, sdl2.SDL_GL_CONTEXT_PROFILE_CORE)
        sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_MULTISAMPLEBUFFERS, 1)
        sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_MULTISAMPLESAMPLES, 4) 
        sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_DOUBLEBUFFER, 1)
        

        flags = sdl2.SDL_WINDOW_OPENGL
        if self.settings.RESIZABLE:
            flags |= sdl2.SDL_WINDOW_RESIZABLE
        if self.settings.BORDERLESS:
            flags |= sdl2.SDL_WINDOW_BORDERLESS
        if self.settings.FULLSCREEN:
            flags |= sdl2.SDL_WINDOW_FULLSCREEN_DESKTOP
        
        
        self._window = sdl2.ext.Window(self.settings.TITLE, size=(self.settings.WINDOW_WIDTH, self.settings.WINDOW_HEIGHT), flags=flags)
        sdl2.SDL_SetWindowMinimumSize(self._window.window, self.settings.WINDOW_MINWIDTH, self.settings.WINDOW_MINHEIGHT)
        

        self.__gl_context = sdl2.SDL_GL_CreateContext(self._window.window)
        self._ctx = moderngl.create_context()
        self._ctx.viewport = (0, 0, self.settings.WINDOW_WIDTH, self.settings.WINDOW_HEIGHT)
        self._ctx.enable(moderngl.DEPTH_TEST)
        self._ctx.enable(moderngl.BLEND)
        self._ctx.blend_func = (moderngl.SRC_ALPHA, moderngl.ONE_MINUS_SRC_ALPHA)
        self._ctx.point_size = self.settings.POINT_SIZE
        self._ctx.line_width = self.settings.LINE_SIZE

        sdl2.SDL_GL_SetSwapInterval(self.settings.VSYNC) 
        self._window.show()

        #SCENE ROUTER FOR SCENE MANAGMENT
        try:
            module = import_module(f"{self.PROJECT_NAME}.router")
        except ModuleNotFoundError:
            self.logger._system_log("ERROR", traceback.format_exc())
            self.logger._system_log("ERROR", "Game failure exit")
            exit(1)


        if not hasattr(module, "SceneManager"):
            self.logger._system_log("ERROR", f"Can not found 'SceneManager' from {self.PROJECT_NAME}/router.py ")
            self.logger._system_log("ERROR", "Game failure exit")
            exit(1)

        try:
            self._scene_router = module.SceneManager(self, "HERE THIS YOU CAN REGISTER YOUR SCENES LOL!!!")
        except Exception:
            self.logger._system_log("ERROR", f"You got error in {self.PROJECT_NAME}/router.py.")
            self.logger._system_log("ERROR", traceback.format_exc())
            self.logger._system_log("ERROR", "Game failure exit")
            exit(1)

    
        self.keyboard = None
        self.mouse = None
        

        

    
    def getFps(self): return self._fps
    def getCurrentScene(self): return self._current_scene_name


    def __limit_fps(self, frame_start):
        if self._target_fps <= 0:
            return

        target_frame_time = 1.0 / self._target_fps

        frame_end = time.perf_counter()
        frame_duration = frame_end - frame_start

        sleep_time = target_frame_time - frame_duration

        if sleep_time > 0:
            time.sleep(sleep_time)
    


    
    def __update(self): 
        self._scene_router._update()

        for event in sdl2.ext.get_events():
            if event.type == sdl2.SDL_QUIT:
                self._running = False
            self._scene_router._event(event)


    def __render(self):
        self._ctx.clear(self._screen_color[0], self._screen_color[1], self._screen_color[2])
        self._scene_router._render()
        sdl2.SDL_GL_SwapWindow(self._window.window)


    def __run(self): 
        while self._running:
            frame_start = time.perf_counter()
            
            self.delta_time = frame_start - self._last_time
            self._last_time = frame_start

            if self.delta_time > 0:
                self._fps = 1.0 / self.delta_time


            try:
                self.__update()
                self.__render()
            except Exception:
                error_message = traceback.format_exc()
                self.ERROR = error_message
                self.request.redirectScene("error-scene")
                self._scene_router.onException(error_message)
            
            self.__limit_fps(frame_start)


        self._scene_router.savingProgress()

        sdl2.SDL_GL_DeleteContext(self.__gl_context)
        sdl2.SDL_DestroyWindow(self._window.window)
        sdl2.ext.quit()

        self.logger._system_log("INFO" if not self.ERROR else "ERROR", "Game succesfully exit" if not self.ERROR else "Game failure exit 2")
        

if __name__ == "__main__":
    Game()._Game__run()