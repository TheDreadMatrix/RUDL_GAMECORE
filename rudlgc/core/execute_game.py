import warnings

warnings.filterwarnings("ignore", message="Using SDL2 binaries from pysdl2-dll*")

import os
import sys
import sdl2
import sdl2.ext
import json
import traceback
import xml.etree
import moderngl
import PIL
import glm
from pathlib import Path
from datetime import datetime
from importlib import import_module



class PathCore:
    def __init__(self):
        if hasattr(sys, "_MEIPASS"):
            self._RESOURCE_DIR = Path(sys._MEIPASS)
        else:
            self._RESOURCE_DIR = Path(__file__).resolve().parent
            

        self.datas_dir = ""
        self.musics_dir = self._RESOURCE_DIR / "musics"
        self.sounds_dir = self._RESOURCE_DIR / "sounds"
        self.assets_dir = self._RESOURCE_DIR / "assets"
        self.fonts_dir = self._RESOURCE_DIR / "fonts"
        self.shaders_dir = self._RESOURCE_DIR / "shaders"



class RequestCore:
    def __init__(self):
        pass

    def closeGame(self):
        pass

    def updateSettings(self):
        pass

    def redirectScene(self, scene):
        pass


class Requirements:
    def __init__(self):
        self.sdl2 = sdl2
        self.moderngl = moderngl
        self.pyglm = glm
        self.pillow = PIL
        



class SettingsCore:
    __DEFAULTS = {
        "DEBUG", "WINDOW_WIDTH", "WINDOW_HEIGHT",
        "WINDOW_MINWIDTH", "WINDOW_MINHEIGHT",
        "WINDOW_MAXWIDTH", "WINDOW_MAXHEIGHT",
        "GAME_NAME", "GAME_DESCRIPTION", "FILE_VERSION",
        "GAME_ICON","GAME_RIGHT", "GAME_VERSION", 
        "TITLE", "VSYNC", 
        "FULLSCREEN", "BORDERLESS", "RESIZABLE",
        "START_SCENE", "SHOW_FPS", "SHOW_INFO", "SHOW_PROMPT",
        "MUSIC_VOLUME", "SOUND_VOLUME",
        "FPS", "PPS",
        "POINT_SIZE", "LINE_SIZE",
        "SIX_SEVEN", "SIX_NINE", "POOR_NUMBER_68"
    }

    def __init__(self):
        self.__settings_module = import_module(os.getenv("RUDLGC_PROJECT_SETTINGS", "test.test_module"))

        self.VSYNC = getattr(self.__settings_module, "VSYNC", False)

        self.WINDOW_WIDTH = getattr(self.__settings_module, "WINDOW_WIDTH", 800)
        self.WINDOW_HEIGHT = getattr(self.__settings_module, "WINDOW_HEIGHT", 600)

        self.WINDOW_MINWIDTH = getattr(self.__settings_module, "WINDOW_MINWIDTH", 799)
        self.WINDOW_MINHEIGHT = getattr(self.__settings_module, "WINDOW_MINHEIGHT", 599)

        self.WINDOW_MAXWIDTH = getattr(self.__settings_module, "WINDOW_MAXWIDTH", None)
        self.WINDOW_MAXHEIGHT = getattr(self.__settings_module, "WINDOW_MAXHEIGHT", None)

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

        self.FPS = getattr(self.__settings_module, "FPS", 60)
        self.PPS = getattr(self.__settings_module, "PPS", 60)

        self.START_SCENE = getattr(self.__settings_module, "START_SCENE", "empty-rudlgc")
        self.SHOW_FPS = getattr(self.__settings_module, "SHOW_FPS", True)
        self.SHOW_INFO = getattr(self.__settings_module, "SHOW_INFO", True)
        self.SHOW_PROMPT = getattr(self.__settings_module, "SHOW_PROMPT", True)

        self.MUSIC_VOLUME = getattr(self.__settings_module, "MUSIC_VOLUME", 1.0)
        self.SOUND_VOLUME = getattr(self.__settings_module, "SOUND_VOLUME", 1.0)

        self.POINT_SIZE = getattr(self.__settings_module, "POINT_SIZE", 10)
        self.LINE_SIZE = getattr(self.__settings_module, "LINE_SIZE", 10)

        self.SIX_SEVEN = 67
        self.POOR_NUMBER_68 = 68
        self.SIX_NINE = 69

        for attr in dir(self.__settings_module):
            if attr not in SettingsCore.__DEFAULTS and not attr.startswith("__"):
                value = getattr(self.__settings_module, attr)
                setattr(self, attr, value)



