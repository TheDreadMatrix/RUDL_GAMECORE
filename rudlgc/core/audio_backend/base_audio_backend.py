


class BaseAudioBackend:
    def __init__(self, game):
        self.settings = game.settings
        self.resources = game.resources
        self.audio = game._requirements.audio

        self.volumeAutoSavingBySettings = True


    def playMusic(self, item_id, count_loop=999): pass
    
    def setVolumeMusic(self, volume):pass

    def pauseMusic(self, item_id): pass
    
    def resumeMusic(self, item_id): pass

    def fadeInMusic(self, item_id, count_loop=999, ms=2000): pass

    def fadeOutMusic(self, item_id, ): pass

