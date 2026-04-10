
from rudlgc.contrib import SceneModel, GameType
#THERE WE IMPORT OURS SCENES
from AAA_game.scenes.example import ExampleScene

class SceneManager(SceneModel):
    def __init__(self, game: GameType, help_text: str=''):
        super().__init__(game)

        #FIRST OF WE SWITCHING TO DEFAULT START SCENE
        self.game.request.redirectScene(self.game.settings.START_SCENE)

        #HERE YOU CALLING 'self.registerScene' TO REGISTRATE TO GAME
        self.registerScene('example', ExampleScene(game=game))

        #ONLY ONE RULE IF YOU PUSH UNDEFINED SCENE YOUR CAN CRASH THE PROGRAM
        #SO ITS NOT GOOD IDEA, PLEASE BE ACCURACY, GOOD LUCK

