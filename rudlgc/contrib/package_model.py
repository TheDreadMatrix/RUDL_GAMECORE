from . import GameType, AbstractScene
from .package_scenes import SceneEmpty, SceneError
import traceback as _error


class SceneModel:
    def __init__(self, game: GameType):
        self.game = game

        self._state_of_scene = ""
        self._scene_dict = {
            "empty-scene": lambda: SceneEmpty(game=game, text_title="Buildings Scene", text_about_scene="MOST USEFUL SCENE IN THE WORLD!!!", scene_switching=1),
            "error-scene": lambda: SceneError(game=game),
        }
        self._current_scene_class = self._scene_dict.get(self.game.settings.START_SCENE, lambda: AbstractScene(game=game))()
        


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


    def loadSettings(self, joshua_settings_data):
        self.game.settings.WINDOW_WIDTH = joshua_settings_data["window"]["window-size"]["width"]
        self.game.settings.WINDOW_HEIGHT = joshua_settings_data["window"]["window-size"]["height"]
        self.game.settings.WINDOW_MINWIDTH = joshua_settings_data["window"]["window-size"]["min-width"]
        self.game.settings.WINDOW_MINHEIGHT = joshua_settings_data["window"]["window-size"]["min-height"]

        self.game.settings.VSYNC = joshua_settings_data["window"]["window-attr"]["vsync"]
        self.game.settings.BORDERLESS = joshua_settings_data["window"]["window-attr"]["borderless"]
        self.game.settings.FULLSCREEN = joshua_settings_data["window"]["window-attr"]["fullscreen"]
        self.game.settings.RESIZABLE = joshua_settings_data["window"]["window-attr"]["resizable"]

        self.game.settings.FPS = joshua_settings_data["frametime"]
        self.game.settings.SOUND_VOLUME = joshua_settings_data["audio"]["sound-volume"]
        self.game.settings.MUSIC_VOLUME = joshua_settings_data["audio"]["music-volume"]
        self.game.api.updateSettings()


    def saveSettings(self, joshua_settings_data, joshua_settings_data_read: None=None):
        save_dict = {
            "window": {
                "window-size": {
                    "width": self.game.settings.WINDOW_WIDTH,
                    "height": self.game.settings.WINDOW_HEIGHT,
                    "min-width": self.game.settings.WINDOW_MINWIDTH,
                    "min-height": self.game.settings.WINDOW_MINHEIGHT
                },
                "window-attr": {
                    "vsync": self.game.settings.VSYNC,
                    "fullscreen": self.game.settings.FULLSCREEN,
                    "borderless": self.game.settings.BORDERLESS,
                    "resizable": self.game.settings.RESIZABLE
                }
            },
            "audio": {
                "sound-volume": self.game.settings.SOUND_VOLUME,
                "music-volume": self.game.settings.MUSIC_VOLUME
            },
            "frametime": self.game.settings.FPS
        }

        joshua_settings_data.saveData(save_dict)
        if joshua_settings_data_read is not None:
            joshua_settings_data.saveData(joshua_settings_data_read)


    def savingProgress(self):
        pass


    def onException(self, error: str): 
        pass


