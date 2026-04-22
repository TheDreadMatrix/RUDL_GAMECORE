from rudlgc.contrib import GameType
import textwrap


class CustomShader:
    _FRAGMENT_HEADER_REPLACER = textwrap.dedent("""
        #version 330 core
                                     
        in vec2 GclUv;
        out vec4 GclColor;
                                              
        uniform sampler2D GclTexture;
        uniform float GclAlpha;
        
        vec4 GCL_getBasicsShaderColor(){
            return texture(GclTexture, GclUv) * vec4(0, 0, 0, GclAlpha);
        }
    """)

    def __init__(self, game: GameType, *folders: tuple[str], filename: str):
        mgl = game._requirements.mgl

        file_path = game.paths.getShadersPath(*folders, file=filename)



        self._program = None


    def __setattr__(self, name, value):
        pass


    def __getattr__(self, name):
        pass




