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
    NOT_WORKING = 0




class Keyboard:
    def __init__(self):
        self.keys = None
        self.__dict_keynums = {
            # Letters (0–25)
            0: sdl2.SDL_SCANCODE_A,
            1: sdl2.SDL_SCANCODE_B,
            2: sdl2.SDL_SCANCODE_C,
            3: sdl2.SDL_SCANCODE_D,
            4: sdl2.SDL_SCANCODE_E,
            5: sdl2.SDL_SCANCODE_F,
            6: sdl2.SDL_SCANCODE_G,
            7: sdl2.SDL_SCANCODE_H,
            8: sdl2.SDL_SCANCODE_I,
            9: sdl2.SDL_SCANCODE_J,
            10: sdl2.SDL_SCANCODE_K,
            11: sdl2.SDL_SCANCODE_L,
            12: sdl2.SDL_SCANCODE_M,
            13: sdl2.SDL_SCANCODE_N,
            14: sdl2.SDL_SCANCODE_O,
            15: sdl2.SDL_SCANCODE_P,
            16: sdl2.SDL_SCANCODE_Q,
            17: sdl2.SDL_SCANCODE_R,
            18: sdl2.SDL_SCANCODE_S,
            19: sdl2.SDL_SCANCODE_T,
            20: sdl2.SDL_SCANCODE_U,
            21: sdl2.SDL_SCANCODE_V,
            22: sdl2.SDL_SCANCODE_W,
            23: sdl2.SDL_SCANCODE_X,
            24: sdl2.SDL_SCANCODE_Y,
            25: sdl2.SDL_SCANCODE_Z,

            # Top numbers
            30: sdl2.SDL_SCANCODE_0,
            31: sdl2.SDL_SCANCODE_1,
            32: sdl2.SDL_SCANCODE_2,
            33: sdl2.SDL_SCANCODE_3,
            34: sdl2.SDL_SCANCODE_4,
            35: sdl2.SDL_SCANCODE_5,
            36: sdl2.SDL_SCANCODE_6,
            37: sdl2.SDL_SCANCODE_7,
            38: sdl2.SDL_SCANCODE_8,
            39: sdl2.SDL_SCANCODE_9,

            # Numpad
            40: sdl2.SDL_SCANCODE_KP_0,
            41: sdl2.SDL_SCANCODE_KP_1,
            42: sdl2.SDL_SCANCODE_KP_2,
            43: sdl2.SDL_SCANCODE_KP_3,
            44: sdl2.SDL_SCANCODE_KP_4,
            45: sdl2.SDL_SCANCODE_KP_5,
            46: sdl2.SDL_SCANCODE_KP_6,
            47: sdl2.SDL_SCANCODE_KP_7,
            48: sdl2.SDL_SCANCODE_KP_8,
            49: sdl2.SDL_SCANCODE_KP_9,

            50: sdl2.SDL_SCANCODE_KP_PLUS,
            51: sdl2.SDL_SCANCODE_KP_MINUS,
            52: sdl2.SDL_SCANCODE_KP_MULTIPLY,
            53: sdl2.SDL_SCANCODE_KP_DIVIDE,
            54: sdl2.SDL_SCANCODE_KP_DECIMAL,
            55: sdl2.SDL_SCANCODE_KP_ENTER,

            # Movement
            60: sdl2.SDL_SCANCODE_UP,
            61: sdl2.SDL_SCANCODE_DOWN,
            62: sdl2.SDL_SCANCODE_LEFT,
            63: sdl2.SDL_SCANCODE_RIGHT,

            # Controls
            70: sdl2.SDL_SCANCODE_SPACE,
            71: sdl2.SDL_SCANCODE_RETURN,
            72: sdl2.SDL_SCANCODE_ESCAPE,
            73: sdl2.SDL_SCANCODE_TAB,
            74: sdl2.SDL_SCANCODE_CAPSLOCK,
            75: sdl2.SDL_SCANCODE_BACKSPACE,
            76: sdl2.SDL_SCANCODE_DELETE,
            77: sdl2.SDL_SCANCODE_INSERT,
            78: sdl2.SDL_SCANCODE_HOME,
            79: sdl2.SDL_SCANCODE_END,
            80: sdl2.SDL_SCANCODE_PAGEUP,
            81: sdl2.SDL_SCANCODE_PAGEDOWN,

            # Modifiers
            90: sdl2.SDL_SCANCODE_LSHIFT,
            91: sdl2.SDL_SCANCODE_RSHIFT,
            92: sdl2.SDL_SCANCODE_LCTRL,
            93: sdl2.SDL_SCANCODE_RCTRL,
            94: sdl2.SDL_SCANCODE_LALT,
            95: sdl2.SDL_SCANCODE_RALT,

            # Function keys
            100: sdl2.SDL_SCANCODE_F1,
            101: sdl2.SDL_SCANCODE_F2,
            102: sdl2.SDL_SCANCODE_F3,
            103: sdl2.SDL_SCANCODE_F4,
            104: sdl2.SDL_SCANCODE_F5,
            105: sdl2.SDL_SCANCODE_F6,
            106: sdl2.SDL_SCANCODE_F7,
            107: sdl2.SDL_SCANCODE_F8,
            108: sdl2.SDL_SCANCODE_F9,
            109: sdl2.SDL_SCANCODE_F10,
            110: sdl2.SDL_SCANCODE_F11,
            111: sdl2.SDL_SCANCODE_F12,

            # Special
            120: sdl2.SDL_SCANCODE_PRINTSCREEN,
            121: sdl2.SDL_SCANCODE_SCROLLLOCK,
            122: sdl2.SDL_SCANCODE_PAUSE,

            # Punctuation
            130: sdl2.SDL_SCANCODE_GRAVE,
            131: sdl2.SDL_SCANCODE_MINUS,
            132: sdl2.SDL_SCANCODE_EQUALS,
            133: sdl2.SDL_SCANCODE_LEFTBRACKET,
            134: sdl2.SDL_SCANCODE_RIGHTBRACKET,
            135: sdl2.SDL_SCANCODE_BACKSLASH,
            136: sdl2.SDL_SCANCODE_SEMICOLON,
            137: sdl2.SDL_SCANCODE_APOSTROPHE,
            138: sdl2.SDL_SCANCODE_COMMA,
            139: sdl2.SDL_SCANCODE_PERIOD,
            140: sdl2.SDL_SCANCODE_SLASH,
        }

    def updateThis(self):
        self.keys = sdl2.SDL_GetKeyboardState(None)


    def isPressDown(self, key, event):
        if event.type == sdl2.SDL_KEYDOWN and event.key.repeat == 0:
            return event.key.keysym.scancode == self.__dict_keynums[key]

    def isPressUp(self, key, event):
        if event.type == sdl2.SDL_KEYUP and event.key.repeat == 0:
            return event.key.keysym.scancode == self.__dict_keynums[key]

    def isPress(self, key): return self.keys[self.__dict_keynums[key]]


