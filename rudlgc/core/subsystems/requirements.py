from rudlgc.core import _getOs
from importlib import import_module


class Requirements:
    def __init__(self, logger):
        self.os = _getOs()
        self.logger = logger
        
        self.mgl = None
        self.glm5 = None
        self.sdl = None
        self.audio = None

        self._loadImports()

   
    def _safeImport(self, name):
        try:
            return import_module(name)
        except Exception as e:
            self.logger._system_log("ERROR", f"[WARN] Cannot import {name}: {e}")
            return None
        
    def _loadImports(self):
        self.sdl = self._safeImport("sdl2")
        self.glm5 = self._safeImport("glm")
        self.audio = self._safeImport("sdl2.sdlmixer")
        
        
        if self.os in ("WINDOWS", "LINUX"):
            self.mgl = self._safeImport("moderngl")
            
        elif self.os == "ANDROID":
            self.mgl = None

        else:
            self.logger._system_log("ERROR", f"Can not work with systems: {self.os}")
