
from rudlgc.packages import GameType, PackageScene

class Menu(PackageScene):
    def __init__(self, game: GameType):
        super().__init__(game)
        # Here we have self.keyboard, self.mouse, self.api

    def onUpdate(self):
        pass

    def onFixedUpdate(self):
        pass

    def onEvent(self, event):
        pass

    def onRender(self):
        pass

    def onSave(self):
        super().onSave()
