import textwrap



_EXAMPLE_PY = textwrap.dedent("""
#There we import 'GameType' for anotation and 'AbstractScene' for ours scene
from rudlgc.contrib import GameType, PackageScene
                              
class ExampleScene(PackageScene):
    #This method is designed to initialize (create) objects.
    #Here you create objects once, which is better
    def __init__(self, game: GameType):
        super().__init__(game)

    #This method is called every frame.                    
    def onUpdate(self):
        pass

    #This method is called every tick                
    def onFixedUpdate(self):
        pass

    #This method is called on any event, such as clicking, changing focus, etc.                      
    def onEvent(self, event):
        pass

    #The method is called after 'onUpdate' is created to draw objects              
    def onRender(self):
        pass

    #The method is called when the scene switches to another, otherwise the useful date must save here             
    def onSave(self):
        super().onSave()
                    
""")


def _SCENE_PY(class_name: str):
    formatted_name = "".join(word.capitalize() for word in class_name.replace("_", " ").split())

    return textwrap.dedent(f"""
    from rudlgc.contrib import GameType, PackageScene

    class {formatted_name}(PackageScene):
        def __init__(self, game: GameType):
            super().__init__(game)
            # Here we have self.keyboard, self.mouse, self.api

        def onUpdate(self):
            pass
            
        def onFixedUpdate(self):
            pass

        def onEvent(self, event):
            pass

        def onRender(self):
            pass

        def onSave(self):
            super().onSave()
    """)



def _ROUTER_PY(project_name: str):
    return textwrap.dedent(f"""
    from rudlgc.contrib import GameType, SceneEmpty
    from rudlgc.contrib.package_model import RouterModel

    # Our scenes
    from {project_name}.scenes.example import ExampleScene
                           
    class SceneManager(RouterModel):
        def onRegistration(self, game: GameType)
                           
            # FIRST OF WE SWITCHING TO DEFAULT START SCENE
            self.START_SCENE = 'example'
            
            # HERE YOU CALLING 'self.registerScene' TO REGISTRATE TO GAME
            self.registerScene('example', lambda: ExampleScene(game=game))

            # Also has stub scene class
            # 'text_title' - for Window Title
            # 'text_about_scene' - for UI text
            # 'scene_switching' - for switching to scene when click the [ESC]
            # You can also change EmptyScene by inheritance
            self.registerScene('my-empty-scene', lambda: SceneEmpty(game=game, text_title='Stubs Title', text_about_scene='Hello World!', scene_switching='example'))

            

            
        # This method calling when game is ending. (Need for saving game progress)
        def savingProgress(self):
            pass


        # This method calling when program is catched an error.
        def onException(self, error: str):
            pass

    """)




def _SETTINGS_PY(project_name: str):
    return textwrap.dedent(f"""
# =============================================
# {project_name.upper().replace("_", " ")} - SETTINGS CONFIGURATION FILE
# =============================================


# =========================================================
# CORE / DEBUG
# =========================================================

# Enables debug mode with logs and development tools.
# Must be False in production builds.
DEBUG = True

# Shows information about Engine and Fps
SHOW_INFO = True


# =========================================================
# PROJECT METADATA
# =========================================================

# Application and build metadata.
# APP_FOLDER defines the directory where game data will be stored
# and may also be used as the folder name during build/export.
# META contains general information about the game (title, version, etc.).
# Must be declarated

GAME_METADATA = {{
    "APP_FOLDER": ".{project_name.lower()}_data",
    "META": {{
        "GAME_TITLE": "My Game",
        "GAME_DESCRIPTION": "A game built with RUDLGC Engine",
        "GAME_ICON_TRUE": None,
        "GAME_ICON": None,
        "GAME_VERSION": "1.0.0",
        "COMPANY": "Write something...",
        "FILE_VERSION": "1.0.0.0"  
    }}
}}


# Joseph is class from rudlgc/johnson.py
# Use for saving settings into your json file. Works in '{project_name}/assets/csaves'
# from rudlgc.johnson import Joseph

RUDLGC_JOSEPH = None



# =========================================================
# WINDOW / DISPLAY SETTINGS
# =========================================================

WIDTH = 800
HEIGHT = 600

# Minimum allowed window size
MIN_WIDTH = 799
MIN_HEIGHT = 599

# Window behavior flags
VSYNC = 0 # must be [-1, 0, 1]
WINDOW_MODE = 0 # [0 - DEFAULT, 1 - RESIZABLE, 2 - BORDERLESS, 3 - FULLSCREEN]


# Frame timing settings
FPS = 60   # rendering FPS cap

# =========================================================
# RENDERING QUALITY
# =========================================================

POINT_SIZE = 10.0
LINE_WIDTH = 10.0

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
            # Set default name for the project
            # Also do not touch that environ!!! You can destroy your project!!!
            os.environ.setdefault("RUDLGC_PROJECT_NAME", "{project_name}")
            

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
