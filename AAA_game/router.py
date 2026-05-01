
from rudlgc.packages import GameType, SceneEmpty
from rudlgc.packages.package_model import RouterModel

from rudlgc import __version__


from AAA_game.scenes import ExampleScene



class SceneManager(RouterModel):
    def onResourcesCreate(self, game):
        game.resources.addImage(game.paths.getImagesPath(file="childs.png"), "out-image")
        game.resources.addImage(game.paths.getImagesPath(file="icon68.png"), "my-icon")

        game.resources.addMusic(game.paths.getMusicsPath(file="domain_island.ogg"), "daemon-music-1")
        game.resources.addSound(game.paths.getSoundsPath(file="sound_1.ogg"), "daemon-sound-1")



    def onRegistration(self, game: GameType):
        self.START_SCENE = "example"
        

        self.registerScene('none-scene', lambda: SceneEmpty(game=game, title="FutureScene", text_scene="Hello World!", switch="example"))
        self.registerScene('example', lambda: ExampleScene(game=game))
        
        

    # THIS METHOD APPEARS WHEN GAME IS ENDING. (NEED FOR SAVING DATA PROGRESS)
    
    def savingProgress(self):
        pass


    # THIS METHOD APPEARS WHEN AN ERROR OCCURS IN THE CODE.
    def onException(self, error: str):
        pass

