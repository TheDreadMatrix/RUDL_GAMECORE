import warnings as _WARNING_OFF_SDL

_WARNING_OFF_SDL.filterwarnings("ignore", message="Using SDL2 binaries from pysdl2-dll*")


OPENGL = 1
OPENGL_ES = 2
VULKAN = 4

__version__ = "1.0.0"
