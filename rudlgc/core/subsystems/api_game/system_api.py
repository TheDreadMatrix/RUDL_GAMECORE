import easygui



class SystemApi:
    def __init__(self, game):
        self.sdl = game._requirements.sdl
        self._settings = game.settings

        self.__message_box_dict = {
            0: self.sdl.SDL_MESSAGEBOX_INFORMATION,
            1: self.sdl.SDL_MESSAGEBOX_WARNING,
            2: self.sdl.SDL_MESSAGEBOX_ERROR
        }

    def openUrl(self, url):
        self.sdl.SDL_OpenURL(url.encode())


    def chooseFile(self, message):
        return easygui.fileopenbox(message, self._settings.GAME_METADATA.META.GAME_TITLE)
    

    def createMsgBox(self, title, info, type_messagebox=0): 
        self.sdl.SDL_ShowSimpleMessageBox(self.__message_box_dict.get(type_messagebox, 2), title.encode(), info.encode(), None)
