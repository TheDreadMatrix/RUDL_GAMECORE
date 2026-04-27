


class BaseGraphicBackend:
    NAME_CONTEXT="NONE"
    def __init__(self, game):
        self.game = game
        
        # SETTINGS
        self.glm = game._requirements.glm5
        self.sdl = game._requirements.sdl
        self.pil = game._requirements.pil


        purple = (128, 0, 128)
        black = (0, 0, 0)

        pixels = bytearray()

        for y in range(256):
            for x in range(256):
                if ((x // 32) + (y // 32)) % 2 == 0:
                    color = purple
                else:
                    color = black

                pixels.extend(color)


        self.UNDEFINED_TEXTURE_BYTE = pixels

        self.settings = game.settings
        self.subInitBufferData(self.glm)

    def createTexture(self):
        pass

    def createNonTexture(self):
        pass

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
            0.0, 1.0, 0.0, 1.0, 
            1.0, 1.0, 1.0, 1.0, 
            1.0, 0.0, 1.0, 0.0, 
            0.0, 0.0, 0.0, 0.0
        )


    def clearColor(self, r, g, b):
        pass


    def setProjectile2D(self, width, height):
        pass