import sdl2
import easygui



class RequestCore:
    def __init__(self, game):
        self.__game = game
        self.__message_box_dict = {0: sdl2.SDL_MESSAGEBOX_INFORMATION, 2: sdl2.SDL_MESSAGEBOX_ERROR, 1: sdl2.SDL_MESSAGEBOX_WARNING}

    def closeGame(self):
        self.__game._running = False

    def updateSettings(self): self.__game.logger._system_log("ERROR", "Its not working")

    def redirectScene(self, scene):
        self.__game._current_scene_name = scene

    def restartScene(self):
        self.__game._scene_router._restartScene()

    def openUrl(self, url): sdl2.SDL_OpenURL(url.encode())

    def chooseFile(self, message): return easygui.fileopenbox(message, self.__game.settings.GAME_METADATA.META.GAME_TITLE)

    def isMinimilized(self, event):
        return event.type == sdl2.SDL_WINDOWEVENT and event.window.event == sdl2.SDL_WINDOWEVENT_MINIMIZED
        
    def isMaximilized(self, event):
        return event.type == sdl2.SDL_WINDOWEVENT and event.window.event == sdl2.SDL_WINDOWEVENT_MAXIMIZED
        
    def isRestored(self, event):
        return event.type == sdl2.SDL_WINDOWEVENT and event.window.event == sdl2.SDL_WINDOWEVENT_RESTORED
        
    def isResized(self, event):
        return event.type == sdl2.SDL_WINDOWEVENT and event.window.event == sdl2.SDL_WINDOWEVENT_RESIZED
    
    def isFocusLost(self, event):
        return event.type == sdl2.SDL_WINDOWEVENT and event.window.event == sdl2.SDL_WINDOWEVENT_FOCUS_LOST
    
    def isFocusGain(self, event):
        return event.type == sdl2.SDL_WINDOWEVENT and event.window.event == sdl2.SDL_WINDOWEVENT_FOCUS_GAINED
        


    def createMessageBox(self, title, info, type_messagebox=0): 
        sdl2.SDL_ShowSimpleMessageBox(self.__message_box_dict.get(type_messagebox, 0), title.encode(), info.encode(), None)

        
    def setWindowGrab(self, flag): sdl2.SDL_SetWindowGrab(self.__game._window.window, flag)
    def setWindowRelative(self, flag): sdl2.SDL_SetRelativeMouseMode(flag)
    def setScreenColor(self, r, g, b): self.__game._screen_color = (r, g, b)
    def setWindowPosition(self, x, y): self.__game._window.position = (x, y)
    def setWindowTitle(self, title): self.__game._window.title = title
    def setWindowSize(self, w, h): self.__game._window.size = (w, h)