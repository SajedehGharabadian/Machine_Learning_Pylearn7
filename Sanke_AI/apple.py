import arcade
import random


class Apple(arcade.Sprite):
    def __init__(self,SCREEN_WIDTH,SCREEN_HEIGHT,wall_width):
        super().__init__()
        self.width = 15
        self.height = 15
        self.r = 15
        self.color = arcade.color.RED
        
        self.center_x  = random.randint(wall_width,(SCREEN_WIDTH-wall_width)) // wall_width * wall_width
        self.center_y = random.randint(wall_width,(SCREEN_HEIGHT-wall_width)) // wall_width * wall_width

    def draw(self):
        arcade.draw_circle_filled(self.center_x,self.center_y,self.r,self.color)  
