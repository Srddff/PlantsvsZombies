import arcade


class Pea(arcade.Sprite):
    def __init__(self):
        super().__init__("items/bul.png",0.1)
        self.change_x=7
        self.damage=1

    def update(self):
        self.center_x+=self.change_x
