
#There we import 'GameType' for anotation and 'AbstractScene' for ours scene
from rudlgc.contrib import GameType, AbstractScene
from rudlgc.rudlums import Evalent

class ExampleScene(AbstractScene):
    #This method is designed to initialize (create) objects.
    #Here you create objects once, which is better
    def __init__(self, game: GameType):
        self.game = game

        self.game.request.setWindowTitle(f"{self.game.getCurrentScene()}")
        
        
        

    #This method is called every frame.                    
    def onUpdate(self):
        self.game.request.setWindowTitle(f"{self.game.getFps()}")
        

    #This method is called on any event, such as clicking, changing focus, etc.                      
    def onEvent(self, event):
        if event.type == Evalent.KEY_DOWN:
            self.game.request.redirectScene('future-scene')
            

    #The method is called after 'onUpdate' is created to draw objects              
    def onRender(self):
        self.game.request.setScreenColor(0.0, 0.8, 0.9)
        

    #The method is called when the scene switches to another, otherwise the useful date must save here             
    def onSave(self):
        pass
