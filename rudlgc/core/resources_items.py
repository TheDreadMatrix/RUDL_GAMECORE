




class ResourcesItems:
    def __init__(self, game):

        self.backend_render = game.backend_render

        self._imageDict = {}
        self._fontDict = {}
        self._musicDict = {}
        self._soundDict = {}
        


    def addImage(self, path, item_id):
        self._imageDict.update({item_id: self.backend_render.createTexture(path)})

    def addFont(self, path, item_id):
        pass

    def addMusic(self, path, item_id):
        pass

    def addSound(self, path, item_id):
        pass


    def removeImage(self, item_id):
        if item_id in self._imageDict:
            del self._imageDict[item_id]
        


    def _getItemImage(self, item_id):
        return self._imageDict.get(item_id)

