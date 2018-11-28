import pygame
from utils import Location

class Player(object):
    def __init__(self):
        self.location = Location(100,100)
        self.size = Location(100, 50)
        self.countdown = 10
        self.cur_offset = 0
        self.reversing = False
        self.sprites = []
        for i in range (0, 4):
            self.sprites.append( pygame.sprite.Sprite() )
            self.sprites[i].image = pygame.image.load("lewis_character.png").convert_alpha()
            self.sprites[i].rect = self.sprites[i].image.get_rect()

    def update(self):
        # TODO: Move through the sprites
        self.countdown -= 1
        if self.countdown < 1:
            self.countdown = 10
            if self.reversing is False:
                self.cur_offset += 50
                if self.cur_offset >= 150:
                    self.cur_offset = 50
                    self.reversing = True
            else:
                self.cur_offset -= 50
                if self.cur_offset < 0:
                    self.cur_offset = 50
                    self.reversing = False
        pass

    def draw(self, screen):
        screen.blit(self.sprites[0].image, self.location.get_loc(), (self.cur_offset,0,50,100))

