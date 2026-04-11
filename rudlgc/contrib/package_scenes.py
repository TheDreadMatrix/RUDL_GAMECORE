from rudlgc.contrib import GameType, AbstractScene



class _SceneError(AbstractScene):
    def __init__(self, game: GameType):
        self.game = game
        self.game.request.setWindowTitle("RUDLGC Error")
        
        print(self.game.ERROR if self.game.ERROR else None)



    def onUpdate(self):
        pass
    

    def onEvent(self, event):
        return super().onEvent(event)
    

    def onRender(self):
        return super().onRender()
    

    def onSave(self):
        return super().onSave()
    


    

class SceneEmpty(AbstractScene):
    def __init__(self, game: GameType, text_about_scene: str, scene_switch: str):
        self.game = game



    def onUpdate(self):
        return super().onUpdate()
    

    def onEvent(self, event):
        return super().onEvent(event)
    

    def onRender(self):
        return super().onRender()
    

    def onSave(self):
        return super().onSave()
    

