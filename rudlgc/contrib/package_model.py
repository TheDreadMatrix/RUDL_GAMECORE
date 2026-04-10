from . import GameType, AbstractScene



class SceneModel:
    def __init__(self, game: GameType):
        self.game = game

        self._state_of_scene = ""
        self._scene_dict = {
            "empty-rudlgc": lambda: AbstractScene(game=game),
            "error-scene": lambda: AbstractScene(game=game),
        }
        self._current_scene_class = self._scene_dict.get(self.game.settings.START_SCENE, lambda: AbstractScene(game=game))()
        


    def registerScene(self, name, scene):
        self._scene_dict.update({name: scene})


    def _restartScene(self): pass


    def _update(self):
        state = self.game.getCurrentScene()
        
        
        if state != self._state_of_scene:
            self._state_of_scene = state
            self._current_scene_class.onSave()
            self._current_scene_class = self._scene_dict.get(state)()

        self._current_scene_class.onUpdate()


    def _event(self, event):
        self._current_scene_class.onEvent(event)


    def _render(self):
        self._current_scene_class.onRender()


    def savingProgress(self):
        pass


    def onException(self, error: str): 
        pass


