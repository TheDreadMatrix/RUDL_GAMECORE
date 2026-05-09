JOSHUA SETTINGS IN self.game.settings

change|load CONSTANT save them to your file 

V0.1.1
['rudlgc', 'rudlgc.core', 'rudlgc.core.execute_prompt', 'rudlgc.core.templates', 'rudlgc.core.templates.templates', 'rudlgc.core.templates.functions', 'rudlgc.core.subsystems.logger_core', 'rudlgc.core.subsystems.request_core', 'rudlgc.core.subsystems.settings_core', 'rudlgc.core.subsystems.paths_core', 'rudlgc.core.subsystems', 'rudlgc.core.execute_game', 'rudlgc.contrib.package_type', 'rudlgc.contrib.package_scenes', 'rudlgc.contrib.package_model', 'rudlgc.contrib', 'rudlgc.rudlums', 'rudlgc.johnson']


V0.1.2
['rudlgc', 'rudlgc.core', 'rudlgc.core.execute_prompt', 'rudlgc.core.templates', 'rudlgc.core.templates.templates', 'rudlgc.core.templates.functions', 'rudlgc.core.subsystems.logger_core', 'rudlgc.core.subsystems.api_game.request_core', 'rudlgc.core.subsystems.api_game.window_api', 'rudlgc.core.subsystems.api_game.event_api', 'rudlgc.core.subsystems.api_game.system_api', 'rudlgc.core.subsystems.api_game', 'rudlgc.core.subsystems.settings_core', 'rudlgc.core.subsystems.paths_core', 'rudlgc.core.subsystems', 'rudlgc.core.subsystems.input_game.inputs', 'rudlgc.core.subsystems.input_game', 'rudlgc.core.backends', 'rudlgc.core.backends.base_backend', 'rudlgc.core.backends.opengl', 'rudlgc.core.execute_game', 'rudlgc.contrib.package_type', 'rudlgc.contrib.package_scenes', 'rudlgc.contrib.package_model', 'rudlgc.contrib', 'rudlgc.rudlums', 'rudlgc.johnson']

['rudlgc', 'rudlgc.core', 'rudlgc.core.execute_prompt', 'rudlgc.core.templates', 'rudlgc.core.templates.templates', 'rudlgc.core.templates.functions', 'rudlgc.core.subsystems', 'rudlgc.core.subsystems.logger_core', 'rudlgc.core.subsystems.api_game.config_api', 'rudlgc.core.subsystems.api_game.window_api', 'rudlgc.core.subsystems.api_game.event_api', 'rudlgc.core.subsystems.api_game.system_api', 'rudlgc.core.subsystems.api_game', 'rudlgc.core.subsystems.requirements', 'rudlgc.johnson', 'rudlgc.core.subsystems.settings_core', 'rudlgc.core.subsystems.paths_core', 'rudlgc.core.subsystems.control_core', 'rudlgc.core.graphic_backend', 'rudlgc.core.graphic_backend.base_graphic_backend', 'rudlgc.core.graphic_backend.opengl', 'rudlgc.core.execute_game', 'AAA_game', 'AAA_game.settings', 'rudlgc.packages.package_typing', 'rudlgc.rudlums', 'rudlgc.rendering.custom_shader', 'rudlgc.rendering.renderer', 'rudlgc.rendering.sprite_render', 'rudlgc.rendering', 'rudlgc.packages.package_scenes', 'rudlgc.packages', 'rudlgc.packages.package_model', 'AAA_game.scenes.example', 'AAA_game.scenes', 'AAA_game.router']


['rudlgc', 'rudlgc.core', 'rudlgc.core.execute_prompt', 'rudlgc.core.templates', 'rudlgc.core.templates.templates', 'rudlgc.core.templates.functions', 'rudlgc.core.execute_game', 'rudlgc.core.subsystems', 'rudlgc.core.subsystems.logger_core', 'rudlgc.core.subsystems.requirements', 'rudlgc.core.subsystems.settings_core', 'rudlgc.core.subsystems.paths_core', 'rudlgc.core.subsystems.control_core', 'AAA_game', 'rudlgc.johnson', 'rudlgc.rudlums', 'AAA_game.settings', 'rudlgc.core.graphic_backend', 'rudlgc.core.graphic_backend.base_graphic_backend', 'rudlgc.core.graphic_backend.opengl', 'rudlgc.core.subsystems.api_ game.config_api', 'rudlgc.core.subsystems.api_game.window_api', 'rudlgc.core.subsystems.api_game.event_api', 'rudlgc.core.subsystems.api_game.system_api', 'rudlgc.core.subsystems.api_game', 'rudlgc.packages.package_typing', 'rudlgc.rendering.custom_shader', 'rudlgc.rendering.renderer', 'rudlgc.rendering.sprite_render', 'rudlgc.rendering', 'rudlgc.packages.package_scenes', 'rudlgc.packages', 'rudlgc.packages.package_model', 'AAA_game.scenes', 'AAA_game.scenes.example', 'AAA_game.scenes.main', 'AAA_game.router']


Custom json settings must be:
your_custom_settings.json must be in PROJECT-NAME/.saves/

{
    "window": {
        "window-size": {
            "width": 800,
            "height": 600,
            "min-width": 799,
            "min-height": 599
        },
        "window-attr": {
            "vsync": 0,
            "fullscreen": false,
            "borderless": false,
            "resizable": true
        }
    },

    "audio": {
        "sound-volume": 1.0,
        "music-volume": 1.0
    },

    "frametime": 240

    "custom-audio": {...}
}



in PROJECT-NAME/router.py we write in init

self.settings_data = Joshua(...)
self.settings_dataread = self.settings_data.readData()
 
self.load_settings(self.settings_dataread)

and in savingProgress we write

self.save_settings()



CustomShader:

#include gcl

void main(){
    GclColor = GCL_getBaseShaderColor();
}


->->->

#version 330 core

in vec2 GclUv;
out vec4 GclColor;

uniform sampler2D GclTexture;
uniform float GclAlpha;


vec4 GCL_getBaseShaderColor(){
    return texture(GclTexture, GclUv) * vec4(0, 0, 0, GclAlpha);
}



void main(){
    GclColor = GCL_getBaseShaderColor();
}





game.resources

game.resources.addImage(path, id: str)
game.resources.addMusic(path, id: str)

game.resources.removeImage(path, id: str)


game.resouces._getItemImage(id: str)











game.resources.addMusic(..., "my-music")


self.music.playMusic("my-music")
self.music.autoSavingBySettings = True


self.music.stopMusic("my-music")
