
# =============================================
# AAA_GAME - SETTINGS CONFIGURATION FILE
# =============================================


# DEBUG mode enables additional logs and development features.
# Should be set to False in production.

from rudlgc.johnson import Joseph


# Init Joseph

# 1. Init and change
# 2. Save in router
# 3. Set in game


# Declaration Joseph
RUDLGC_JOSEPH = Joseph("settings.json", app_folder=".aaa_gameGameData")


DEBUG = True
SHOW_INFO = True

# Changing by Joseph
WIDTH = 800
HEIGHT = 600

# 0 - default
# 1 - resize
# 2 - borderless 
# 3 - fullscreen
WINDOW_MODE = 1


MIN_WIDTH = 400
MIN_HEIGHT = 300

VSYNC = 0


# Application and build metadata
# APPNAME is used as the application identifier and may also define
# the folder name when building/exporting the project.

RUDLGC_INIT_BACKEND = "SDL-MANIA" # [SDL_MANIA, KIVY, GLFW]

RUDLGC_AUDIO_BACKEND = "SOLOUD" # [SOLOUD, MIXER_MANIA]

RUDLGC_RENDER_BACKEND = "OPENGL" # [VULKAN, OPENGL, ES]




GAME_METADATA = {
    "APP_FOLDER": ".aaa_gameData",
    "META": {
        "GAME_TITLE": "My Game",
        "GAME_DESCRIPTION": "A game built with RUDLGC Engine",
        "GAME_ICON_TRUE": "icon68.png",
        "GAME_ICON": None,
        "GAME_VERSION": "1.0.0",
        "COMPANY": "Write something...",
    }
}



# Rendering / window behavior
POINT_SIZE = 10
LINE_WIDTH = 10


# Entry scene loaded at startup.



# Debug UI options



OS_PLATFORM = "hello"




# Engine timing settings
# FPS - frames per second target for rendering
# PPS - physics/update steps per second
FPS = 240




# =========================
# CUSTOM CONFIGURATION
# =========================
# Define constant values used by the game engine.
# Convention:
# - UPPER_CASE = constant
# - no __dunder__ names
# - accessible via game.settings if registered

__CUSTOM_CATEGORY = {
   "JUST-ATTR": ["HELLO_WORLD"],
   "FUTURE": ["RUDLGC_AUDIO_BACKEND", "RUDLGC_INIT_BACKEND", "RUDLGC_RENDER_BACKEND"]
   
}

HELLO_WORLD = ":)"

