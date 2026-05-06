
#There we import 'GameType' for anotation and 'AbstractScene' for ours scene
from rudlgc.packages import GameType, PackageScene
from rudlgc.rudlums import MouseNum, KeyNum
from rudlgc.rendering.sprite_render import Sprite2D


class ExampleScene(PackageScene):
    #This method is designed to initialize (create) objects.
    #Here you create objects once, which is better
    def __init__(self, game: GameType):
        super().__init__(game)

        self.sprite = Sprite2D(game, renderer=self.renderer)
        self.sprite.setSize(self.settings.WINDOW_WIDTH, self.settings.WINDOW_HEIGHT)
        
        
        

        self.sprite_2 = Sprite2D(game, renderer=self.renderer)
        self.sprite_2.setSize(300, 450)
        
        
        self.x, self.y = 0, 0


    #This method is called every frame. 
    def onUpdate(self):
        self.window_api.setTitle(f"{self.game.getFps():.2f}")
        
        

    def onFixedUpdate(self):
        if self.keyboard.isPress(KeyNum.A):
            self.x -= 230 * self.game.tick_time

        if self.keyboard.isPress(KeyNum.D):
            self.x += 230 * self.game.tick_time


        self.sprite.setPosition(self.x, self.y)
        
    

    #This method is called on any event, such as clicking, changing focus, etc.                      
    def onEvent(self, event):
        if self.keyboard.isPressDown(KeyNum.R, event):
            self.config_api.setFps(300)
        elif self.keyboard.isPressDown(KeyNum.T, event):
            self.config_api.setFps(60)

        if self.mouse.mouseButtonDown(MouseNum.LEFT, event):
            self.game.raiseError()

        if self.event_api.isResized(event):
            self.settings.JOSEPH.set("width", self.settings.WINDOW_WIDTH)
            self.settings.JOSEPH.set("height", self.settings.WINDOW_HEIGHT)


        
            

    #The method is called after 'onUpdate' is created to draw objects              
    def onRender(self):
        self.window_api.clearColor(0.0, 0.8, 0.9)

        self.renderer.render()

        

    #The method is called when the scene switches to another, otherwise the useful date must save here             
    def onSave(self):
        super().onSave()
