import os
import sdl2
import sdl2.ext
import time
import traceback
from importlib import import_module




from rudlgc.core.subsystems import Logger
from rudlgc.core.subsystems import (GameConfigApi, WindowApi, EventApi, SystemApi)

from rudlgc.core.subsystems import SettingsCore
from rudlgc.core.subsystems import PathCore

from rudlgc.core.subsystems.input_game import Keyboard, Mouse, Gamepad, Touchpad

from rudlgc.core.resources_items import ResourcesItems
from rudlgc.core import _callOnce, _getOs


_BACKEND_CLASS = None
_OS = _getOs()
if _OS in ["WINDOWS", "LINUX"]:
    from rudlgc.core.backends.opengl import OpenGLBackend
    _BACKEND_CLASS = OpenGLBackend
elif _OS in ["MACOS", "IOS"]:
    _BACKEND_CLASS = "SomeMetalBackend"
elif _OS == "ANDROID":
    _BACKEND_CLASS = "SomeOpenGLesBackend"



class Requirements:
    def __init__(self, logger):
        self.os = _getOs()
        self.logger = logger
        
        self.mgl = None
        self.glm = None
        self.pil = None
        self.sdl = None

        self._loadImports()

   
    def _safeImport(self, name):
        try:
            return import_module(name)
        except Exception as e:
            self.logger._system_log("ERROR", f"[WARN] Cannot import {name}: {e}")
            return None
        
    def _loadImports(self):
        self.pil = self._safeImport("PIL.Image")
        self.glm5 = self._safeImport("glm")
        self.sdl = self._safeImport("sdl2")
        
        
        if self.os in ("WINDOWS", "LINUX"):
            self.mgl = self._safeImport("moderngl")
            
        elif self.os == "ANDROID":
            self.mgl = None

        else:
            self.logger._system_log("ERROR", f"Can not work with systems: {self.os}")











class Game:
    def __init__(self):
        sdl2.SDL_Init(sdl2.SDL_INIT_VIDEO | sdl2.SDL_INIT_AUDIO)
    
        #FREE TO USE
        self.PROJECT_NAME = os.environ.get("RUDLGC_PROJECT_NAME", "NOT_FOUND")
        self.ERROR = ""

        self.paths = PathCore(self)
        self.logger = Logger()
        self.settings = SettingsCore(self)

        self.keyboard = Keyboard()
        self.mouse = Mouse()
        self.gamepad = Gamepad()
        self.touchpad = Touchpad()

        self.delta_time = 0
        self.tick_time = 1 / 60

        #PRIVATE PROTECTED
        self._requirements = Requirements(self.logger)
        self._running = True
        self._current_scene_name = "empty-scene"
        

        self._last_time = time.perf_counter()
        self._fps = 0.0
        self._tps = 0.0
        self._tick_count = 0
        self._tick_timer = 0.0
        self._frame_count = 0
        self._fps_timer = 0.0
        self._target_fps = self.settings.FPS
        self._accumulator = 0

        
        #SETTINGS OF THE WINDOW AND CONTEXT
        self.backend_render = _BACKEND_CLASS(self)
        self.backend_render.createVersion()

        self._window = sdl2.ext.Window(self.settings.GAME_METADATA.META.GAME_TITLE, 
                                       size=(self.settings.WINDOW_WIDTH, self.settings.WINDOW_HEIGHT), 
                                       position=(sdl2.SDL_WINDOWPOS_CENTERED, sdl2.SDL_WINDOWPOS_CENTERED),
                                       flags=self.backend_render.createFlags())
        

        sdl2.SDL_SetWindowMinimumSize(self._window.window, self.settings.WINDOW_MINWIDTH, self.settings.WINDOW_MINHEIGHT)
        self._window.show()
        
        # GPU CONTEXT
        self.backend_render.createContext()
        self.backend_render.setPointSize(self.settings.POINT_SIZE)
        self.backend_render.setLineWidth(self.settings.LINE_SIZE)

        self.backend_render.setViewPort(self.settings.WINDOW_WIDTH, self.settings.WINDOW_HEIGHT)
        self.backend_render.setProjectile2D(self.settings.WINDOW_WIDTH, self.settings.WINDOW_HEIGHT)



    @_callOnce()
    def _connectDebugServer(self):
        self.logger._system_log("WARNING", "Connected to Debug Server")
        
        
    @_callOnce()
    def _initGame(self):
        self.resources = ResourcesItems(self)
        self.window_api = WindowApi(self)
        self.event_api = EventApi(self)
        self.config_api = GameConfigApi(self)
        self.system_api = SystemApi(self)

        
        

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
            self._scene_router = module.SceneManager(self)
            self._scene_router.onRegistration(self)
            self._scene_router._startGameLoop()
        except Exception:
            self.logger._system_log("ERROR", f"You got error in {self.PROJECT_NAME}/router.py.")
            self.logger._system_log("ERROR", traceback.format_exc())
            self.logger._system_log("ERROR", "Game failure exit")
            exit(1)    

        self.logger._system_log("INFO", "RUDL Game Core build with SDL2 && OpenGL 3.3.0")

        

    
    def getFps(self): return self._fps
    def getTps(self): return self._tps
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
        self.keyboard.updateThis() 
        self.mouse.updateThis()

        self._accumulator += self.delta_time
        self._scene_router._update()

        while self._accumulator >= self.tick_time:
            self._scene_router._updateFixed()
            self._accumulator -= self.tick_time

            self._tick_count += 1

        for event in sdl2.ext.get_events():
            if event.type == sdl2.SDL_QUIT:
                self._running = False
            
            if event.type == sdl2.SDL_WINDOWEVENT and event.window.event == sdl2.SDL_WINDOWEVENT_RESIZED:
                self.settings.WINDOW_WIDTH = event.window.data1
                self.settings.WINDOW_HEIGHT = event.window.data2

                self.backend_render.setViewPort(self.settings.WINDOW_WIDTH, self.settings.WINDOW_HEIGHT)
                self.backend_render.setProjectile2D(self.settings.WINDOW_WIDTH, self.settings.WINDOW_HEIGHT)


            self.mouse.eventThis(event)
            self._scene_router._event(event)

        self._tick_timer += self.delta_time
        if self._tick_timer >= 1.0:
            self._tps = self._tick_count
            self._tick_count = 0
            self._tick_timer = 0.0


    def __render(self):
        self.backend_render.clearColor(0.9, 0.9, 0.9)
        self._scene_router._render()
        sdl2.SDL_GL_SwapWindow(self._window.window)


    @_callOnce()
    def _run(self): 
        frame_start = time.perf_counter()
        while self._running:
            frame_start = time.perf_counter()
            
            self.delta_time = min(frame_start - self._last_time, 0.02)
            self._last_time = frame_start

            if self.delta_time > 0:
                self._fps = 1.0 / self.delta_time

            try:
                self.__update()  
                self.__render()
            except Exception:
                error_message = traceback.format_exc()
                self.ERROR = error_message if self.settings.DEBUG else "Oops...! You catched an error!!!"
                self.config_api.redirectScene("error-scene")
                self._scene_router.onException(error_message)
            
            self.__limit_fps(frame_start)

            


        self._scene_router.savingProgress()

        sdl2.ext.quit()
        self.logger._system_log("INFO" if not self.ERROR else "ERROR", "Game succesfully exit" if not self.ERROR else "Game failure exit 2")
        
        

if __name__ == "__main__":
    Game()._run()