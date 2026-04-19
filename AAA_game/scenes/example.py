
#There we import 'GameType' for anotation and 'AbstractScene' for ours scene
from rudlgc.contrib import GameType, PackageScene
from rudlgc.rudlums import Keysym, Mouse
from rudlgc.johnson import Joshua, Xmlion


class ExampleScene(PackageScene):
    #This method is designed to initialize (create) objects.
    #Here you create objects once, which is better
    def __init__(self, game: GameType):
        super().__init__(game)

        self.api.setWindowTitle(f"{self.game.getCurrentScene()}")
        
        

    #This method is called every frame. 
    def onUpdate(self):
        pass


    def onFixedUpdate(self):
        pass
        
    

    #This method is called on any event, such as clicking, changing focus, etc.                      
    def onEvent(self, event):
        if self.mouse.mouseButtonDown(Mouse.LEFT, event):
            self.logger.trace("Left")

        if self.mouse.mouseButtonUp(Mouse.MIDDLE, event):
            self.logger.trace("Right")
        
            

    #The method is called after 'onUpdate' is created to draw objects              
    def onRender(self):
        self.api.setScreenColor(0.0, 0.8, 0.9)

        

    #The method is called when the scene switches to another, otherwise the useful date must save here             
    def onSave(self):
        pass
