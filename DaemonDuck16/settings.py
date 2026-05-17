
# =============================================
# DAEMONDUCK16 - SETTINGS CONFIGURATION FILE
# =============================================

# =========================================================
# CORE / DEBUG
# =========================================================

# Enables debug mode with debug server and development tools.
DEBUG = True

# Shows information about Engine and Fps
SHOW_INFO = True


# =========================================================
# PROJECT METADATA
# =========================================================

# For building path
RUDLGC_APP_FOLDER = ".daemonduck16_data"

# Application and build metadata.
# APP_FOLDER defines the directory where game data will be stored
# and may also be used as the folder name during build/export.
# META contains general information about the game (title, version, etc.).
# Must be declarated

GAME_METADATA = {
    "GAME_TITLE": "My Game",
    "GAME_DESCRIPTION": "A game built with RUDLGC Engine",
    "GAME_ICON_TRUE": None,
    "GAME_ICON": None,
    "GAME_VERSION": "1.0.0",
    "COMPANY": "Write something..."
}


# Joseph is class from rudlgc/johnson.py
# Use for saving settings into your json file. Works in 'DaemonDuck16/assets/csaves'
# Also have in game.settings.JOSEPH to change and save data in game

from rudlgc.johnson import Joseph

RUDLGC_JOSEPH = Joseph('settings.json', RUDLGC_APP_FOLDER)



# =========================================================
# WINDOW / DISPLAY SETTINGS
# =========================================================

from rudlgc.rudlums import RenderModes, WindowModes, VsyncModes

# Choose your render backend 
RUDLGC_RENDER_BACKEND = RenderModes.OPENGL


WIDTH = 800
HEIGHT = 600

# Minimum allowed window size
MIN_WIDTH = 799
MIN_HEIGHT = 599

# Window behavior flags
VSYNC = VsyncModes.DISABLED
WINDOW_MODE = WindowModes.DEFAULT


# Frame timing settings
FPS = 240   # rendering FPS cap

# Render tools
POINT_SIZE = 10.0
LINE_WIDTH = 10.0


# =========================================================
# CUSTOM SETTINGS (ENGINE EXTENSION LAYER)
# =========================================================

# Categories are used ONLY for editor/UI grouping.
# They do NOT affect runtime logic.
__CUSTOM_CATEGORY = {
    "GENERAL": ["HELLO_WORLD"],
    "SECRET": ["MY_ABSOLUTE_SECRET",]
}

# Custom user-defined constants (accessible via game.settings)
HELLO_WORLD = ":)"
MY_ABSOLUTE_SECRET = 12345


