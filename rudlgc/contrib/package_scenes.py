from rudlgc.contrib import GameType, PackageScene



class SceneError(PackageScene):
    def __init__(self, game: GameType):
        super().__init__(game)
        self.window_api.setTitle("RUDLGC Error")
        
        self.logger._system_log("ERROR", "Catched error!!!")
        self.logger._system_log("ERROR", self.game.ERROR if self.game.ERROR else None)



    def onUpdate(self):
        pass
    

    def onEvent(self, event):
        return super().onEvent(event)
    

    def onRender(self):
        self.window_api.clearColor(0, 0, 0)
    

    def onSave(self):
        return super().onSave()
    


    

class SceneEmpty(PackageScene):
    def __init__(self, game: GameType, title: str, text_scene: str, switch: str):
        super().__init__(game)
        if title != "Ignore":
            self.window_api.setTitle(f"RUDLGC EMPTY: {title}")

        



    def onUpdate(self):
        return super().onUpdate()
    

    def onEvent(self, event):
        return super().onEvent(event)
    

    def onRender(self):
        self.window_api.clearColor(0, 0, 0)
    

    def onSave(self):
        return super().onSave()
    

