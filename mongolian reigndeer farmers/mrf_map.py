import pygame
from utils.location import Location
import random

class MRFMap(object):
    def __init__(self, width, height, message_pump):
        self.message_pump = message_pump
        self.message_pump.register(self)
        self.curlevel = 1
        
        self.mapsprite = pygame.sprite.Sprite()
        self.mapsprite.image = pygame.image.load("map.jpg").convert()
        self.mapsprite.image= pygame.transform.scale(self.mapsprite.image,(width, height))
        self.mapsprite.rect = self.mapsprite.image.get_rect()
        self.location = Location(0,0)
        
    def update(self):
        pass

    def message(self, msg_type, msg):
        
        if msg_type == "change level":
            if msg == "1":
                self.curlevel = 1
                print("loading first level")
            elif msg == "2":
                self.curlevel = 2
                print("loading yurt")
            elif msg == "3":
                self.curlevel = 3
                print("loading map") 
            elif msg == "4":
                self.curlevel = 4
                print("loading second level")
            elif msg == "5":
                self.curlevel = 5
                print("loading third level")
            elif msg == "6":
                self.curlevel = 6
                print("loading forth level")
                       
        elif msg_type == "player location" and self.curlevel == 3:
            x = msg.split(" ")[0]
            x = int(x)
            y = msg.split(" ")[1]
            y = int(y)
            
            if x> 94 and x < 138:
                if y > 180 and y < 290:
                    self.message_pump.send_message("change level","4")#
            
            print("{} : {} , [{}]".format(x, y, type(x)))

            
    def draw(self, screen):
        if self.curlevel != 3:
            print("ERROR: Should not be able to call this when not on level 3")
        #draw map stuff - ie. all the map bits
        screen.blit(self.mapsprite.image, self.location.get_loc())
