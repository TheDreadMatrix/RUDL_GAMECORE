import textwrap
import re
import keyword

def is_valid_name(name: str) -> bool:
    if not name:
        return False

    if not (name[0].isalpha() or name[0] == "_"):
        return False
    
    if re.search(r"[^a-zA-Z0-9_]", name):
        return False

    if keyword.iskeyword(name):
        return False

    return True


_PROHIBITED_WORDS = [
    "nigga",
    "rudlgc",
    "test",
    "game",
    "mygame",
    "pygame",
    "pygaeme-ce",
    "moderngl",
    "rudleg",
    "rudlpp",
    "audio",
    "camera",
    "core",
    "contrib",
    "render",
    "stuff",
    "testproject",
    "venv",
]


_EXAMPLE_PY = textwrap.dedent("""
#There we import 'GameType' for anotation and 'AbstractScene' for ours scene
from rudlgc.contrib import GameType, AbstractScene
                              
class ExampleScene(AbstractScene):
    #This method is designed to initialize (create) objects.
    #Here you create objects once, which is better
    def __init__(self, game: GameType):
        self.game = game

    #This method is called every frame.                    
    def onUpdate(self):
        pass

    #This method is called on any event, such as clicking, changing focus, etc.                      
    def onEvent(self, event):
        pass

    #The method is called after 'onUpdate' is created to draw objects              
    def onRender(self):
        pass

    #The method is called when the scene switches to another, otherwise the useful date must save here             
    def onSave(self):
        pass
                    
""")


def _SCENE_PY(class_name: str):
    formatted_name = "".join(word.capitalize() for word in class_name.replace("_", " ").split())

    return textwrap.dedent(f"""
    from rudlgc.contrib import GameType, AbstractScene

    class {formatted_name}(AbstractScene):
        def __init__(self, game: GameType):
            self.game = game

        def onUpdate(self):
            pass

        def onEvent(self, event):
            pass

        def onRender(self):
            pass

        def onSave(self):
            pass
    """)



def _ROUTER_PY(project_name: str):
    return textwrap.dedent(f"""
    from rudlgc.contrib import SceneModel, GameType
    #THERE WE IMPORT OURS SCENES
    from {project_name}.scenes.example import ExampleScene
                           
    class SceneManager(SceneModel):
        def __init__(self, game: GameType, help_text: str=''):
            super().__init__(game)
                           
            #FIRST OF WE SWITCHING TO DEFAULT START SCENE
            self.game.request.redirectScene(self.game.settings.START_SCENE)
            
            #HERE YOU CALLING 'self.registerScene' TO REGISTRATE TO GAME
            self.registerScene('example', ExampleScene(game=game))

            #ONLY ONE RULE IF YOU PUSH UNDEFINED SCENE YOUR CAN CRASH THE PROGRAM
            #SO ITS NOT GOOD IDEA, PLEASE BE ACCURACY, GOOD LUCK

    """)




def _SETTINGS_PY(project_name: str):
    return textwrap.dedent(f"""
# =============================================
# {project_name.upper()} - SETTINGS CONFIGURATION FILE
# =============================================


# DEBUG mode enables additional logs and development features.
# Should be set to False in production.
DEBUG = True


# Window size settings
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Minimum allowed window size
WINDOW_MINWIDTH = 799
WINDOW_MINHEIGHT = 599

# Maximum allowed window size
WINDOW_MAXWIDTH = 1920
WINDOW_MAXHEIGHT = 1080

# Application and build metadata
# APPNAME is used as the application identifier and may also define
# the folder name when building/exporting the project.
APPNAME = ".{project_name.lower()}GameData"

# Human-readable game name displayed in UI or window title.
GAME_NAME = "My Game"

# Short description of the game/project.
GAME_DESCRIPTION = "A game built with the engine."

# File version used for internal tracking of builds/resources.
FILE_VERSION = "1.0.0"

# Path to the game icon used in the executable/window.
GAME_ICON = None

# Copyright or rights notice string.
GAME_RIGHT = "All rights reserved."

# Public game version shown to users.
GAME_VERSION = "1.0.0"

# Window title text.
TITLE = GAME_NAME


# Rendering / window behavior
VSYNC = False
FULLSCREEN = False
BORDERLESS = False
RESIZABLE = True


# Entry scene loaded at startup.
START_SCENE = "empty-rudlgc"


# Debug UI options
SHOW_FPS = True
SHOW_INFO = True
SHOW_PROMPT = True


# Audio settings (range typically 0.0 - 1.0)
MUSIC_VOLUME = 0.5
SOUND_VOLUME = 0.7


# Engine timing settings
# FPS - frames per second target for rendering
# PPS - physics/update steps per second
FPS = 60
PPS = 60


# Rendering quality settings
POINT_SIZE = 1.0
LINE_SIZE = 1.0

# =========================
# CUSTOM CONFIGURATION
# =========================
# Define constant values used by the game engine.
# Convention:
# - UPPER_CASE = constant
# - no __dunder__ names
# - accessible via game.settings if registered

HELLO_WORLD = ":)"

""")



def _MANAGE_PY(project_name: str):
    return textwrap.dedent(f"""
        import os


        def main():
            # Set default settings module and name for the project
            # Also do not touch that environs!!! You can destroy your project!!!
            os.environ.setdefault("RUDLGC_PROJECT_NAME", "{project_name}")
            os.environ.setdefault("RUDLGC_PROJECT_SETTINGS", "{project_name}.settings")

            try:
                # Import your CLI executor here
                from rudlgc.core.execute_prompt import execute_console
            except ImportError as exc:
                raise ImportError(
                    "Couldn't import RUDLGC. Are you sure it's installed? Did you forget to activate a virtual environment?"
                ) from exc

            # Pass CLI arguments to your engine
            execute_console()


        if __name__ == "__main__":
            main()
    """)



def _BUILD_PY(project_name: str):
    pass







if __name__ == "__main__":
    print(_ROUTER_PY("game"))