class Mouse:
    def __init__(self):
        self.pos_x, self.pos_y = sdl2.c_int(), sdl2.c_int()
        self.rel_x, self.rel_y = 0, 0
        self.wheel = 0
        self.buttons = None
        self.__dict_mousenum = {
            0: sdl2.SDL_BUTTON_LEFT,
            1: sdl2.SDL_BUTTON_MIDDLE,
            2: sdl2.SDL_BUTTON_RIGHT
        }

    def updateThis(self): self.buttons = sdl2.SDL_GetMouseState(self.pos_x, self.pos_y)

    def eventThis(self, event):
        if event.type == sdl2.SDL_MOUSEMOTION:
            self.rel_x, self.rel_y = event.motion.xrel, event.motion.yrel

        if event.type == sdl2.SDL_MOUSEWHEEL:
            self.wheel = event.wheel.y


    def mouseEnter(self, event):
        return event.type == sdl2.SDL_WINDOWEVENT and event.window.event == sdl2.SDL_WINDOWEVENT_ENTER

    def mouseLeave(self, event):
        return event.type == sdl2.SDL_WINDOWEVENT and event.window.event == sdl2.SDL_WINDOWEVENT_LEAVE
        

    def mouseButtonDown(self, button, event):
        return event.type == sdl2.SDL_MOUSEBUTTONDOWN and event.button.button == self.__dict_mousenum[button]
    
    def mouseButtonUp(self, button, event):
        return event.type == sdl2.SDL_MOUSEBUTTONUP and event.button.button == self.__dict_mousenum[button]


    def isLeft(self): return self.buttons & sdl2.SDL_BUTTON(sdl2.SDL_BUTTON_LEFT)
    
    def isMiddle(self): return self.buttons & sdl2.SDL_BUTTON(sdl2.SDL_BUTTON_MIDDLE)
    
    def isRight(self): return self.buttons & sdl2.SDL_BUTTON(sdl2.SDL_BUTTON_RIGHT)
    
    def getPos(self): return (self.pos_x.value, self.pos_y.value)
    
    def getRel(self): return (self.rel_x, self.rel_y)

    def getWheel(self): return self.wheel






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
        self.gamepad = Gamepad()

        self.delta_time = 0
        self.tick_time = 1 / 60

        #PRIVATE PROTECTED
        self._requirements = Requirements()
        self._running = True
        self._current_scene_name = self.settings.START_SCENE
        self._screen_color = (0.8, 0.8, 0.8)

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
            
            self.mouse.eventThis(event)
            self._scene_router._event(event)

        self._tick_timer += self.delta_time
        if self._tick_timer >= 1.0:
            self._tps = self._tick_count
            self._tick_count = 0
            self._tick_timer = 0.0


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