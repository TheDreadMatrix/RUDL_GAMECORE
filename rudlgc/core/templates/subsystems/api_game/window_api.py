



class WindowApi:
    def __init__(self, game):
        self.sdl = game._requirements.sdl
        self._window = game._window
        self._backend = game.backend_render


    def setGrab(self, grab_flag): 
        self.sdl.SDL_SetWindowGrap(self._window.window, grab_flag)

    def setRelative(self, rel_flag):
        self.sdl.SDL_SetRelativeMouseMode(rel_flag)

    def clearColor(self, r, g, b):
        self._backend.clearColor(r, g, b)

    def setWindowPos(self, x, y):
        self._window.position = (x, y)

    def setWindowMinlimit(self, min_x, min_y):
        self.sdl.SDL_SetWindowMinimumSize(self._window.window, min_x, min_y)

    def setTitle(self, title):
        self._window.title = title

    def setWindowSize(self, w, h):
        self._window.size = (w, h)


    