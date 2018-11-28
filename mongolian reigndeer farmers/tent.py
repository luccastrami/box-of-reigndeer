import pygame
from utils import Location
import random

class Tent(object):
    def __init__(self, message_pump):
        self.message_pump = message_pump
        self.message_pump.register(self)
        
        self.location = Location(10,150)
#        self.reset() #Randomly pick a starting location

#        self.size = Location(40,40)
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = pygame.image.load("yurt.png").convert_alpha()
        self.sprite.image= pygame.transform.scale(self.sprite.image,(300, 250))
#        self.sprite.image = self.sprite.image.convert_alpha()
        self.sprite.rect = self.sprite.image.get_rect()

    def update(self):
        pass
#        self.location.y += 10
#        if self.location.y > 500:
#            self.reset()
    def message(self, msg_type, msg):
        if msg_type == "change level":
            if msg == "1":
                print("loading first level")
            elif msg == "2":
                self.location.x += 100
                print("loading second level")

    def reset(self):
        # We have reached the bottom of the screen so reset
#        self.location.y = 0
#        self.location.x = random.randint(0, 560)
        pass

    def draw(self, screen):
        screen.blit(self.sprite.image, self.location.get_loc())

    def check_collision(self, obj):
        # Check if the two objects are touching
        diffx = self.location.x - obj.location.x
        diffy = obj.location.y - self.location.y
        if diffx < self.size.x and diffx > (self.size.x * -1):
            if diffy < self.size.y and diffy > (self.size.y * -1):
                return True
        return False
