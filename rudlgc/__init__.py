import warnings as _WARNING_OFF_SDL

_WARNING_OFF_SDL.filterwarnings("ignore", message="Using SDL2 binaries from pysdl2-dll*")


from .contrib import GameType, AbstractScene
from .stuff import JUST_CUBE


__version__ = "1.0.0"
__all__ = ["JUST_CUBE", "GameType", "AbstractScene"]