import platformdirs
from pathlib import Path
import sys




class PathCore:
    def __init__(self, game):
        PROJECT_DIR = game.PROJECT_NAME
        if hasattr(sys, "frozen"):
            self._BASE_DATA_DIR = Path(platformdirs.user_data_dir(game.settings.GAME_METADATA.APP_FOLDER))
        else:
            self._BASE_DATA_DIR = Path.cwd() / PROJECT_DIR

        if hasattr(sys, "_MEIPASS"):
            self._RESOURCE_DIR = Path(sys._MEIPASS)
        else:
            self._RESOURCE_DIR = Path.cwd() / PROJECT_DIR
            

        self.musics_dir = self._RESOURCE_DIR / "musics"
        self.sounds_dir = self._RESOURCE_DIR / "sounds"
        self.assets_dir = self._RESOURCE_DIR / "assets"
        self.fonts_dir = self._RESOURCE_DIR / "fonts"
        self.shaders_dir = self._RESOURCE_DIR / "shaders"

        self.config_dir = self._BASE_DATA_DIR / ".config"
        self.saves_dir = self._BASE_DATA_DIR / ".saves"

    def _build_path(self, base: Path, *folders, file: str | None = None):
        path = base
        for f in folders:
            path = path / f

        if file:
            path = path / file
        
        if not path.exists():
            raise FileExistsError(f"Path not found: '{str(path)}'")
        return str(path)

    def getConfigPath(self, *folder, file):
        return self._build_path(self.config_dir, *folder, file=file)

    def getSavesPath(self, *folder, file):
        return self._build_path(self.saves_dir, *folder, file=file)

    def getMusicsPath(self, *folder, file):
        return self._build_path(self.musics_dir, *folder, file=file)

    def getSoundsPath(self, *folder, file):
        return self._build_path(self.sounds_dir, *folder, file=file)

    def getAssetsPath(self, *folder, file):
        return self._build_path(self.assets_dir, *folder, file=file)

    def getFontsPath(self, *folder, file):
        return self._build_path(self.fonts_dir, *folder, file=file)

    def getShadersPath(self, *folder, file):
        return self._build_path(self.shaders_dir, *folder, file=file)