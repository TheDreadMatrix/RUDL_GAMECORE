from rudlgc.core import lru_cache




class ResourcesItems:
    def __init__(self, game):
        self.logger = game.logger
        self.backend_render = game.backend_render

        self._imageDict = {}
        self._fontDict = {}
        self._musicDict = {}
        self._soundDict = {}
        

    @lru_cache(maxsize=512)
    def addImage(self, path, item_id, ignore=False):
        if not ignore:
            self.logger._system_log("INFO", f"'{item_id}' has been registered")
        self._imageDict.update({item_id: self.backend_render.createTexture(path)})

    def addFont(self, path, item_id):
        pass

    def addMusic(self, path, item_id):
        pass

    def addSound(self, path, item_id):
        pass


    def removeImage(self, item_id, ignore=False):
        if not ignore:
            self.logger._system_log("INFO", f"'{item_id}' has been deleted")
        if item_id in self._imageDict:
            del self._imageDict[item_id]
        


    def _getItemImage(self, item_id):
        return self._imageDict.get(item_id)

