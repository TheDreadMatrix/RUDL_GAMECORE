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


def _group_by_category(settings, category_map):
    grouped = {}

    # reverse map: variable -> category
    reverse_map = {}

    for category, vars_list in category_map.items():
        for var in vars_list:
            reverse_map[var] = category

    for name, value in settings:
        group = reverse_map.get(name, "OTHER")

        if group not in grouped:
            grouped[group] = []

        grouped[group].append((name, value))

    return grouped


_PROHIBITED_WORDS = [
    "os",
    "sys",
    "importlib",
    "traceback",
    "signal",
    "pickle",
    "marshal",
    "rudlgc",
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
                           
    # THERE ALSO USING EMPTY SCENES FOR STUBS
    from rudlgc.contrib.package_scenes import SceneEmpty

    # THERE WE IMPORT OURS SCENES
    from {project_name}.scenes.example import ExampleScene
                           
    class SceneManager(SceneModel):
        def __init__(self, game: GameType, help_text: str=''):
            super().__init__(game)
                           
            # FIRST OF WE SWITCHING TO DEFAULT START SCENE
            self.game.api.redirectScene(self.game.settings.START_SCENE)
            
            # HERE YOU CALLING 'self.registerScene' TO REGISTRATE TO GAME
            self.registerScene('example', lambda: ExampleScene(game=game))

            # ALSO CREATE STUBS SCENE
            # 'text_title' - for Window Title
            # 'text_about_scene' - for UI text
            # 'scene_switching' - for switching to scene when click the [ESC]
            # You can also change EmptyScene by inheritance
            self.registerScene('my-empty-scene', lambda: SceneEmpty(game=game, text_title='Stubs Title', text_about_scene='Hello World!', scene_switching='example'))

            # ONLY ONE RULE IF YOU PUSH UNDEFINED SCENE YOUR CAN CRASH THE PROGRAM
            #SO ITS NOT GOOD IDEA, PLEASE BE ACCURACY, GOOD LUCK

            
        # THIS METHOD APPEARS WHEN GAME IS ENDING. (NEED FOR SAVING DATA PROGRESS)
        def savingProgress(self):
            pass


        # THIS METHOD APPEARS WHEN AN ERROR OCCURS IN THE CODE.
        def onException(self, error: str):
            pass

    """)




def _SETTINGS_PY(project_name: str):
    return textwrap.dedent(f"""
# =============================================
# {project_name.upper()} - SETTINGS CONFIGURATION FILE
# =============================================


# =========================================================
# CORE / DEBUG
# =========================================================

# Enables debug mode with logs and development tools.
# Must be False in production builds.
DEBUG = True

# External settings override file (stored in '.saves/settings.json').
# If None, engine auto-manages runtime settings.
JSON_SETTINGS = None


# =========================================================
# PROJECT METADATA
# =========================================================

# Internal application identifier (also used for build folder name)
APPNAME = "{project_name.lower()}_gamedata"

# Human-readable game name (UI/window title)
GAME_NAME = "My Game"

# Short description of the project
GAME_DESCRIPTION = "A game built with the engine."

# Version used for internal build tracking
FILE_VERSION = "1.0.0.0"

# Public version shown to players
GAME_VERSION = "1.0.0"

# Copyright / rights info
GAME_RIGHT = "All rights reserved."

# Path to application icon (None = default)
GAME_ICON = None


# =========================================================
# WINDOW / DISPLAY SETTINGS
# =========================================================

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Minimum allowed window size
WINDOW_MINWIDTH = 799
WINDOW_MINHEIGHT = 599

# Window behavior flags
VSYNC = False
FULLSCREEN = False
BORDERLESS = False
RESIZABLE = True


# =========================================================
# ENGINE RUNTIME
# =========================================================

# First scene loaded on startup
START_SCENE = "example"

# Frame timing settings
FPS = 60   # rendering FPS cap
PPS = 60   # physics/update rate


# =========================================================
# AUDIO
# =========================================================

# Volume values are in range 0.0 - 1.0
MUSIC_VOLUME = 0.5
SOUND_VOLUME = 0.7


# =========================================================
# DEBUG UI
# =========================================================

# Show performance and debug overlays
SHOW_FPS = True
SHOW_INFO = True


# =========================================================
# RENDERING QUALITY
# =========================================================

POINT_SIZE = 1.0
LINE_SIZE = 1.0


# =========================================================
# CUSTOM SETTINGS (ENGINE EXTENSION LAYER)
# =========================================================

# Categories are used ONLY for editor/UI grouping.
# They do NOT affect runtime logic.
__CUSTOM_CATEGORY = {{
    "GENERAL": ["HELLO_WORLD"],
    "SECRET": ["MY_ABSOLUTE_SECRET",]
}}

# Custom user-defined constants (accessible via game.settings)
HELLO_WORLD = ":)"
MY_ABSOLUTE_SECRET = 12345

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
