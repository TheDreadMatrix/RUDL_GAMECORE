




class ResourcesItems:
    def __init__(self, game):
        self.logger = game.logger
        self.backend_render = game.backend_render

        self._imageDict = {}
        self._fontDict = {}  
        self._musicDict = {}
        self._soundDict = {}
        
    # ADD ITEM TO MANAGER
    def addImage(self, path, item_id):
        self.__showMessage(item_id, 1)

        self._imageDict.update({item_id: self.backend_render.createTexture(path)})

    
    def addFont(self, path, item_id):
        self.__showMessage(item_id, 1)

    
    def addMusic(self, path, item_id):
        self.__showMessage(item_id, 1)
        self._musicDict.update({item_id: path})

   
    def addSound(self, path, item_id):
        self.__showMessage(item_id, 1)
        self._soundDict.update({item_id: path})


    # DELETING RESOURCES
    def removeImage(self, item_id):
        self.__showMessage(item_id, 0)

        if item_id in self._imageDict:
            del self._imageDict[item_id]

    def removeMusic(self, item_id):
        self.__showMessage(item_id, 0)

        if item_id in self._musicDict:
            del self._musicDict[item_id]

    def removeSound(self, item_id):
        self.__showMessage(item_id, 0)

        if item_id in self._soundDict:
            del self._soundDict[item_id]


    # PRIVATE PROTECTED
    def __showMessage(self, item_id, msg_type):
        self.logger._system_log("RESOURCE", f"'{item_id}' has been deleted" if not msg_type else f"'{item_id}' has been registered")


    def _getItemImage(self, item_id):
        return self._imageDict.get(item_id)
    
    def _getItemMusic(self, item_id):
        return self._musicDict.get(item_id)
    
    def _getItemSound(self, item_id):
        return self._soundDict.get(item_id)
    
    def _getItemFont(self, item_id):
        return self._fontDict.get(item_id)

