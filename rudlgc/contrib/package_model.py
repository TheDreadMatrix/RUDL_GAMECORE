from . import GameType, AbstractScene
from .package_scenes import SceneEmpty, _SceneError



class SceneModel:
    def __init__(self, game: GameType):
        self.game = game

        self._state_of_scene = ""
        self._scene_dict = {
            "empty-scene": lambda: SceneEmpty(game=game, text_title="Buildings Scene", text_about_scene="MOST USEFUL SCENE IN THE WORLD!!!", scene_switching=1),
            "error-scene": lambda: _SceneError(game=game),
        }
        self._current_scene_class = self._scene_dict.get(self.game.settings.START_SCENE, lambda: AbstractScene(game=game))()
        


    def registerScene(self, name: str, scene, ignore: bool=False):
        if not ignore:
            self.game.logger._system_log("INFO", f"Scene '{name}' has been registered.")
        self._scene_dict.update({name: scene})


    def _restartScene(self): 
        self._state_of_scene = self.game.getCurrentScene()
        self._current_scene_class.onSave()
        self._current_scene_class = None
        self._current_scene_class = self._scene_dict.get(self._state_of_scene)()


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


