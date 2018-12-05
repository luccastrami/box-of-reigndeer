import pygame
from utils.location import Location
from utils.rect import Rect

class Player(object):
    def __init__(self, message_pump):
        self.curlevel = 0
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
        
        self.levels = []
        level0 = []
        self.levels.append(level0)
        level1 = []
        self.levels.append(level1)
        level2 = []
        bed_rect = Rect(185, 170, 195, 100)
        cushion_rect = Rect(0,0,110,250)
        cushion_rect_2 = Rect(0,0,90, 280)
        stove_rect = Rect(0,0,66,340)
        level2.append(bed_rect)
        level2.append(cushion_rect)
        level2.append(cushion_rect_2)
        level2.append(stove_rect)
        self.levels.append(level2)
        
        self.facing = "right"
       
    def message(self, msg_type, msg):
        if msg_type == "change level":
            if msg == "1":
                self.location.x = 50
                self.location.y = 440
                self.curlevel = 1
            if msg == "2":
                self.curlevel = 2

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
            self.location.x -= 2

        if pygame.key.get_pressed()[pygame.K_RIGHT] != 0:
            self.facing = "right"
            # We need to move to the RIGHT
            self.location.x += 2

        if pygame.key.get_pressed()[pygame.K_UP] != 0:
            # We need to move UP
            self.location.y -= 2
            
        if pygame.key.get_pressed()[pygame.K_DOWN] != 0:
            # We need to move to the DOWN
            self.location.y += 2
            
        # Make sure we can't leave the screen
        if self.location.x > 386:
            self.location.x = 386
            
        if self.location.x < 0:
            self.location.x = 0
            
        if self.location.y > 440:
            self.location.y = 440

        if self.location.y < 0:
            self.location = 0
            
        #Level specific boundary checks
        if self.curlevel == 1:
            if self.location.y < 230:
                self.location.y = 230
        elif self.curlevel == 2:
            bHit = False
            for r in self.levels[2]:
                if r.hit_test(self.location.x, self.location.y):
                    self.location.x = old_x
                    self.location.y = old_y
                    bHit = True

            # Now check the boundaries
            if self.location.y < 230:
                self.location.y = 230
            if self.location.x > 500:
                self.location.x = 500

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
