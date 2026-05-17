from . import GameType
from .package_scenes import SceneEmpty, SceneError
from typing import Callable
import traceback as _error

__all__ = ["RouterModel"]

class RouterModel:
    def __init__(self, game: GameType):
        self.game = game

        self.START_SCENE = 0

        self._state_of_scene = ""
        self._scene_dict = {
            0: lambda: SceneEmpty(game=game, title="Buildings Scene", text_scene="MOST USEFUL SCENE IN THE WORLD!!!", switch=1),
            1: lambda: SceneError(game=game),
        }
        
        
    def onRegistration(self, game: GameType):
        pass

    


    def _startGameLoop(self):
        self.game._current_scene_name = self.START_SCENE
        self._state_of_scene = self.START_SCENE
        self._current_scene_class = self._scene_dict.get(self.game._current_scene_name, self._scene_dict[0])()


    def registerScene(self, name: str, scene_fabric: Callable[[], SceneEmpty]):
        self.game.logger._system_log("SCENE", f"Scene '{name}' has been registered.")
        self._scene_dict.update({name: scene_fabric})


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


