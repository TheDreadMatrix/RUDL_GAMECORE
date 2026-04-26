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


    _DEFAULT_VERTEX_SHADER = textwrap.dedent("""
        #version 330 core
        
        in vec2 inPos;
        in vec2 inUv;
                                             
        layout(std140) uniform Projection{
            mat4 unProj;
        };

        out vec2 GclUv;

        uniform vec2 unSize;
        uniform vec2 unPos;
        


        void main(){
            vec2 finalPos = inPos * unSize + unPos;

            gl_Position = unProj * vec4(finalPos, 0.0, 1.0);


            GclUv = inUv;                                
        }                           
    """)

    _DEFAULT_FRAGMENT_SHADER = textwrap.dedent("""
        #version 330 core
                                               
        in vec2 GclUv;
                                               
        out vec4 GclColor;
        
        uniform float GclAlpha;
        uniform sampler2D GclTexture;
                                               
        void main(){
            GclColor = texture(GclTexture, GclUv) * vec4(1, 1, 1, GclAlpha);                             
        }
    """)

    def __init__(self, game, *folders: tuple[str], filename: str):
        file_path = game.paths.getShadersPath(*folders, file=filename)



        self._program = None


    def __setattr__(self, name, value):
        pass


    def __getattr__(self, name):
        pass




