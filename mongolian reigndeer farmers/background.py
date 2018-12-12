import pygame
from utils.location import Location
from mrf_map import MRFMap
import random

class Background(object):
    def __init__(self, width, height, message_pump, tent):
        self.tent = tent
        self.message_pump = message_pump
        self.message_pump.register(self)
        self.curlevel = 1
        self.location = Location(0,0)
        self.reset() #Randomly pick a starting location
        self.player_location = Location(0,0)
#        self.size = Location(40,40)
        self.forestsprite = pygame.sprite.Sprite()
        self.forestsprite.image = pygame.image.load("start location.jpg").convert()
        self.forestsprite.image= pygame.transform.scale(self.forestsprite.image,(width, height))
        self.forestsprite.rect = self.forestsprite.image.get_rect()
        
        self.forestsprite2 = pygame.sprite.Sprite()
        self.forestsprite2.image = pygame.image.load("location 2.jpg").convert()
        self.forestsprite2.image= pygame.transform.scale(self.forestsprite2.image,(width, height))
        self.forestsprite2.rect = self.forestsprite2.image.get_rect()
        
        self.forestsprite3 = pygame.sprite.Sprite()
        self.forestsprite3.image = pygame.image.load("location 3.jpg").convert()
        self.forestsprite3.image= pygame.transform.scale(self.forestsprite3.image,(width, height))
        self.forestsprite3.rect = self.forestsprite3.image.get_rect()

        self.forestsprite4 = pygame.sprite.Sprite()
        self.forestsprite4.image = pygame.image.load("location 4.jpg").convert()
        self.forestsprite4.image= pygame.transform.scale(self.forestsprite4.image,(width, height))
        self.forestsprite4.rect = self.forestsprite4.image.get_rect()
        
        self.forestsprite5 = pygame.sprite.Sprite()
        self.forestsprite5.image = pygame.image.load("location 5.jpg").convert()
        self.forestsprite5.image= pygame.transform.scale(self.forestsprite5.image,(width, height))
        self.forestsprite5.rect = self.forestsprite5.image.get_rect()
        
        self.forestsprite6 = pygame.sprite.Sprite()
        self.forestsprite6.image = pygame.image.load("location 6.jpg").convert()
        self.forestsprite6.image= pygame.transform.scale(self.forestsprite6.image,(width, height))
        self.forestsprite6.rect = self.forestsprite6.image.get_rect()
        
        self.yurtsprite = pygame.sprite.Sprite()
        self.yurtsprite.image = pygame.image.load("yurt inside.jpg").convert()
        self.yurtsprite.image= pygame.transform.scale(self.yurtsprite.image,(width, height))
        self.yurtsprite.rect = self.yurtsprite.image.get_rect()
        
        self.mapsprite = pygame.sprite.Sprite()
        self.mapsprite.image = pygame.image.load("map.jpg").convert()
        self.mapsprite.image= pygame.transform.scale(self.mapsprite.image,(100, 45))
        self.mapsprite.rect = self.mapsprite.image.get_rect()
        
        self.map = MRFMap(width, height, message_pump)
        self.changed_level = False
        
    def update(self):
        self.changed_level = False
        if self.curlevel == 2:
            if self.player_location.x >380 and self.player_location.x <470:
                if self.player_location.y >=230 and self.player_location.y <250:

                    if pygame.key.get_pressed()[pygame.K_e] != 0:
                        print("press e")
                        self.message_pump.send_message("change level", "3")
        elif self.curlevel == 3:
#            print("update map...")
            self.map.update()
#            self.facing = "e"
#            # We need to move to the LEFT
#            self.location.x -= 2

    def message(self, msg_type, msg):
        if msg_type == "change level" and self.changed_level is False:
            self.changed_level = True
            self.curlevel = int(msg)
            if msg == "1":
#                self.curlevel = 1
                print("loading first location")
            elif msg == "2":
#                self.curlevel = 2
                print("loading tent")
            elif msg == "3":
#                self.curlevel = 3
                print("loading map in background.py")
            elif msg == "4":
#                self.curlevel = 4
                pass
                
            else:
                print("ERROR: Unkown level in background.py {}".format(msg))
                
        elif msg_type == "player location" and self.curlevel == 2:
            x = msg.split(" ")[0]
            x = int(x)
            y = msg.split(" ")[1]
            y = int(y)
            self.player_location.x = x
            self.player_location.y = y
            if y > 420:
                print("Going to level 1")
                self.message_pump.send_message("change level",self.tent.return_level)
           
        
            print("{} : {} , [{}] background.py".format(x, y, type(x)))
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
        elif self.curlevel == 4:
            screen.blit(self.forestsprite2.image, self.location.get_loc())
        elif self.curlevel == 5:
            screen.blit(self.forestsprite3.image, self.location.get_loc())
        elif self.curlevel == 6:
            screen.blit(self.forestsprite4.image, self.location.get_loc())
        elif self.curlevel == 7:
            screen.blit(self.forestsprite5.image, self.location.get_loc())
        elif self.curlevel == 8:
            screen.blit(self.forestsprite6.image, self.location.get_loc())
            
    def check_collision(self, obj):
        # Check if the two objects are touching
        diffx = self.location.x - obj.location.x
        diffy = obj.location.y - self.location.y
        if diffx < self.size.x and diffx > (self.size.x * -1):
            if diffy < self.size.y and diffy > (self.size.y * -1):
                return True
        return False
