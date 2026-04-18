import textwrap
import ast
import os





def check_security(parser):
    project_name = os.getenv("RUDLGC_PROJECT_NAME")

    if not project_name:
        parser.error("Project name not found in RUDLGC_PROJECT_NAME")

    base_path = os.path.abspath(project_name)

    if not os.path.exists(base_path):
        parser.error(f"Project folder not found: {base_path}")

    violations = []

    for root, _, files in os.walk(base_path):
        for file in files:
            if not file.endswith(".py"):
                continue

            file_path = os.path.join(root, file)

            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    tree = ast.parse(f.read(), filename=file_path)
            except Exception:
                continue

            for node in ast.walk(tree):

                # 🔴 IMPORT
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        name = alias.name.split(".")[0]

                        if name == "rudlgc":
                            continue

                        if name in _PROHIBITED_WORDS:
                            violations.append((file_path, f"import {name}"))

                # 🔴 FROM IMPORT
                elif isinstance(node, ast.ImportFrom):
                    if node.module:
                        name = node.module.split(".")[0]

                        if name == "rudlgc":
                            continue

                        if name in _PROHIBITED_WORDS:
                            violations.append((file_path, f"from {name} import ..."))

                # 🔴 FUNCTION CALL
                elif isinstance(node, ast.Call):

                    # случай: eval(...)
                    if isinstance(node.func, ast.Name):
                        func_name = node.func.id

                        if func_name in _PROHIBITED_FUNCTIONS:
                            violations.append((file_path, f"call to {func_name}()"))

                    # случай: os.system(...)
                    elif isinstance(node.func, ast.Attribute):
                        value = node.func.value

                        if isinstance(value, ast.Name):
                            obj_name = value.id
                            attr_name = node.func.attr

                            # запрещаем os.*
                            if obj_name in _PROHIBITED_WORDS:
                                violations.append(
                                    (file_path, f"{obj_name}.{attr_name}()")
                                )

    if violations:
        messages = []
        for path, issue in violations:
            messages.append(f"{path} -> {issue}")

        parser.error(
            "Security violation: prohibited imports or function usage detected.\n"
            "Do not use restricted modules or dangerous functions.\n\n"
            + "\n".join(messages)
        )





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

_PROHIBITED_FUNCTIONS = [
    "getattr",
    "setattr",
    "delattr",
    "eval",
    "exec",
    "__import__",
    "compile",
    "open",        
    "input",
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
            
        def onFixedUpdate(self):
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
        def __init__(self, game: GameType):
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
# {project_name.upper().replace("_", " ")} - SETTINGS CONFIGURATION FILE
# =============================================

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
    "APP_FOLDER": ".{project_name.lower()}GameData",
    "META": {{
        "GAME_TITLE": "My Game",
        "GAME_DESCRIPTION": "A game built with RUDLGC Engine",
        "GAME_ICON": None,
        "GAME_VERSION": "1.0.0",
        "COMPANY": "Write something...",
        "FILE_VERSION": "1.0.0.0"  
    }}
}}


# =========================================================
# WINDOW / DISPLAY SETTINGS
# =========================================================

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Minimum allowed window size
WINDOW_MINWIDTH = 799
WINDOW_MINHEIGHT = 599

# Window behavior flags
VSYNC = 0 # must be [-1, 0, 1]
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


# =========================================================
# AUDIO
# =========================================================

# Volume values are in range 0.0 - 1.0
MUSIC_VOLUME = 1.0
SOUND_VOLUME = 1.0



# =========================================================
# RENDERING QUALITY
# =========================================================

POINT_SIZE = 10.0
LINE_SIZE = 10.0


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
