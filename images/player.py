import pygame
from utils.location import Location

class Player(object):
    def __init__(self):
        self.location = Location(100,100)
        self.size = Location(100, 50)
        self.countdown = 5
        self.cur_offset = 0
        self.reversing = False
        self.sprites = []
        for i in range (0, 6):
            self.sprites.append( pygame.sprite.Sprite() )
            self.sprites[i].image = pygame.image.load("lewis_character_5.png").convert_alpha()
            self.sprites[i].rect = self.sprites[i].image.get_rect()

    def update(self):
        # TODO: Move through the sprites
        self.countdown -= 1
        if self.countdown < 1:
            self.countdown = 5
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
        

    def draw(self, screen):
        screen.blit(self.sprites[0].image, self.location.get_loc(), (self.cur_offset,0,50,100))

