import pygame
from player import Player
from background import Background
from tent import Tent
from pygame.locals import KEYDOWN
from message_pump import MessagePump

def update():
    # Here we update the game to move elements
    player.update()

def draw(screen):
    # Here we draw each component to the screen
    screen.fill([0, 0, 0])

    # Draw our player and asteroid objects
    background.draw(screen)
    tent.draw(screen)
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
    global message_pump
    
    message_pump = MessagePump()

    Screen_Width = 600
    Screen_Height = 480

    # Initialize the PyGame module
    pygame.init()
    screen = pygame.display.set_mode([Screen_Width, Screen_Height])

    # Make our player and asteroid objects
    player = Player()
    background = Background(Screen_Width, Screen_Height, message_pump)
    tent = Tent(message_pump)
    message_pump.send_message("change level","1")
    run()