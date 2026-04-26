
from rudlgc.contrib import SceneModel, GameType
from rudlgc.contrib.package_scenes import SceneEmpty


from AAA_game.scenes import ExampleScene



class SceneManager(SceneModel):
    def onResourcesCreate(self, game):
        game.resources.addImage(game.paths.getImagesPath(file="childs.png"), "out-image")
        game.resources.addImage(game.paths.getImagesPath(file="icon68.png"), "my-icon")



    def onRegistration(self, game: GameType):
        self.START_SCENE = "example"
        

        self.registerScene('future-scene', lambda: SceneEmpty(game=game, title="FutureScene", text_scene="Hello World!", switch="example"), ignore=True)
        self.registerScene('example', lambda: ExampleScene(game=game), ignore=True)
        
        

    #THIS METHOD APPEARS WHEN GAME IS ENDING. (NEED FOR SAVING DATA PROGRESS)
    def savingProgress(self):
        pass


    #THIS METHOD APPEARS WHEN AN ERROR OCCURS IN THE CODE.
    def onException(self, error: str):
        pass

