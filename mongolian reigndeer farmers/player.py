import pygame
from utils import Location

class Player(object):
    def __init__(self, message_pump):
        self.message_pump = message_pump
        self.message_pump.register(self)
        
        self.location = Location(50,440)
        self.size = Location(40, 40)

        self.countdown = 10
        self.cur_offset = 0
        self.reversing = False
        self.COOLDOWN = 5
        self.sprites = []
       
        self.sprites.append( pygame.sprite.Sprite() )
        self.sprites[0].image = pygame.image.load("lewis_character_5.png").convert_alpha()
        self.sprites[0].rect = self.sprites[0].image.get_rect()
        self.sprites.append( pygame.sprite.Sprite() )
        self.sprites[1].image = pygame.image.load("lewis_character_5_left.png").convert_alpha()
        self.sprites[1].rect = self.sprites[1].image.get_rect()
        
        self.facing = "right"
       
    def message(self, msg_type, msg):
        pass

    def update_walking_sprite(self):
        self.countdown -= 1
        if self.countdown < 1:
            self.countdown = self.COOLDOWN
            if self.reversing is False:
                self.cur_offset += 50
                if self.cur_offset >= 250:
                    self.cur_offset = 150
                    self.reversing = True
            else:
                self.cur_offset -= 50
                if self.cur_offset < 0:
                    self.cur_offset = 50
                    self.reversing = False

    def update(self):
        # To track whether we have actually moved or not
        old_x = self.location.x
        old_y = self.location.y

        if pygame.key.get_pressed()[pygame.K_LEFT] != 0:
            self.facing = "left"
            # We need to move to the LEFT
            self.location.x -= 3

        if pygame.key.get_pressed()[pygame.K_RIGHT] != 0:
            self.facing = "right"
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

        if self.location.y < 280:
            self.location.y = 280
        
        if self.location.x != old_x or self.location.y != old_y:
            self.update_walking_sprite()
            # Only update everyone on our location if we have actually moved - otherwise this is a waste
            self.message_pump.send_message("player location","{} {}".format(self.location.x, self.location.y))
        else:
            self.cur_offset = 100
            self.countdown = self.COOLDOWN

    def draw(self, screen):
        if self.facing == "left":
            screen.blit(self.sprites[1].image, self.location.get_loc(), (self.cur_offset,0,50,100))    
        else:
            screen.blit(self.sprites[0].image, self.location.get_loc(), (self.cur_offset,0,50,100))
       
    def reset(self):
        self.destroy()

    def destroy(self):
        # Reset back to our location
        self.location.x = 300
        self.location.y = 430
