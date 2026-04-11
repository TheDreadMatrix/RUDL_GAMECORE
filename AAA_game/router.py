
from rudlgc.contrib import SceneModel, GameType
from rudlgc.contrib.package_scenes import SceneEmpty
#THERE WE IMPORT OURS SCENES
from AAA_game.scenes.example import ExampleScene
from AAA_game.scenes.menu import Menu

class SceneManager(SceneModel):
    def __init__(self, game: GameType, help_text: str=''):
        super().__init__(game)

        #FIRST OF WE SWITCHING TO DEFAULT START SCENE
        self.game.request.redirectScene(self.game.settings.START_SCENE)

        #HERE YOU CALLING 'self.registerScene' TO REGISTRATE TO GAME
        self.registerScene('future-scene', lambda: SceneEmpty(game=game, text_title="FutureScene", text_about_scene="Hello World!", scene_switching="example"))
        self.registerScene('example', lambda: ExampleScene(game=game))
        self.registerScene('menu', lambda: Menu(game=game))
        #ONLY ONE RULE IF YOU PUSH UNDEFINED SCENE YOUR CAN CRASH THE PROGRAM
        #SO ITS NOT GOOD IDEA, PLEASE BE ACCURACY, GOOD LUCK


    #THIS METHOD APPEARS WHEN GAME IS ENDING. (NEED FOR SAVING DATA PROGRESS)
    def savingProgress(self):
        pass


    #THIS METHOD APPEARS WHEN AN ERROR OCCURS IN THE CODE.
    def onException(self, error: str):
        pass

