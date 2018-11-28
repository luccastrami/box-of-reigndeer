import pygame
from player import Player
from pygame.locals import KEYDOWN
# from message_pump import MessagePump

def update():
    # Here we update the game to move elements
    player.update()

def draw(screen):
    # Here we draw each component to the screen
    screen.fill([55, 55, 55])

    # Draw our player and asteroid objects
    player.draw(screen)
    pygame.display.update()

def run():

    quit = False
    while quit == False:
        # If we are told to quit then we will quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit = True

        # Call our update function
        update()
        # Call our draw function
        draw(screen)

        # Wait before calculating the next movement
        pygame.time.wait(20)
    pygame.quit()


if __name__=='__main__':
    global player
    global background
    global tent
    global screen
    
    # message_pump = MessagePump()

    Screen_Width = 600
    Screen_Height = 480

    # Initialize the PyGame module
    pygame.init()
    screen = pygame.display.set_mode([Screen_Width, Screen_Height])

    # Make our player and asteroid objects
    # TODO: Be able to specify the sprite sheet
    player = Player()
    run()