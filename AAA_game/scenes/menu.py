
from rudlgc.contrib import GameType, AbstractScene

class Menu(AbstractScene):
    def __init__(self, game: GameType):
        self.game = game
        self.sdl2 = self.game.requirements.sdl2
        self.game.request.setWindowTitle(f"{self.game.getCurrentScene()}")

    def onUpdate(self):
        pass

    def onEvent(self, event):
        if event.type == self.sdl2.SDL_KEYDOWN:
            self.game.request.redirectScene("example")

    def onRender(self):
        self.game.request.setScreenColor(1.0, 0.0, 0.9)

    def onSave(self):
        pass