class Johnson:
    pass

class Xmllion:
    pass


class Logger:
    COLORS = {
        "INFO": "\033[94m", 
        "WARNING": "\033[33m",
        "TRACE-USER": "\033[92m",
        "ERROR": "\033[91m",
        "RESET": "\033[0m"
    }
        
    @staticmethod
    def trace(message):
        now = datetime.now().strftime("%H:%M:%S")
        color = Logger.COLORS["TRACE-USER"]
        reset = Logger.COLORS["RESET"]
        print(f"{color}[{now}]-[TRACE-USER]: {message}{reset}")

    @staticmethod
    def _system_log(tag, message):
        now = datetime.now().strftime("%H:%M:%S")
        color = Logger.COLORS.get(tag, "")
        reset = Logger.COLORS["RESET"]
        print(f"{color}[{now}]-[{tag}]: {message}{reset}")




class Game:
    def __init__(self):
        sdl2.ext.init()
        self.settings = SettingsCore()

        self._running = True
        self.delta_time = 0
        self.pelta_time = 1 / self.settings.PPS
        self.scene = self.settings.START_SCENE

        self.paths = PathCore()
        self.logger = Logger()
        self.request = RequestCore()

        self.johnson = Johnson()
        self.xmllion = Xmllion()
        
        
        self.requirements = Requirements()


        if self.settings.SHOW_PROMPT:
            self.logger._system_log("INFO", "RUDL Game Core build with SDL2 && OpenGL 3.3.0")
        
        if self.settings.DEBUG:
            self.logger._system_log("WARNING", "DEBUG mode is enabled")
        


        sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_CONTEXT_MAJOR_VERSION, 3)
        sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_CONTEXT_MINOR_VERSION, 3)
        sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_CONTEXT_PROFILE_MASK, sdl2.SDL_GL_CONTEXT_PROFILE_CORE)
        sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_DOUBLEBUFFER, 1)
        

        self.__window = sdl2.ext.Window(self.settings.TITLE, size=(self.settings.WINDOW_WIDTH, self.settings.WINDOW_HEIGHT), flags=sdl2.SDL_WINDOW_OPENGL)
        self.__window.show()

        if self.settings.RESIZABLE:
            sdl2.SDL_SetWindowResizable(self.__window.window, sdl2.SDL_TRUE)

        if self.settings.FULLSCREEN:
            sdl2.SDL_SetWindowFullscreen(self.__window.window, sdl2.SDL_WINDOW_FULLSCREEN_DESKTOP)

        if self.settings.BORDERLESS:
            sdl2.SDL_SetWindowBordered(self.__window.window, sdl2.SDL_FALSE)

        sdl2.SDL_SetWindowMinimumSize(self.__window.window, self.settings.WINDOW_MINWIDTH, self.settings.WINDOW_MINHEIGHT)
        if self.settings.WINDOW_MAXWIDTH and self.settings.WINDOW_MAXHEIGHT:
            sdl2.SDL_SetWindowMaximumSize(self.__window.window, self.settings.WINDOW_MAXWIDTH, self.settings.WINDOW_MAXHEIGHT)

        self.__gl_context = sdl2.SDL_GL_CreateContext(self.__window.window)
        self._ctx = moderngl.create_context()

        

    
    def getFps(self): pass  
    def getCurrentScene(self): pass
    


    
    def __update(self): 
        for event in sdl2.ext.get_events():
            if event.type == sdl2.SDL_QUIT:
                self._running = False




    def __render(self):
        self._ctx.clear(0.8, 0.8, 0.8)

        sdl2.SDL_GL_SwapWindow(self.__window.window)


    def __run(self): 
        while self._running:
            self.__update()
            self.__render()


        if self.settings.SHOW_PROMPT:
            self.logger._system_log("INFO", "Game succesfully exit")
            

        sdl2.SDL_GL_DeleteContext(self.__gl_context)
        sdl2.SDL_DestroyWindow(self.__window.window)
        sdl2.ext.quit()
        

Game()._Game__run()