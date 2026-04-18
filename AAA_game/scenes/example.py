
#There we import 'GameType' for anotation and 'AbstractScene' for ours scene
from rudlgc.contrib import GameType, AbstractScene
from rudlgc.rudlums import Evalent, Keysym
from rudlgc.johnson import Joshua, Xmlion


class ExampleScene(AbstractScene):
    #This method is designed to initialize (create) objects.
    #Here you create objects once, which is better
    def __init__(self, game: GameType):
        self.game = game
        #JSON
        self.data_json = Joshua(self.game.paths.getConfigPath(file="test.json"))
        self.data_read_json = self.data_json.readData()
        self.data_read_json["count"] = 1000
        self.data_json.saveData(self.data_read_json)

        self.glm = self.game._requirements.glm5
        
        

        #XML
        self.data_xml = Xmlion(self.game.paths.getConfigPath(file="text.xml"))
        self.data_read_xml = self.data_xml.readXML()
        self.data_read_xml["hello"] = "123"
        
        self.game.logger.trace(self.game.settings.DEBUG)
        self.game.logger.traceMagenta(self.game.settings.GRAPHICS_API)


        self.game.api.setWindowTitle(f"{self.game.getCurrentScene()}")
        
        
        self.time_fps = 0
        self.time_tps = 0
        


    #This method is called every frame. 
    def onUpdate(self):
        self.time_fps += self.game.delta_time
        self.game.api.setWindowTitle(f"FPS: {self.time_fps:.2f} - TPS: {self.time_tps:.2f} - FRAMERATE: {int(self.game.getFps())}")


    def onFixedUpdate(self):
        self.time_tps += self.game.tick_time
        
        if self.game.keyboard.isPressed(Keysym.LEFT): self.game.logger.trace("LEFT")
        if self.game.keyboard.isPressed(Keysym.RIGHT): self.game.api.redirectScene('future-scene')
    

    #This method is called on any event, such as clicking, changing focus, etc.                      
    def onEvent(self, event):
        pass
            

    #The method is called after 'onUpdate' is created to draw objects              
    def onRender(self):
        self.game.api.setScreenColor(0.0, 0.8, 0.9)

        

    #The method is called when the scene switches to another, otherwise the useful date must save here             
    def onSave(self):
        self.data_xml.saveXML(self.data_read_xml)
