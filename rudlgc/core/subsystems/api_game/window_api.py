import easygui

    



class WindowApi:
    def __init__(self, game):
        self.sdl = game._requirements.sdl
        self._window = game._window
        self._settings = game.settings
        self._backend = game.backend_render

        self._x, self._y, self._w, self._h = self.sdl.c_int(), self.sdl.c_int(), self.sdl.c_int(), self.sdl.c_int()

        self.__message_box_dict = {
            0: self.sdl.SDL_MESSAGEBOX_INFORMATION,
            1: self.sdl.SDL_MESSAGEBOX_WARNING,
            2: self.sdl.SDL_MESSAGEBOX_ERROR
        }

    def openUrl(self, url):
        self.sdl.SDL_OpenURL(url.encode())


    def chooseFile(self, message):
        return easygui.fileopenbox(message, self._settings._GAME_METADATA.GAME_TITLE)
    

    def createMsgBox(self, title, info, type_messagebox=0): 
        self.sdl.SDL_ShowSimpleMessageBox(self.__message_box_dict.get(type_messagebox, 2), title.encode(), info.encode(), None)


    def setGrab(self, grab_flag): 
        self.sdl.SDL_SetWindowGrab(self._window.window, grab_flag)

    def setVsync(self, vsync_mode):
        self.sdl.SDL_GL_SwapInterval(vsync_mode)

    def setRelative(self, rel_flag):
        self.sdl.SDL_SetRelativeMouseMode(rel_flag)

    def clearColor(self, r, g, b):
        self._backend.clearColor(r, g, b)

    def setWindowPos(self, x, y):
        self._window.position = (int(x), int(y))

    def setWindowMinlimit(self, min_x, min_y):
        self.sdl.SDL_SetWindowMinimumSize(self._window.window, int(min_x), int(min_y))

    def setTitle(self, title):
        self._window.title = title

    def setWindowSize(self, w, h):
        self._window.size = (int(w), int(h))


    def getWindowSize(self):
        pass

    def getWindowPos(self):
        self.sdl.SDL_GetWindowPosition(self._window.window, self._x, self._y)

        return self._x.value, self._y.value


    