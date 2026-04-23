


class BaseClassBackend:
    NAME_CONTEXT="NONE"
    def __init__(self, game):
        self.game = game
        
        # SETTINGS
        self.glm = game._requirements.glm5
        self.sdl = game._requirements.sdl

        self.settings = game.settings
        self.subInitBufferData(self.glm)


    def showInfo(self):
        pass

    def createContext(self):
        pass


    def createFlags(self):
        pass


    def createVersion(self):
        pass

    def setPointSize(self, size):
        pass

    def setLineWidth(self, width):
        pass

    def setViewPort(self, width, height):
        pass


    def subInitBufferData(self, glm):
        self.indices = glm.array(glm.uint32, 0, 1, 2, 0, 2, 3,)
        self.vertices = glm.array(glm.float32,
            -1.0, -1.0,  0.0, 0.0, 
            1.0, -1.0,  1.0, 0.0,
            1.0,  1.0,  1.0, 1.0, 
            -1.0,  1.0,  0.0, 1.0, 
        )


    def clearColor(self, r, g, b):
        pass


    def setProjectile2D(self, width, height):
        pass