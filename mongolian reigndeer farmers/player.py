import pygame
from utils import Location

class Player(object):
    def __init__(self, message_pump):
        self.curlevel = 0
        self.message_pump = message_pump
        self.message_pump.register(self)
        
        self.location = Location(50,440)
        self.size = Location(40, 40)

        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = pygame.image.load("player.png").convert()
        self.sprite.rect = self.sprite.image.get_rect()
    
    def message(self, msg_type, msg):
        if msg_type == "change level":
            if msg == "1":
                self.location.x = 50
                self.location.y = 440
                self.curlevel = 1
            if msg == "2":
                self.curlevel = 2

    def update(self):
        # To track whether we have actually moved or not
        old_x = self.location.x
        old_y = self.location.y

        if pygame.key.get_pressed()[pygame.K_LEFT] != 0:
            # We need to move to the LEFT
            self.location.x -= 3

        if pygame.key.get_pressed()[pygame.K_RIGHT] != 0:
            # We need to move to the RIGHT
            self.location.x += 3

        if pygame.key.get_pressed()[pygame.K_UP] != 0:
            # We need to move UP
            self.location.y -= 3
            
        if pygame.key.get_pressed()[pygame.K_DOWN] != 0:
            # We need to move to the DOWN
            self.location.y += 3
            
        # Make sure we can't leave the screen
        if self.location.x > 560:
            self.location.x = 560
            
        if self.location.x < 0:
            self.location.x = 0
            
        if self.location.y > 440:
            self.location.y = 440

        if self.location.y < 0:
            self.location = 0
            
        #Level specific boundary checks
        if self.curlevel == 1:
            if self.location.y < 280:
                self.location.y = 280
        elif self.curlevel == 2:
            if self.location.y < 300:
                self.location.y = 300
            if self.location.x < 66:
                self.location.x = 66
            if self.location.x > 500:
                self.location.x = 500
        if self.location.x != old_x or self.location.y != old_y:
            # Only update everyone on our location if we have actually moved - otherwise this is a waste
            self.message_pump.send_message("player location","{} {}".format(self.location.x, self.location.y))
            
    def draw(self, screen):
        screen.blit(self.sprite.image, self.location.get_loc())

    def reset(self):
        self.destroy()

    def destroy(self):
        # Reset back to our location
        self.location.x = 300
        self.location.y = 430
