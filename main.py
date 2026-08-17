import time
import Zombies
import arcade
import random
from Constans import *
import plants
import arcade.gui



#####Сделать кнопку выхода из игры(arcade.exit())
def justify_x(pos_x):
    column=1
    right_x=245+CELL_WIDTH
    while right_x<pos_x:
        right_x+=CELL_WIDTH
        column+=1
    cell_center_x=right_x-CELL_WIDTH/2
    return cell_center_x,column




def justify_y(pos_y):
    row=1
    top_y=34+CELL_HEIGHT
    while top_y<pos_y:
        top_y+=CELL_HEIGHT
        row+=1
    cell_center_y=top_y-CELL_HEIGHT/2
    return cell_center_y,row


class Window(arcade.Window):
    def __init__(self):
        super().__init__(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, title=SCREEN_TITLE)
        self.bg = arcade.load_texture("textures/background.jpg")
        self.menu_bg = arcade.load_texture("textures/menu_vertical.png")
        self.plants=arcade.SpriteList()
        self.temp_plant=None
        self.plants_coords=[]
        self.sun_money=500
        self.suns=arcade.SpriteList()
        self.peas=arcade.SpriteList()
        self.zombiess=arcade.SpriteList()
        self.zombie_time=time.time()
        self.lose_bg=arcade.load_texture("textures/end.png")
        self.game=False
        self.main_menu=True
        self.start_menu_bg=arcade.load_texture("textures/screensaver.jpg")


        ##UI Manager
        self.ui_manager=arcade.gui.UIManager()
        self.ui_manager.enable()
        ##Buttons
        self.start_button=arcade.gui.UITextureButton(width=400,height=200,texture=arcade.load_texture("textures/1c2029f28dab612.png"))
        self.start_button.on_click=self.start_game
        self.ui_manager.add(arcade.gui.UIAnchorWidget(anchor_x="center",anchor_y="center",align_y=30,child=self.start_button))


        self.start_button=arcade.gui.UITextureButton(width=400,height=200,texture=arcade.load_texture("textures/fba764d369e0b325ba029ace897c2de4.png"))
        self.start_button.on_click=self.exit_game
        self.ui_manager.add(arcade.gui.UIAnchorWidget(anchor_x="center",anchor_y="center",align_y=-175,child=self.start_button))
    def start_game(self,event):
        if self.main_menu:
            self.main_menu=False
            self.game=True


    def exit_game(self,event):
        if self.main_menu:
            self.main_menu=False
            arcade.exit()


    def on_draw(self):
        arcade.start_render()
        if not self.main_menu:
            arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.bg)
            arcade.draw_texture_rectangle(67, SCREEN_HEIGHT / 2, 134, SCREEN_HEIGHT, self.menu_bg)
            self.plants.draw()
            self.suns.draw()
            self.zombiess.draw()
            if self.temp_plant != None:
                self.temp_plant.draw()
            self.peas.draw()
            arcade.draw_text(f"{self.sun_money}",8,500,(0,0,0),25,117,"center")
            if not self.game:
                arcade.draw_texture_rectangle(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,SCREEN_WIDTH,SCREEN_HEIGHT,self.lose_bg)
        else:
            arcade.draw_texture_rectangle(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,SCREEN_WIDTH,SCREEN_HEIGHT,self.start_menu_bg)
            self.ui_manager.draw()
    def update(self, delta_time: float):
        if self.game:
            self.plants.update()
            self.plants.update_animation(delta_time)
            self.suns.update()
            self.peas.update()
            self.zombiess.update()
            self.zombiess.update_animation(delta_time)
            if time.time()-self.zombie_time>=5:
                zombie_chance=random.randint(1,10)
                center_y, row = justify_y(random.randint(35, 540))
                if 1<=zombie_chance<=5:
                    new_zombie=Zombies.Normal_zombie(center_y,row,self)
                elif 6<=zombie_chance<=8:
                    new_zombie = Zombies.Cone_zombie(center_y, row,self)
                else:
                    new_zombie = Zombies.Bucket_zombie(center_y, row,self)
                self.zombiess.append(new_zombie)
                self.zombie_time=time.time()






    def setup(self):
        pass

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if self.game:
            print(x,y)
            if 18<=x<=110:
                if 382<=y<=474:
                    print("Солнышко")
                    self.temp_plant=plants.Sun_Flower(self)
                if 271<=y<=360:
                    print("Горошек")
                    self.temp_plant=plants.PeaShooter(self)
                if 157<=y<=247:
                    print("Орех")
                    self.temp_plant = plants.Nut(self)
                if 41<=y<=131:
                    print("мудрое дерево со сгоревшими мозгами")
                    self.temp_plant = plants.Tree(self)
            if self.temp_plant != None:
                self.temp_plant.center_x=x
                self.temp_plant.center_y=y
                self.temp_plant.alpha=150
            for sun in self.suns:
                if sun.left<=x<=sun.right and sun.bottom<=y<=sun.top:
                    sun.kill()
                    self.sun_money+=50



    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        if self.temp_plant != None:
            self.temp_plant.center_x=x
            self.temp_plant.center_y=y



    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
        if LEFT_FIELD_SIDE<=x<=965 and 35<=y<=540 and self.temp_plant != None:
            plant_cx,column=justify_x(x)
            plant_cy,row=justify_y(y)
            if (row,column) in self.plants_coords or self.temp_plant.cost>self.sun_money:
                self.temp_plant=None
                return
            self.temp_plant.planting(plant_cx,plant_cy,row,column)
            self.sun_money-=self.temp_plant.cost
            self.plants_coords.append((row,column))
            print(self.plants_coords)
            self.temp_plant.alpha=255
            self.plants.append(self.temp_plant)
            self.temp_plant=None
        else:
            self.temp_plant=None



window = Window()
window.setup()
arcade.run()
