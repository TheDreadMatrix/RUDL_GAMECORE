


class EventApi:
    def __init__(self, game):
        self.sdl = game._requirements.sdl

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
        


    
