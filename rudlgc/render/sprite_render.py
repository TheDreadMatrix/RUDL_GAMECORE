from rudlgc.contrib import GameType
from rudlgc.render import CustomShader



class Sprite2D:
    def __init__(self, game: GameType, custom_shader: CustomShader|None=None):
        self.__glm = game._requirements.glm5

        self.game = game


        self.__Position = self.__glm.vec2(0, 0)
        self.__Size = self.__glm.vec2(0, 0)
        self.__Layer = 0

        self.__Alpha = 1
        self.__Texture = None  #UNDEF TEXTURE
        


    def setPosition(self, x: float, y: float):
        self.__Position = self.__glm.vec2(x, y)

    def setSize(self, w: float, h: float):
        self.__Size = self.__glm.vec2(w, h)

    def setLayer(self, layer: int):
        self.__Layer = layer

    def setAlpha(self, alpha: float):
        self.__Alpha = alpha

    def setTexture(self):
        self.__Texture = None

    
    def showMe(self):
        pass

    