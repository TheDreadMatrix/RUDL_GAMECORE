from rudlgc.contrib import GameType


#from rudlgc.render import Sprite2D
from rudlgc.rudlums import KeyNum
from rudlgc.render import Renderer


class PackageScene:
    def __init__(self, game: GameType):
        self.game = game

        self.keyboard = game.keyboard
        self.mouse = game.mouse

        self.window_api = game.window_api
        self.event_api = game.event_api
        self.config_api = game.config_api
        self.system_api = game.system_api

        self.resources = game.resources

        self.settings = game.settings
        self.paths = game.paths
        self.logger = game.logger

        self._requirements = game._requirements
        self.renderer = Renderer()

        self.logger._system_log("SCENE", f"Created scene: {self.__class__.__name__}")

    def onFixedUpdate(self):
        pass

    def onUpdate(self): 
        pass

    def onEvent(self, event):
        pass

    def onRender(self):
        pass
    
    def onSave(self):
        self.logger._system_log("SCENE", f"Deleted scene: {self.__class__.__name__}")


    


class SceneError(PackageScene):
    def __init__(self, game: GameType):
        super().__init__(game)
        self.window_api.setTitle("Error Game")
        
        
        self.logger._system_log("ERROR" if self.game.ERROR else "WARNING", 
                                self.game.ERROR if self.game.ERROR else "You shouldn`t have redirected that scene without error///")



    def onUpdate(self):
        pass
    

    def onEvent(self, event):
        if self.keyboard.isPressDown(KeyNum.ESC, event):
            self.config_api.closeGame()
    

    def onRender(self):
        self.window_api.clearColor(0.9, 0.7, 0)
    

    


    

class SceneEmpty(PackageScene):
    def __init__(self, game: GameType, title: str, text_scene: str, switch: str):
        super().__init__(game)
        if title != "Ignore":
            self.window_api.setTitle(f"{title}")

        self.switch = switch
    



    def onUpdate(self):
        pass
    

    def onEvent(self, event):
        if self.keyboard.isPressDown(KeyNum.ESC, event):
            if isinstance(self.switch, str):
                self.config_api.redirectScene(self.switch)
            else:
                self.config_api.closeGame()
    

    def onRender(self):
        self.window_api.clearColor(0.1, 0.6, 0.1)
    

    

