import arcade
import time

class Sun(arcade.Sprite):
    def __init__(self):
        super().__init__("items/sun.png",0.2)
        self.sun_timer=time.time()


    def update(self):
        self.angle+=3
        if time.time()-self.sun_timer>=2:
            self.kill()