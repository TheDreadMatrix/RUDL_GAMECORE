
#There we import 'GameType' for anotation and 'AbstractScene' for ours scene
from rudlgc.contrib import GameType, AbstractScene
from rudlgc.rudlums import Evalent, Keysym

class ExampleScene(AbstractScene):
    #This method is designed to initialize (create) objects.
    #Here you create objects once, which is better
    def __init__(self, game: GameType):
        self.game = game

        self.game.api.setWindowTitle(f"{self.game.getCurrentScene()}")
        #self.game.request.setWindowRelative(True)
        #self.game.request.setWindowGrab(True)
        self.game.logger.trace(self.game.settings.OS_PLATFORM)

    #This method is called every frame.                    
    def onUpdate(self):
        if self.game.keyboard.isPressed(Keysym.LEFT): self.game.logger.trace("LEFT")
        if self.game.keyboard.isPressed(Keysym.RIGHT): self.game.logger.trace("RIGHT")


        

    #This method is called on any event, such as clicking, changing focus, etc.                      
    def onEvent(self, event):
        pass
            

    #The method is called after 'onUpdate' is created to draw objects              
    def onRender(self):
        self.game.api.setScreenColor(0.0, 0.8, 0.9)
        

    #The method is called when the scene switches to another, otherwise the useful date must save here             
    def onSave(self):
        pass
