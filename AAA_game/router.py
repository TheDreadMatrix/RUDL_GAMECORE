
from rudlgc.contrib import SceneModel, GameType
from rudlgc.contrib.package_scenes import SceneEmpty
#THERE WE IMPORT OURS SCENES
from AAA_game.scenes.example import ExampleScene
from AAA_game.scenes.menu import Menu
from rudlgc.johnson import Joshua

class SceneManager(SceneModel):
    def __init__(self, game: GameType):
        super().__init__(game)

        self.settings = Joshua(self.game.paths.getSavesPath(file="settings.json"))
        self.settings_read = self.settings.readData()

        self.loadSettings(self.settings_read)
       
        #FIRST OF WE SWITCHING TO DEFAULT START SCENE
        self.game.api.redirectScene(self.game.settings.START_SCENE)

        #HERE YOU CALLING 'self.registerScene' TO REGISTRATE TO GAME
        self.registerScene('future-scene', lambda: SceneEmpty(game=game, text_title="FutureScene", text_about_scene="Hello World!", scene_switching="example"))
        self.registerScene('example', lambda: ExampleScene(game=game))
        self.registerScene('menu', lambda: Menu(game=game))
        #ONLY ONE RULE IF YOU PUSH UNDEFINED SCENE YOUR CAN CRASH THE PROGRAM
        #SO ITS NOT GOOD IDEA, PLEASE BE ACCURACY, GOOD LUCK


    #THIS METHOD APPEARS WHEN GAME IS ENDING. (NEED FOR SAVING DATA PROGRESS)
    def savingProgress(self):
        self.saveSettings(self.settings, self.settings_read)


    #THIS METHOD APPEARS WHEN AN ERROR OCCURS IN THE CODE.
    def onException(self, error: str):
        pass

