import sdl2

class Gamepad:
    NOT_WORKING = 0


class Touchpad:
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