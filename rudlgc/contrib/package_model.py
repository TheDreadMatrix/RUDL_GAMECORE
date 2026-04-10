from . import GameType, AbstractScene



class SceneModel:
    def __init__(self, game: GameType):
        self.game = game
        
        self._scene_dict = {
            "empty-rudlgc": lambda: AbstractScene(game=game),
            "error-scene": lambda: AbstractScene(game=game),
            "tile-map": lambda: AbstractScene(game=game),
            "quit": lambda: AbstractScene(game=game)
        }


    def registerScene(self, name, scene):
        self._scene_dict.update({name: lambda: scene})


    def update(self):
        pass


    def event(self):
        pass


    def render(self):
        pass


