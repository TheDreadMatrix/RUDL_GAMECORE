from rudlgc.core.graphic_backend.base_graphic_backend import BaseGraphicBackend




class VulkanBackend(BaseGraphicBackend):
    NAME_CONTEXT = "Vulkan"
    def __init__(self, game):
        super().__init__(game)