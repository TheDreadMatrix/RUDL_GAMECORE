



class GameConfigApi:
    def __init__(self, game):
        self.__game = game
        

    def closeGame(self):
        self.__game._running = False



    def redirectScene(self, scene):
        self.__game._current_scene_name = scene

    def restartScene(self):
        self.__game._scene_router._restartScene()





    
