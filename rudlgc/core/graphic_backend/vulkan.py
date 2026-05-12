from rudlgc.core.graphic_backend.base_graphic_backend import BaseGraphicBackend




class VulkanBackend(BaseGraphicBackend):
    NAME_CONTEXT = "Vulkan"
    NAME_VERSION = "1.0.0"
    def __init__(self, game):
        super().__init__(game)