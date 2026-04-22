

class WindowManager:
    def __init__(self, game):
        self.sdl = game._requirements.sdl
        self.logger = game.logger
        self.settings = game.settings

    def _createFlagOpenGL(self):
        flags = self.sdl.SDL_WINDOW_OPENGL
        if self.settings.RESIZABLE:
            flags |= self.sdl.SDL_WINDOW_RESIZABLE
        if self.settings.BORDERLESS:
            flags |= self.sdl.SDL_WINDOW_BORDERLESS
        if self.settings.FULLSCREEN:
            flags |= self.sdl.SDL_WINDOW_FULLSCREEN_DESKTOP
        return flags


    def _createVersionOpenGL(self):
        if self.settings.GRAPHICS_API == "OPENGL":
            self.logger._system_log("WARNING", "Created OpenGL context")
            self.sdl.SDL_GL_SetAttribute(self.sdl.SDL_GL_CONTEXT_PROFILE_MASK, self.sdl.SDL_GL_CONTEXT_PROFILE_CORE)
            self.sdl.SDL_GL_SetAttribute(self.sdl.SDL_GL_CONTEXT_MAJOR_VERSION, 3)
            self.sdl.SDL_GL_SetAttribute(self.sdl.SDL_GL_CONTEXT_MINOR_VERSION, 3)
        elif self.settings.GRAPHICS_API == "OPENGL_ES":
            self.logger._system_log("WARNING", "Created OpenGL ES context")
            self.sdl.SDL_GL_SetAttribute(self.sdl.SDL_GL_CONTEXT_PROFILE_MASK,  self.sdl.SDL_GL_CONTEXT_PROFILE_ES)
            self.sdl.SDL_GL_SetAttribute(self.sdl.SDL_GL_CONTEXT_MAJOR_VERSION, 3)
            self.sdl.SDL_GL_SetAttribute(self.sdl.SDL_GL_CONTEXT_MINOR_VERSION, 0)

        self.sdl.SDL_GL_SetAttribute(self.sdl.SDL_GL_MULTISAMPLEBUFFERS, 1)
        self.sdl.SDL_GL_SetAttribute(self.sdl.SDL_GL_MULTISAMPLESAMPLES, 4) 
        self.sdl.SDL_GL_SetAttribute(self.sdl.SDL_GL_DEPTH_SIZE, 24)
        self.sdl.SDL_GL_SetAttribute(self.sdl.SDL_GL_ALPHA_SIZE, 8)
        self.sdl.SDL_GL_SetAttribute(self.sdl.SDL_GL_DOUBLEBUFFER, 1)