import sdl2




class RequestCore:
    def __init__(self, game):
        self.game = game

    def closeGame(self):
        self.game._running = False

    def updateSettings(self): self.game.logger._system_log("ERROR", "Its not working")

    def redirectScene(self, scene):
        self.game._current_scene_name = scene

    def restartScene(self):
        self.game._scene_router._restartScene()

    def openUrl(self, url): sdl2.SDL_OpenURL(url.encode())



    def setWindowGrab(self, flag): sdl2.SDL_SetWindowGrab(self.game._window.window, flag)
    def setWindowRelative(self, flag): sdl2.SDL_SetRelativeMouseMode(flag)
    def setScreenColor(self, r, g, b): self.game._screen_color = (r, g, b)
    def setWindowPosition(self, x, y): self.game._window.position = (x, y)
    def setWindowTitle(self, title): self.game._window.title = title
    def setWindowSize(self, w, h): self.game._window.size = (w, h)