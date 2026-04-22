from rudlgc.contrib import GameType, PackageScene



class SceneError(PackageScene):
    def __init__(self, game: GameType):
        self.game = game
        self.game.window_api.setTitle("RUDLGC Error")
        
        self.game.logger._system_log("ERROR", "Catched error!!!")
        self.game.logger._system_log("ERROR", self.game.ERROR if self.game.ERROR else None)



    def onUpdate(self):
        pass
    

    def onEvent(self, event):
        return super().onEvent(event)
    

    def onRender(self):
        self.game.window_api.clearColor(0, 0, 0)
    

    def onSave(self):
        return super().onSave()
    


    

class SceneEmpty(PackageScene):
    def __init__(self, game: GameType, text_title: str, text_about_scene: str, scene_switching: str):
        self.game = game
        self.game.api.setWindowTitle(f"RUDLGC EMPTY: {text_title}")

        



    def onUpdate(self):
        return super().onUpdate()
    

    def onEvent(self, event):
        return super().onEvent(event)
    

    def onRender(self):
        self.game.api.setScreenColor(0, 0, 0)
    

    def onSave(self):
        return super().onSave()
    

