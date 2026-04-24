JOSHUA SETTINGS IN self.game.settings

change|load CONSTANT save them to your file 

V0.1.1
['rudlgc', 'rudlgc.core', 'rudlgc.core.execute_prompt', 'rudlgc.core.templates', 'rudlgc.core.templates.templates', 'rudlgc.core.templates.functions', 'rudlgc.core.subsystems.logger_core', 'rudlgc.core.subsystems.request_core', 'rudlgc.core.subsystems.settings_core', 'rudlgc.core.subsystems.paths_core', 'rudlgc.core.subsystems', 'rudlgc.core.execute_game', 'rudlgc.contrib.package_type', 'rudlgc.contrib.package_scenes', 'rudlgc.contrib.package_model', 'rudlgc.contrib', 'rudlgc.rudlums', 'rudlgc.johnson']


V0.1.2
['rudlgc', 'rudlgc.core', 'rudlgc.core.execute_prompt', 'rudlgc.core.templates', 'rudlgc.core.templates.templates', 'rudlgc.core.templates.functions', 'rudlgc.core.subsystems.logger_core', 'rudlgc.core.subsystems.api_game.request_core', 'rudlgc.core.subsystems.api_game.window_api', 'rudlgc.core.subsystems.api_game.event_api', 'rudlgc.core.subsystems.api_game.system_api', 'rudlgc.core.subsystems.api_game', 'rudlgc.core.subsystems.settings_core', 'rudlgc.core.subsystems.paths_core', 'rudlgc.core.subsystems', 'rudlgc.core.subsystems.input_game.inputs', 'rudlgc.core.subsystems.input_game', 'rudlgc.core.backends', 'rudlgc.core.backends.base_backend', 'rudlgc.core.backends.opengl', 'rudlgc.core.execute_game', 'rudlgc.contrib.package_type', 'rudlgc.contrib.package_scenes', 'rudlgc.contrib.package_model', 'rudlgc.contrib', 'rudlgc.rudlums', 'rudlgc.johnson']


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


