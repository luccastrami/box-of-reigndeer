from utils.location import Location
import pygame

class HighlightToken(object):
    def __init__(self, _x, _y, level):
        self.highlighted = False
        self.level_name = level
        self.location = Location(_x, _y)
        self.size = Location(80,80)

        self.tokensprite = pygame.sprite.Sprite()
        self.tokensprite.image = pygame.image.load("highlight_token.png").convert_alpha()
        self.tokensprite.image= pygame.transform.scale(self.tokensprite.image,( 20, 20))
        self.tokensprite.rect = self.tokensprite.image.get_rect()

    def draw(self, screen):
        if self.highlighted:
            screen.blit(self.tokensprite.image, self.location.get_loc())

    def hit_check(self, x, y):
        if x > self.location.x - (self.size.x/2) and x < self.location.x + (self.size.x/2):
            if y > self.location.y - (self.size.y/2) and y < self.location.y + (self.size.y/2):
                self.highlighted = True
                return True
        self.highlighted = False
        return False
