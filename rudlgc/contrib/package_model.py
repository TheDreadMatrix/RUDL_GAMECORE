from . import GameType, AbstractScene



class SceneModel:
    def __init__(self, game: GameType):
        
        self.__scene_dict = {
            "empty-rudlgc": AbstractScene(game=game),
            "error-scene": AbstractScene(game=game),
            "tile-map": AbstractScene(game=game),
            "quit": AbstractScene(game=game)
        }


    def registerScene(self, name, scene):
        self.__scene_dict.update({name: scene})


    def update(self):
        pass


    def event(self):
        pass


    def render(self):
        pass


