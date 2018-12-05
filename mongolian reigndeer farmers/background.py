import pygame
from utils.location import Location
from mrf_map import MRFMap
import random

class Background(object):
    def __init__(self, width, height, message_pump):
        self.message_pump = message_pump
        self.message_pump.register(self)
        self.curlevel = 1
        self.location = Location(0,0)
        self.reset() #Randomly pick a starting location

#        self.size = Location(40,40)
        self.forestsprite = pygame.sprite.Sprite()
        self.forestsprite.image = pygame.image.load("start location.jpg").convert()
        self.forestsprite.image= pygame.transform.scale(self.forestsprite.image,(width, height))
        self.forestsprite.rect = self.forestsprite.image.get_rect()

        self.yurtsprite = pygame.sprite.Sprite()
        self.yurtsprite.image = pygame.image.load("yurt inside.jpg").convert()
        self.yurtsprite.image= pygame.transform.scale(self.yurtsprite.image,(width, height))
        self.yurtsprite.rect = self.yurtsprite.image.get_rect()
        
        self.mapsprite = pygame.sprite.Sprite()
        self.mapsprite.image = pygame.image.load("map.jpg").convert()
        self.mapsprite.image= pygame.transform.scale(self.mapsprite.image,(100, 45))
        self.mapsprite.rect = self.mapsprite.image.get_rect()
        
        self.map = MRFMap(width, height, message_pump)
        
    def update(self):
        pass
#        self.location.y += 10
#        if self.location.y > 500:
#            self.reset()
    def message(self, msg_type, msg):
        if msg_type == "change level":
            if msg == "1":
                self.curlevel = 1
                print("loading first level")
            elif msg == "2":
                self.curlevel = 2
                print("loading second level")
            elif msg == "3":
                self.curlevel = 3
        elif msg_type == "player location" and self.curlevel == 2:
            x = msg.split(" ")[0]
            x = int(x)
            y = msg.split(" ")[1]
            y = int(y)
            if y > 420:
                print("Going to level 1")
                self.message_pump.send_message("change level","1")
            print("{} : {} , [{}]".format(x, y, type(x)))
    def reset(self):
        # We have reached the bottom of the screen so reset
#        self.location.y = 0
#        self.location.x = random.randint(0, 560)
        pass

    def draw(self, screen):
#        screen.blit(self.forestsprite.image, self.location.get_loc())
        if self.curlevel == 1:
            screen.blit(self.forestsprite.image, self.location.get_loc())
        elif self.curlevel == 2:
            screen.blit(self.yurtsprite.image, self.location.get_loc())
            screen.blit(self.mapsprite.image, (410, 220))
        elif self.curlevel == 3:
            self.map.draw(screen)
            
    def check_collision(self, obj):
        # Check if the two objects are touching
        diffx = self.location.x - obj.location.x
        diffy = obj.location.y - self.location.y
        if diffx < self.size.x and diffx > (self.size.x * -1):
            if diffy < self.size.y and diffy > (self.size.y * -1):
                return True
        return False
