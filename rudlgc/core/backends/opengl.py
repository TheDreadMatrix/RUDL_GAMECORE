from rudlgc.core.backends import BaseClassBackend



class OpenGLBackend(BaseClassBackend):
    NAME_CONTEXT = "OPENGL"
    def __init__(self, game):
        super().__init__(game)
        self.mgl = game._requirements.mgl

        

    def showInfo(self):
        self.game.logger._system_log("INFO", self.context.info)

    def createFlags(self):
        flags = self.sdl.SDL_WINDOW_OPENGL
        if self.settings.RESIZABLE:
            flags |= self.sdl.SDL_WINDOW_RESIZABLE
        if self.settings.BORDERLESS:
            flags |= self.sdl.SDL_WINDOW_BORDERLESS
        if self.settings.FULLSCREEN:
            flags |= self.sdl.SDL_WINDOW_FULLSCREEN_DESKTOP
        return flags
    

    def createVersion(self):
        if self.settings.GRAPHICS_API == "OPENGL":
            self.game.logger._system_log("WARNING", "Created OpenGL context")
            self.sdl.SDL_GL_SetAttribute(self.sdl.SDL_GL_CONTEXT_PROFILE_MASK, self.sdl.SDL_GL_CONTEXT_PROFILE_CORE)
            self.sdl.SDL_GL_SetAttribute(self.sdl.SDL_GL_CONTEXT_MAJOR_VERSION, 3)
            self.sdl.SDL_GL_SetAttribute(self.sdl.SDL_GL_CONTEXT_MINOR_VERSION, 3)
        elif self.settings.GRAPHICS_API == "OPENGL_ES":
            self.game.logger._system_log("WARNING", "Created OpenGL ES context")
            self.sdl.SDL_GL_SetAttribute(self.sdl.SDL_GL_CONTEXT_PROFILE_MASK,  self.sdl.SDL_GL_CONTEXT_PROFILE_ES)
            self.sdl.SDL_GL_SetAttribute(self.sdl.SDL_GL_CONTEXT_MAJOR_VERSION, 3)
            self.sdl.SDL_GL_SetAttribute(self.sdl.SDL_GL_CONTEXT_MINOR_VERSION, 0)

        self.sdl.SDL_GL_SetAttribute(self.sdl.SDL_GL_MULTISAMPLEBUFFERS, 1)
        self.sdl.SDL_GL_SetAttribute(self.sdl.SDL_GL_MULTISAMPLESAMPLES, 4) 
        self.sdl.SDL_GL_SetAttribute(self.sdl.SDL_GL_DEPTH_SIZE, 24)
        self.sdl.SDL_GL_SetAttribute(self.sdl.SDL_GL_ALPHA_SIZE, 8)
        self.sdl.SDL_GL_SetAttribute(self.sdl.SDL_GL_DOUBLEBUFFER, 1)
        

    def createContext(self):
        # SDL CONTEXT
        self.sdl.SDL_GL_CreateContext(self.game._window.window)
        self.sdl.SDL_GL_SetSwapInterval(self.settings.VSYNC) 

        # CONTEXT
        self.context = self.mgl.create_context()

        self.setViewPort(self.settings.WINDOW_WIDTH, self.settings.WINDOW_HEIGHT)
        self.setPointSize(self.settings.POINT_SIZE)
        self.setLineWidth(self.settings.LINE_SIZE)

        self._enable(self.mgl.DEPTH_TEST)
        self._enable(self.mgl.BLEND)

        self.context.blend_func = (self.mgl.SRC_ALPHA, self.mgl.ONE_MINUS_SRC_ALPHA)

        # BUFFER AND PROJECTION
        self.projection_2d = self.glm.ortho(0, self.settings.WINDOW_WIDTH, 0, self.settings.WINDOW_HEIGHT, -1, 1)

        self.ubo = self.context.buffer(reserve=1024)
        self.ubo.bind_to_uniform_block(0)
        self.ubo.write(self.projection_2d.to_bytes())

        self.vbo = self.context.buffer(self.vertices)
        self.ebo = self.context.buffer(self.indices)



    def setProjectile2D(self, width, height):
        self.projection_2d = self.glm.ortho(0, width, 0, height, -1, 1)
        self.ubo.write(self.projection_2d.to_bytes())


    def setPointSize(self, size):
        self.context.point_size = size

    def setLineWidth(self, width):
        self.context.line_width = width

    def setViewPort(self, width, height):
        self.context.viewport = (0, 0, width, height)

    def clearColor(self, r, g, b):
        self.context.clear(r, g, b)


    def _enable(self, flag):
        self.context.enable(flag)
