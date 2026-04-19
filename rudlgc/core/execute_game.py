import os
import sdl2
import sdl2.ext
import time
import traceback
import moderngl
from importlib import import_module




from rudlgc.core.subsystems import Logger, _callOnce
from rudlgc.core.subsystems import RequestCore
from rudlgc.core.subsystems import SettingsCore
from rudlgc.core.subsystems import PathCore


class Requirements:
    mgl = moderngl
    sdl = sdl2
    pillow = __import__("PIL")
    glm5 = __import__("glm")


class Gamepad:
    def __init__(self):
        pass




class Keyboard:
    def __init__(self):
        self.keys = None

    def updateThis(self):
        self.keys = sdl2.SDL_GetKeyboardState(None)


    def isPressDown(self, key, event):
        if event.type == sdl2.SDL_KEYDOWN and event.key.repeat == 0:
            return event.key.keysym.scancode == key

    def isPressUp(self, key, event):
        if event.type == sdl2.SDL_KEYUP and event.key.repeat == 0:
            return event.key.keysym.scancode == key

    def isPress(self, key): return self.keys[key]


class Mouse:
    def __init__(self):
        self.pos_x, self.pos_y = sdl2.c_int(), sdl2.c_int()
        self.rel_x, self.rel_y = 0, 0
        self.wheel_x, self.wheel_y = 0, 0
        self.buttons = None

    def updateThis(self): self.buttons = sdl2.SDL_GetMouseState(self.pos_x, self.pos_y)

    def eventThis(self, event):
        if event.type == sdl2.SDL_MOUSEMOTION:
            self.rel_x, self.rel_y = event.motion.xrel, event.motion.yrel

        if event.type == sdl2.SDL_MOUSEWHEEL:
            self.wheel_x, self.wheel_y = event.wheel.x, event.wheel.y


    def mouseEnter(self, event):
        if event.type == sdl2.SDL_WINDOWEVENT:
            return event.window.event == sdl2.SDL_WINDOWEVENT_ENTER
        return False

    def mouseLeave(self, event):
        if event.type == sdl2.SDL_WINDOWEVENT:
            return event.window.event == sdl2.SDL_WINDOWEVENT_LEAVE
        return False


    def isLeft(self): return self.buttons & sdl2.SDL_BUTTON(sdl2.SDL_BUTTON_LEFT)
    
    def isMiddle(self): return self.buttons & sdl2.SDL_BUTTON(sdl2.SDL_BUTTON_MIDDLE)
    
    def isRight(self): return self.buttons & sdl2.SDL_BUTTON(sdl2.SDL_BUTTON_RIGHT)
    
    def getPos(self): return (self.pos_x.value, self.pos_y.value)
    
    def getRel(self): return (self.rel_x, self.rel_y)

    def getWheel(self): return (self.wheel_x, self.wheel_y)






