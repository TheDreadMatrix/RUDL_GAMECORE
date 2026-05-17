from rudlgc.core.graphic_backend.base_graphic_backend import BaseGraphicBackend
from rudlgc.core import _callOnce


class OpenGLBackend(BaseGraphicBackend):
    NAME_CONTEXT = "OpenGL"
    NAME_VERSION = "3.3.0"
    def __init__(self, game):
        super().__init__(game)
        self.mgl = game._requirements.mgl

        
    @_callOnce()
    def showInfo(self):
        self.game.logger._system_log("INFO", self.context.info)

    @_callOnce()
    def createFlags(self):
        flags = self.sdl.SDL_WINDOW_OPENGL
        if self.settings._WINDOW_MODE != 0:
            if self.settings._WINDOW_MODE == 1:
                flags |= self.sdl.SDL_WINDOW_RESIZABLE
            elif self.settings._WINDOW_MODE == 2:
                flags |= self.sdl.SDL_WINDOW_BORDERLESS
            elif self.settings._WINDOW_MODE == 3:
                flags |= self.sdl.SDL_WINDOW_FULLSCREEN_DESKTOP
        return flags
    
    @_callOnce()
    def createVersion(self):
        self.sdl.SDL_GL_SetAttribute(self.sdl.SDL_GL_CONTEXT_PROFILE_MASK, self.sdl.SDL_GL_CONTEXT_PROFILE_CORE)
        self.sdl.SDL_GL_SetAttribute(self.sdl.SDL_GL_CONTEXT_MAJOR_VERSION, 3)
        self.sdl.SDL_GL_SetAttribute(self.sdl.SDL_GL_CONTEXT_MINOR_VERSION, 3)

        self.sdl.SDL_GL_SetAttribute(self.sdl.SDL_GL_MULTISAMPLEBUFFERS, 1)
        self.sdl.SDL_GL_SetAttribute(self.sdl.SDL_GL_MULTISAMPLESAMPLES, 4) 
        self.sdl.SDL_GL_SetAttribute(self.sdl.SDL_GL_DOUBLEBUFFER, 1)
        
    @_callOnce()
    def createContext(self):
        # SDL CONTEXT
        self.sdl.SDL_GL_CreateContext(self.game._window.window)

        # CONTEXT
        self.context = self.mgl.create_context()

        self.enable(self.mgl.DEPTH_TEST)
        self.enable(self.mgl.BLEND)

        self.context.blend_func = (self.mgl.SRC_ALPHA, self.mgl.ONE_MINUS_SRC_ALPHA)

        # BUFFER AND PROJECTION
        self.projection_2d = self.glm.ortho(0, self.settings._WINDOW_WIDTH, 0, self.settings._WINDOW_HEIGHT, -1, 1)

        self.ubo = self.context.buffer(reserve=1024)
        self.ubo.bind_to_uniform_block(0)
        self.ubo.write(self.projection_2d.to_bytes())

        self.vbo = self.context.buffer(self.vertices)
        self.ebo = self.context.buffer(self.indices)



    def setProjectile2D(self, width, height):
        self.projection_2d = self.glm.ortho(0, width, height, 0, -1, 1)
        self.ubo.write(self.projection_2d.to_bytes())

                         
    def createTexture(self, path):
        img = self.pil.open(path).convert("RGBA")
        
        texture = self.context.texture(img.size, 4, img.tobytes())
        texture.filter = (self.mgl.LINEAR, self.mgl.LINEAR)

        return texture
    

    
    def createNonTexture(self):
        texture = self.context.texture((256, 256), 3, self.UNDEFINED_TEXTURE_BYTE)
        texture.filter = (self.mgl.LINEAR, self.mgl.LINEAR)
        
        return texture
        



    def setPointSize(self, size):
        self.context.point_size = size

    def setLineWidth(self, width):
        self.context.line_width = width

    def setViewPort(self, width, height):
        self.context.viewport = (0, 0, width, height)

    def clearColor(self, r, g, b):
        self.context.clear(r, g, b)


    def enable(self, flag):
        self.context.enable(flag)
