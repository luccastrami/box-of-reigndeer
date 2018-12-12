import pygame
from utils.location import Location
import random
from highlight_token import HighlightToken

class MRFMap(object):
    def __init__(self, width, height, message_pump):
        self.message_pump = message_pump
        self.message_pump.register(self)
        self.curlevel = 1
        self.player_location = Location(0, 0)
        
        self.changed_level = False

        self.mapsprite = pygame.sprite.Sprite()
        self.mapsprite.image = pygame.image.load("map.jpg").convert()
        self.mapsprite.image= pygame.transform.scale(self.mapsprite.image,(width, height))
        self.mapsprite.rect = self.mapsprite.image.get_rect()
        self.location = Location(0,0)
        self.tokens = []
        self.tokens.append(HighlightToken(112,183, "1"))
        self.tokens.append(HighlightToken(180,243, "4"))
        self.tokens.append(HighlightToken(256,267, "5"))
        self.tokens.append(HighlightToken(316,310, "6"))
        self.tokens.append(HighlightToken(378,275, "7"))
        self.tokens.append(HighlightToken(436,250, "8"))
        
    def update(self):
            if pygame.key.get_pressed()[pygame.K_e] != 0:
                if self.changed_level is not False:
                    print("duplicate e pressed on map")
                    return 
                for t in self.tokens:
                    if t.hit_check(self.player_location.x, self.player_location.y) is True:
                        print("MRF_map is changing level to {} player {},{}".format(t.level_name, self.player_location.x, self.player_location.y))
                        self.message_pump.send_message("change level", t.level_name)
            else:
                 self.changed_level = False

    def reset(self):
        for t in self.tokens:
            t.highlighted=False
        self.changed_level = False
                    
    def message(self, msg_type, msg):
        if msg_type == "change level":
            print("Got a message {} {}".format(msg, self.changed_level))
            
        if msg_type == "change level" and self.changed_level is False:
            if self.curlevel == 3:
                print("reset")
                self.reset()
                
            if msg == "3":
                self.changed_level = True
                self.curlevel = 3
                self.player_location.x = 0
                self.player_location.y = 0
#                print("loading map on map.py")
            else:
                self.curlevel = 1

                       
        elif msg_type == "player location" and self.curlevel == 3:
           
            x = msg.split(" ")[0]
            x = int(x)
            y = msg.split(" ")[1]
            y = int(y)
            self.player_location.x = x
            self.player_location.y = y
            for t in self.tokens:
                t.hit_check(x, y)

#            print("{} : {} , [{}] mrf_map.py".format(x, y, type(x)))

            
    def draw(self, screen):
#        if self.curlevel != 3:
#            print("ERROR: Should not be able to call this when not on level 3")
        #draw map stuff - ie. all the map bits
        screen.blit(self.mapsprite.image, self.location.get_loc())

        for t in self.tokens:
            t.draw(screen)
