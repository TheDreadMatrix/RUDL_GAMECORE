
# =============================================
# AAA_GAME - SETTINGS CONFIGURATION FILE
# =============================================

# DEBUG mode enables additional logs and development features.
# Should be set to False in production.
DEBUG = True
MY = 10

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
APPNAME = ".aaa_gameGameData"

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
