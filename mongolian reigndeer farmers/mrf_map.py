import pygame
from utils import Location
import random

class MRFMap(object):
    def __init__(self, width, height, message_pump):
        self.message_pump = message_pump
        self.message_pump.register(self)
        self.curlevel = 1
        
        self.forestsprite = pygame.sprite.Sprite()
        self.forestsprite.image = pygame.image.load("location 2.jpg").convert()
        self.forestsprite.image= pygame.transform.scale(self.forestsprite.image,(width, height))
        self.forestsprite.rect = self.forestsprite.image.get_rect()

#        self.yurtsprite = pygame.sprite.Sprite()
#        self.yurtsprite.image = pygame.image.load("yurt inside.jpg").convert()
#        self.yurtsprite.image= pygame.transform.scale(self.yurtsprite.image,(width, height))
#        self.yurtsprite.rect = self.yurtsprite.image.get_rect()
#        
#        self.yurtsprite = pygame.sprite.Sprite()
#        self.yurtsprite.image = pygame.image.load("yurt inside.jpg").convert()
#        self.yurtsprite.image= pygame.transform.scale(self.yurtsprite.image,(width, height))
#        self.yurtsprite.rect = self.yurtsprite.image.get_rect()
        
    def update(self):
        pass

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

    def draw(self, screen):
        if self.curlevel != 3:
            print("ERROR: Should not be able to call this when not on level 3")
        #draw map stuff - ie. all the map bits
        screen.blit(self.yurtsprite.image, self.location.get_loc())
