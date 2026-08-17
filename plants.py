import arcade
import sun_farm
import animka
import time
import Pea
class Plant(animka.Anim):
    def __init__(self,image,hp,cost,window):
        super().__init__(image,0.12)
        self.hp=hp
        self.cost=cost
        self.row=0
        self.column=0
        self.window = window


    def update(self):
        eat_zombies=arcade.check_for_collision_with_list(self,self.window.zombiess)
        for zombie in eat_zombies:
            if zombie.row==self.row:
                zombie.eating=True
                self.hp-=0.5
                if self.hp<=0:
                    self.kill()
                    zombie.eating=False


    def planting(self,cx,cy,row,column):
        self.center_x=cx
        self.center_y=cy
        self.row=row
        self.column=column




class Sun_Flower(Plant):
    def __init__(self,window):
        super().__init__("plants/sun1.png",80,50,window=window)
        for i in range(1,3):
            self.append_texture(arcade.load_texture(f"plants/sun{i}.png"))
        self.sun_spawn_time=time.time()



    def update(self):
        super().update()
        if time.time()-self.sun_spawn_time>=3:
            new_sun=sun_farm.Sun()
            new_sun.center_x=self.right
            new_sun.center_y=self.top
            self.window.suns.append(new_sun)
            self.sun_spawn_time = time.time()





class Nut(Plant):
    def __init__(self,window):
        super().__init__("plants/nut1.png",225,50,window=window)
        for i in range(1,4):
            self.append_texture(arcade.load_texture(f"plants/nut{i}.png"))

class PeaShooter(Plant):
    def __init__(self,window):
        super().__init__("plants/pea1.png",100,100,window=window)
        for i in range(1,4):
            self.append_texture(arcade.load_texture(f"plants/pea{i}.png"))
        self.shoot_time=time.time()


    def update(self):
        super().update()
        if time.time()-self.shoot_time>=2:
            pea=Pea.Pea()
            pea.center_x=self.center_x+10
            pea.center_y = self.center_y + 20
            self.window.peas.append(pea)
            self.shoot_time = time.time()


class Tree(Plant):
    def __init__(self,window):
        super().__init__("plants/tree1.png",125,175,window=window)
        for i in range(1,4):
            self.append_texture(arcade.load_texture(f"plants/tree{i}.png"))


    def update(self):
        super().update()
        fire_peas=arcade.check_for_collision_with_list(self,self.window.peas)
        for pea in fire_peas:
            pea.texture=arcade.load_texture("items/firebul.png")
            pea.damage=4


