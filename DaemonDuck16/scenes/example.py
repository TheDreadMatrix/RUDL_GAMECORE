
#There we import 'GameType' for anotation and 'AbstractScene' for ours scene
from rudlgc.packages import GameType, PackageScene

class ExampleScene(PackageScene):
    #This method is designed to initialize (create) objects.
    #Here you create objects once, which is better
    def __init__(self, game: GameType):
        super().__init__(game)

    #This method is called every frame.                    
    def onUpdate(self):
        pass

    #This method is called every tick                
    def onFixedUpdate(self):
        pass

    #This method is called on any event, such as clicking, changing focus, etc.                      
    def onEvent(self, event):
        pass

    #The method is called after 'onUpdate' is created to draw objects              
    def onRender(self):
        pass

    #The method is called when the scene switches to another, otherwise the useful date must save here             
    def onSave(self):
        super().onSave()

