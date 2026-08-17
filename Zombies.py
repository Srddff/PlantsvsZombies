import arcade
import animka
from Constans import SCREEN_WIDTH,LEFT_FIELD_SIDE

class Zombie(animka.Anim):
    def __init__(self,image,hp,center_y,row,window):
        super().__init__(image,0.9)
        self.hp=hp
        self.center_y=center_y
        self.row=row
        self.change_x=0.2 #0.2
        self.center_x=SCREEN_WIDTH
        self.window=window
        self.eating=False

    def update(self):
        if not self.eating:
            self.center_x-=self.change_x

        hit_peas=arcade.check_for_collision_with_list(self,self.window.peas)
        for pea in hit_peas:
            self.hp-=pea.damage
            pea.kill()
        if self.hp<=0:
            self.kill()
        if self.left<LEFT_FIELD_SIDE:
            self.window.game=False


class Normal_zombie(Zombie):
    def __init__(self,center_y,row,window):
        super().__init__("zombies/OrdinaryZombie/Zombie_0.png",15,center_y,row,window)
        for i in range(22):
            self.append_texture(arcade.load_texture(f"zombies/OrdinaryZombie/Zombie_{i}.png"))

class Cone_zombie(Zombie):
    def __init__(self,center_y,row,window):
        super().__init__("zombies/ConeheadZombie/ConeheadZombie_0.png",20,center_y,row,window)
        for i in range(21):
            self.append_texture(arcade.load_texture(f"zombies/ConeheadZombie/ConeheadZombie_{i}.png"))

class Bucket_zombie(Zombie):
    def __init__(self,center_y,row,window):
        super().__init__("zombies/BucketheadZombie/BucketheadZombie_0.png",25,center_y,row,window)
        for i in range(15):
            self.append_texture(arcade.load_texture(f"zombies/BucketheadZombie/BucketheadZombie_{i}.png"))