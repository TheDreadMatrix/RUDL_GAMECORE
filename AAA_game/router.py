
from rudlgc.packages import GameType, SceneEmpty
from rudlgc.packages.package_model import RouterModel


from AAA_game.scenes.example import ExampleScene
from AAA_game.scenes.main import Menu


class SceneManager(RouterModel):
    def onRegistration(self, game: GameType):
        self.START_SCENE = "example"
        
        
        self.registerScene('none-scene', lambda: SceneEmpty(game=game, title="FutureScene", text_scene="Hello World!", switch="example"))
        self.registerScene('example', lambda: ExampleScene(game=game))
        self.registerScene('menu', lambda: Menu(game))
        
        

    # THIS METHOD APPEARS WHEN GAME IS ENDING. (NEED FOR SAVING DATA PROGRESS)
    
    def savingProgress(self):
        self.game.settings.JOSEPH.saveData()
        


    # THIS METHOD APPEARS WHEN AN ERROR OCCURS IN THE CODE.
    def onException(self, error: str):
        pass

