
from rudlgc.packages import GameType, SceneEmpty
from rudlgc.packages.package_model import RouterModel

# Our scenes
from DaemonDuck16.scenes.example import ExampleScene

class SceneManager(RouterModel):
    def onRegistration(self, game: GameType):

        # FIRST OF WE SWITCHING TO DEFAULT START SCENE
        self.START_SCENE = 'example'

        # HERE YOU CALLING 'self.registerScene' TO REGISTRATE TO GAME
        self.registerScene('example', lambda: ExampleScene(game=game))

        # Also has stub scene class
        # 'text_title' - for Window Title
        # 'text_about_scene' - for UI text
        # 'scene_switching' - for switching to scene when click the [ESC]
        # You can also change EmptyScene by inheritance
        self.registerScene('my-empty-scene', lambda: SceneEmpty(game=game, text_title='Stubs Title', text_about_scene='Hello World!', scene_switching='example'))




    # This method calling when game is ending. (Need for saving game progress)
    def savingProgress(self):
        pass


    # This method calling when program is catched an error.
    def onException(self, error: str):
        pass

