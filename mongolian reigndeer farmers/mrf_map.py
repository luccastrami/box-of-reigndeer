import pygame
from utils.location import Location
import random
from highlight_token import HighlightToken

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
        self.tokens = []
        self.tokens.append(HighlightToken(110,170))
        self.tokens.append(HighlightToken(178,230))
        
    def update(self):
#        if self.player_location.x = 112
#            if self.player_location.y = 148
#                
#                if pygame.key.get_pressed()[pygame.K_e] != 0:
#                    print("press e")
#        elif self.player_location.x = 178
#            if self.player_location.y = 204
#            
#                if pygame.key.get_pressed()[pygame.K_e] != 0:
#                    print("press e")
#        elif self.player_location.x = 256
#            if self.player_location.y = 228
#            
#                if pygame.key.get_pressed()[pygame.K_e] != 0:
#                    print("press e")
#        elif self.player_location.x = 314
#            if self.player_location.y = 270
#            
#                if pygame.key.get_pressed()[pygame.K_e] != 0:
#                    print("press e")
#        elif self.player_location.x = 380
#            if self.player_location.y = 240
#                
#                if pygame.key.get_pressed()[pygame.K_e] != 0:
#                    print("press e")
#        elif self.player_location.x = 438
#            if self.player_location.y = 214
#        
#                if pygame.key.get_pressed()[pygame.K_e] != 0:
#                    print("press e")

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
            
#            if x = 112
#                if y = 148
#                    self.message_pump.send_message("change level","4")
#            if x = 178
#                if y = 204
#                    self.message_pump.send_message("change level","4")
#            if x =  256
#                if y = 228
#                    self.message_pump.send_message("change level","4")
#            if x = 314
#                if y = 270
#                    self.message_pump.send_message("change level","4")
#            if x = 380
#                if y = 240
#                    self.message_pump.send_message("change level","4")
#            if x = 438
#                if y = 214
#                    self.message_pump.send_message("change level","4")
            
            for t in self.tokens:
                t.hit_check(x, y)

            print("{} : {} , [{}]".format(x, y, type(x)))

            
    def draw(self, screen):
#        if self.curlevel != 3:
#            print("ERROR: Should not be able to call this when not on level 3")
        #draw map stuff - ie. all the map bits
        screen.blit(self.mapsprite.image, self.location.get_loc())

        for t in self.tokens:
            t.draw(screen)
