
#There we import 'GameType' for anotation and 'AbstractScene' for ours scene
from rudlgc.contrib import GameType, PackageScene
from rudlgc.rudlums import MouseNum, KeyNum, MessageNum


class ExampleScene(PackageScene):
    #This method is designed to initialize (create) objects.
    #Here you create objects once, which is better
    def __init__(self, game: GameType):
        super().__init__(game)
    
        self.window_api.setTitle("Hello world")

    #This method is called every frame. 
    def onUpdate(self):
        #self.api.setWindowTitle(f"{self.game.getFps()}")

        if self.keyboard.isPress(KeyNum.A):
            self.logger.trace("A")

        


    def onFixedUpdate(self):
        pass
        
    

    #This method is called on any event, such as clicking, changing focus, etc.                      
    def onEvent(self, event):
        if self.event_api.isResized(event):
            self.window_api.setTitle(f"{self.settings.WINDOW_WIDTH}x{self.settings.WINDOW_HEIGHT}")
        
            

    #The method is called after 'onUpdate' is created to draw objects              
    def onRender(self):
        self.window_api.clearColor(0.0, 0.8, 0.9)

        

    #The method is called when the scene switches to another, otherwise the useful date must save here             
    def onSave(self):
        pass