class Game:
    def __init__(self):
        sdl2.SDL_Init(sdl2.SDL_INIT_VIDEO | sdl2.SDL_INIT_GAMECONTROLLER)
    
        #FREE TO USE
        self.PROJECT_NAME = os.environ.get("RUDLGC_PROJECT_NAME", "NOT_FOUND")
        self.ERROR = ""

        self.paths = PathCore(self)
        self.api = RequestCore(self)
        self.logger = Logger()
        self.settings = SettingsCore(self)

        self.keyboard = Keyboard()
        self.mouse = Mouse()

        self.delta_time = 0
        self.tick_time = 1 / self.settings.FPS

        #PRIVATE PROTECTED
        self._requirements = Requirements()
        self._running = True
        self._current_scene_name = self.settings.START_SCENE
        self._screen_color = (0.8, 0.8, 0.8)

        self._last_time = time.perf_counter()
        self._fps = 0.0
        self._frame_count = 0
        self._fps_timer = 0.0
        self._target_fps = self.settings.FPS
        self._accumulator = 0

        
        #SETTINGS OF THE WINDOW AND CONTEXT
        if self.settings.DEBUG:
            self.logger._system_log("WARNING", "DEBUG mode is enabled")
        
        if self.settings.GRAPHICS_API == "OPENGL":
            self.logger._system_log("WARNING", "Created OpenGL context")
            sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_CONTEXT_PROFILE_MASK, sdl2.SDL_GL_CONTEXT_PROFILE_CORE)
            sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_CONTEXT_MAJOR_VERSION, 3)
            sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_CONTEXT_MINOR_VERSION, 3)
        elif self.settings.GRAPHICS_API == "OPENGL_ES":
            self.logger._system_log("WARNING", "Created OpenGL ES context")
            sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_CONTEXT_PROFILE_MASK,  sdl2.SDL_GL_CONTEXT_PROFILE_ES)
            sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_CONTEXT_MAJOR_VERSION, 3)
            sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_CONTEXT_MINOR_VERSION, 0)

        sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_MULTISAMPLEBUFFERS, 1)
        sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_MULTISAMPLESAMPLES, 4) 
        sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_DEPTH_SIZE, 24)
        sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_ALPHA_SIZE, 8)
        sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_DOUBLEBUFFER, 1)
        

        flags = sdl2.SDL_WINDOW_OPENGL
        if self.settings.RESIZABLE:
            flags |= sdl2.SDL_WINDOW_RESIZABLE
        if self.settings.BORDERLESS:
            flags |= sdl2.SDL_WINDOW_BORDERLESS
        if self.settings.FULLSCREEN:
            flags |= sdl2.SDL_WINDOW_FULLSCREEN_DESKTOP
        
        
        self._window = sdl2.ext.Window(self.settings.GAME_METADATA.META.GAME_TITLE, 
                                       size=(self.settings.WINDOW_WIDTH, self.settings.WINDOW_HEIGHT), 
                                       position=(sdl2.SDL_WINDOWPOS_CENTERED, sdl2.SDL_WINDOWPOS_CENTERED),
                                       flags=flags)
        

        sdl2.SDL_SetWindowMinimumSize(self._window.window, self.settings.WINDOW_MINWIDTH, self.settings.WINDOW_MINHEIGHT)
        self._window.show()
        

        # GPU CONTEXT
        sdl2.SDL_GL_CreateContext(self._window.window)

        self._ctx = moderngl.create_context()
        self._ctx.viewport = (0, 0, self.settings.WINDOW_WIDTH, self.settings.WINDOW_HEIGHT)
        self._ctx.enable(moderngl.DEPTH_TEST)
        self._ctx.enable(moderngl.BLEND)
        self._ctx.blend_func = (moderngl.SRC_ALPHA, moderngl.ONE_MINUS_SRC_ALPHA)
        self._ctx.point_size = self.settings.POINT_SIZE
        self._ctx.line_width = self.settings.LINE_SIZE
    

        sdl2.SDL_GL_SetSwapInterval(self.settings.VSYNC) 
        

        #SCENE ROUTER FOR SCENE MANAGMENT
        self.logger._system_log("INFO", "RUDL Game Core build with SDL2 && OpenGL 3.3.0")
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
        except Exception:
            self.logger._system_log("ERROR", f"You got error in {self.PROJECT_NAME}/router.py.")
            self.logger._system_log("ERROR", traceback.format_exc())
            self.logger._system_log("ERROR", "Game failure exit")
            exit(1)    

        

        

    
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
        self.keyboard.updateThis() 
        self.mouse.updateThis()

        self._accumulator += self.delta_time
        self._scene_router._update()

        while self._accumulator >= self.tick_time:
            self._scene_router._updateFixed()
            self._accumulator -= self.tick_time

        for event in sdl2.ext.get_events():
            if event.type == sdl2.SDL_QUIT:
                self._running = False
            
            self.mouse.eventThis(event)

            self._scene_router._event(event)


    def __render(self):
        self._ctx.clear(self._screen_color[0], self._screen_color[1], self._screen_color[2])
        self._scene_router._render()
        sdl2.SDL_GL_SwapWindow(self._window.window)


    @_callOnce("It is strictly forbidden to call private functions and methods.")
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
                self.api.redirectScene("error-scene")
                self._scene_router.onException(error_message)
            
            self.__limit_fps(frame_start)

            


        self._scene_router.savingProgress()

        sdl2.ext.quit()

        self.logger._system_log("INFO" if not self.ERROR else "ERROR", "Game succesfully exit" if not self.ERROR else "Game failure exit 2")
        
        

if __name__ == "__main__":
    Game()._run()