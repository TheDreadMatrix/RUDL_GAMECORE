from rudlgc.contrib import GameType, AbstractScene



class SceneError(AbstractScene):
    def __init__(self, game: GameType):
        self.game = game
        self.game.request.setWindowTitle("RUDLGC Error")
        
        self.game.logger._system_log("ERROR", "Catched error!!!")
        self.game.logger._system_log("ERROR", self.game.ERROR if self.game.ERROR else None)



    def onUpdate(self):
        pass
    

    def onEvent(self, event):
        return super().onEvent(event)
    

    def onRender(self):
        self.game.request.setScreenColor(0, 0, 0)
    

    def onSave(self):
        return super().onSave()
    


    

class SceneEmpty(AbstractScene):
    def __init__(self, game: GameType, text_title: str, text_about_scene: str, scene_switching: str):
        self.game = game
        self.game.request.setWindowTitle(f"RUDLGC EMPTY: {text_title}")

        



    def onUpdate(self):
        return super().onUpdate()
    

    def onEvent(self, event):
        return super().onEvent(event)
    

    def onRender(self):
        self.game.request.setScreenColor(0, 0, 0)
    

    def onSave(self):
        return super().onSave()
    

