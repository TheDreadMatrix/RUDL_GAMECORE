




class ResourcesItems:
    def __init__(self, game):
        self.logger = game.logger
        self.backend_render = game.backend_render

        self._imageDict = {}
        self._fontDict = {}
        self._musicDict = {}
        self._soundDict = {}
        
    # ADD ITEM TO MANAGER
    def addImage(self, path, item_id, ignore=False):
        self.__showMessage(item_id, ignore, 1)

        self._imageDict.update({item_id: self.backend_render.createTexture(path)})

    
    def addFont(self, path, item_id, ignore=False):
        self.__showMessage(item_id, ignore, 1)

    
    def addMusic(self, path, item_id, ignore=False):
        self.__showMessage(item_id, ignore, 1)

   
    def addSound(self, path, item_id, ignore=False):
        self.__showMessage(item_id, ignore, 1)


    # DELETING RESOURCES
    def removeImage(self, item_id, ignore=False):
        self.__showMessage(item_id, ignore, 0)

        if item_id in self._imageDict:
            del self._imageDict[item_id]
        


    # PRIVATE PROTECTED
    def __showMessage(self, item_id, ignore, msg_type):
        if not ignore:
            self.logger._system_log("INFO", f"'{item_id}' has been deleted" if not msg_type else f"'{item_id}' has been registered")


    def _getItemImage(self, item_id):
        return self._imageDict.get(item_id)
    
    def _getItemMusic(self, item_id):
        return self._musicDict.get(item_id)
    
    def _getItemSound(self, item_id):
        return self._soundDict.get(item_id)
    
    def _getItemFont(self, item_id):
        return self._fontDict.get(item_id)

