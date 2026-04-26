from rudlgc.render import CustomShader, Renderer


class Sprite2D:
    def __init__(self, game, renderer: Renderer, custom_shader: CustomShader|None=None):
        self.__glm = game._requirements.glm5

        self.game = game
        self.renderer = renderer
        self.renderer.sprites.append(self)

        self.backend_render = game.backend_render


        self.__Position = self.__glm.vec2(0, 0)
        self.__Size = self.__glm.vec2(300, 450)
        self.__Layer = 0

        self.__Alpha = 1
        self.__Texture = game.backend_render.createNonTexture()

        self.__program = custom_shader._program if custom_shader else \
            self.backend_render.context.program(CustomShader._DEFAULT_VERTEX_SHADER, CustomShader._DEFAULT_FRAGMENT_SHADER)
        
        self.__vao = game.backend_render.context.vertex_array(self.__program, [(self.backend_render.vbo, "2f 2f", "inPos", "inUv")], index_buffer=self.backend_render.ebo)
        


    def setPosition(self, x: float, y: float):
        self.__Position = self.__glm.vec2(x, y)

    def setSize(self, w: float, h: float):
        self.__Size = self.__glm.vec2(w, h)

    def setLayer(self, layer: int):
        self.__Layer = layer
        self.renderer.needSort = True

    def setAlpha(self, alpha: float):
        self.__Alpha = alpha

    def setTexture(self, id: str):
        self.__Texture = self.game.resources._getItemImage(id) or self.backend_render.createNonTexture()


    def getLayer(self):
        return self.__Layer
    
    def getSize(self):
        return self.__Size
    
    def getAlpha(self):
        return self.__Alpha
    
    def getPosition(self):
        return self.__Position

    
    def showMe(self):
        self.__Texture.use(0)

        self.__program["GclAlpha"] = self.__Alpha
        self.__program["GclTexture"] = 0

        self.__program["unPos"] = self.__Position
        self.__program["unSize"] = self.__Size

        self.__vao.render()

        

    