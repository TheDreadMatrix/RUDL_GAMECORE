


class BaseClassBackend:
    def __init__(self):
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