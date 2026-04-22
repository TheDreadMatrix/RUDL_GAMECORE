import easygui


class EventApi:
    def __init__(self, game):
        self.sdl = game._requirements.sdl
        self._settings = game.settings

        self.__message_box_dict = {
            0: self.sdl.SDL_MESSAGEBOX_INFORMATION,
            1: self.sdl.SDL_MESSAGEBOX_WARNING,
            2: self.sdl.SDL_MESSAGEBOX_ERROR
        }

    def openUrl(self, url):
        self.sdl.SDL_OpenUrl(url.encode())

    def chooseFile(self, message):
        return easygui.fileopenbox(message, self._settings.GAME_METADATA.META.GAME_TITLE)


    def isMinimilized(self, event):
        return event.type == self.sdl.SDL_WINDOWEVENT and \
        event.window.event == self.sdl.SDL_WINDOWEVENT_MINIMIZED
        
    def isMaximilized(self, event):
        return event.type == self.sdl.SDL_WINDOWEVENT and \
        event.window.event == self.sdl.SDL_WINDOWEVENT_MAXIMIZED
        
    def isRestored(self, event):
        return event.type == self.sdl.SDL_WINDOWEVENT and \
        event.window.event == self.sdl2.SDL_WINDOWEVENT_RESTORED
        
    def isResized(self, event):
        return event.type == self.sdl.SDL_WINDOWEVENT and \
        event.window.event == self.sdl.SDL_WINDOWEVENT_RESIZED
    
    def isFocusLost(self, event):
        return event.type == self.sdl.SDL_WINDOWEVENT and \
        event.window.event == self.sdl.SDL_WINDOWEVENT_FOCUS_LOST
    
    def isFocusGain(self, event):
        return event.type == self.sdl.SDL_WINDOWEVENT and \
        event.window.event == self.sdl.SDL_WINDOWEVENT_FOCUS_GAINED
        


    def createMessageBox(self, title, info, type_messagebox=0): 
        self.sdl.SDL_ShowSimpleMessageBox(self.__message_box_dict.get(type_messagebox, 2), title.encode(), info.encode(), None)
