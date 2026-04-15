import vulkan as vk
import sdl2
import sdl2.ext



sdl2.ext.init()

window = sdl2.ext.Window("Test Vulcan", size=(800, 600), flags=sdl2.SDL_WINDOW_VULKAN | sdl2.SDL_WINDOW_RESIZABLE)

app_info = vk.VkInstanceCreateInfo(sType=vk.VK_STRUCTURE_TYPE_APPLICATION_INFO, 
    pApplicationName="MyEngine",
    applicationVersion=1,
    pEngineName="RUDLGC",
    engineVersion=1,
    apiVersion=vk.VK_API_VERSION_1_2
)

instance_info = vk.VkInstanceCreateInfo(
    sType=vk.VK_STRUCTURE_TYPE_INSTANCE_CREATE_INFO,
    pApplicationInfo=app_info
)

instance = vk.vkCreateInstance(instance_info, None)




running = True


while running:
    for event in sdl2.ext.get_events():
        if event.type == sdl2.QUIT:
            running = False



sdl2.Quit()
