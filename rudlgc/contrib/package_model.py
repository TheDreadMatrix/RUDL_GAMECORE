from . import GameType, PackageScene
from .package_scenes import SceneEmpty, SceneError
import traceback as _error


class SceneModel:
    def __init__(self, game: GameType):
        self.game = game

        self.START_SCENE = "empty-scene"

        self._state_of_scene = ""
        self._scene_dict = {
            "empty-scene": lambda: SceneEmpty(game=game, text_title="Buildings Scene", text_about_scene="MOST USEFUL SCENE IN THE WORLD!!!", scene_switching=1),
            "error-scene": lambda: SceneError(game=game),
        }
        
        
    def onRegistration(self, game: GameType):
        pass


    def _startGameLoop(self):
        self.game._current_scene_name = self.START_SCENE
        self._state_of_scene = self.START_SCENE
        self._current_scene_class = self._scene_dict.get(self.game._current_scene_name)()


    def registerScene(self, name: str, scene, ignore: bool=False):
        if not ignore:
            self.game.logger._system_log("INFO", f"Scene '{name}' has been registered.")
        self._scene_dict.update({name: scene})


    def _restartScene(self): 
        self._state_of_scene = self.game.getCurrentScene()
        try:
            self._current_scene_class.onSave()
            self._current_scene_class = None
        except Exception:
            error_message = _error.format_exc()
            self.game.ERROR = error_message
            self._state_of_scene = "error"
            self.onException(error_message)
        self._current_scene_class = self._scene_dict.get(self._state_of_scene)()


    def _update(self):
        state = self.game.getCurrentScene()
        if state != self._state_of_scene:
            self._state_of_scene = state
            try:
                self._current_scene_class.onSave()
            except Exception:
                error_message = _error.format_exc()
                self.game.ERROR = error_message
                state = "error-scene"
                self.onException(error_message)
            self._current_scene_class = self._scene_dict.get(state)()

        self._current_scene_class.onUpdate()

    def _updateFixed(self):
        self._current_scene_class.onFixedUpdate()

    def _event(self, event):
        self._current_scene_class.onEvent(event)


    def _render(self):
        self._current_scene_class.onRender()


    def savingProgress(self):
        pass


    def onException(self, error: str): 
        pass


