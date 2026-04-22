from rudlgc.core.backends import BaseClassBackend



class OpenGLBackend(BaseClassBackend):
    NAME_CONTEXT = "OPENGL"
    def __init__(self, settings, requirements):
        # SETTINGS
        self.mgl = requirements.mgl
        self.glm = requirements.glm5
        self.subInitBufferData(self.glm)


        # CONTEXT
        self.context = self.mgl.create_context()

        self.setViewPort(settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT)
        self.setPointSize(settings.POINT_SIZE)
        self.setLineWidth(settings.LINE_SIZE)

        self._enable(self.mgl.DEPTH_TEST)
        self._enable(self.mgl.BLEND)

        self.context.blend_func = (self.mgl.SRC_ALPHA, self.mgl.ONE_MINUS_SRC_ALPHA)

        # BUFFER AND PROJECTION
        self.projection_2d = self.glm.ortho(0, settings.WINDOW_WIDTH, 0, settings.WINDOW_HEIGHT, -1, 1)

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
