

class Renderer:
    def __init__(self):
        self.sprites = []
        self.needSort = True




    def render(self):
        if self.needSort:
            self.sprites.sort(key=lambda s: s.getLayer())
            self.needSort = False

        for sprite in self.sprites:
            sprite.showMe()