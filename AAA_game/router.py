
from rudlgc.contrib import SceneModel, GameType
from rudlgc.contrib.package_scenes import SceneEmpty
#THERE WE IMPORT OURS SCENES
from AAA_game.scenes.example import ExampleScene



class SceneManager(SceneModel):
    def onRegistration(self, game: GameType):

        self.START_SCENE = "example"
        #FIRST OF WE SWITCHING TO DEFAULT START SCENE
        #self.game.config_api.redirectScene(self.game.settings.START_SCENE)

        #HERE YOU CALLING 'self.registerScene' TO REGISTRATE TO GAME
        self.registerScene('future-scene', lambda: SceneEmpty(game=game, title="FutureScene", text_scene="Hello World!", switch="example"), ignore=True)
        self.registerScene('example', lambda: ExampleScene(game=game), ignore=True)
        
        

    #THIS METHOD APPEARS WHEN GAME IS ENDING. (NEED FOR SAVING DATA PROGRESS)
    def savingProgress(self):
        pass


    #THIS METHOD APPEARS WHEN AN ERROR OCCURS IN THE CODE.
    def onException(self, error: str):
        pass

