
# =============================================
# AAA_GAME - SETTINGS CONFIGURATION FILE
# =============================================


# DEBUG mode enables additional logs and development features.
# Should be set to False in production.
DEBUG = True

WIDTH = 900
HEIGHT = 600

# 0 - default
# 1 - resize
# 2 - borderless 
# 3 - fullscreen
WINDOW_MODE = 0



# Application and build metadata
# APPNAME is used as the application identifier and may also define
# the folder name when building/exporting the project.

#SETTINGS = {
#    "FOLDERS": [],
 #   "FILE": "settings.json"
#}


GAME_METADATA = {
    "APP_FOLDER": ".aaa_gameGameData",
    "META": {
        "GAME_TITLE": "My Game",
        "GAME_DESCRIPTION": "A game built with RUDLGC Engine",
        "GAME_ICON_TRUE": "icon68.png",
        "GAME_ICON": None,
        "GAME_VERSION": "1.0.0",
        "COMPANY": "Write something...",
        "FILE_VERSION": "1.0.0.0"  
    }
}



# Rendering / window behavior



# Entry scene loaded at startup.



# Debug UI options






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
   "JUST-ATTR": ["HELLO_WORLD", "MY_DICT"],
   
}

HELLO_WORLD = ":)"
MY_DICT = {"num": {
    "1": 1, 
    "2": 2, 
    "3": {}
    }
}
