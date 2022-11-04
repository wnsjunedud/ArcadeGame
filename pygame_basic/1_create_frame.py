import pygame

pygame.init() ##Initialization (must)

# Set screen size
screen_width = 480 #screen horizontal size
screen_height = 640 #screen vertical size
screen = pygame.display.set_mode((screen_width, screen_height))

# Set screen title
pygame.display.set_caption("Start") #GameName

# Event Loop
running = True # Is the game in progress?
while running:
    for event in pygame.event.get(): #What event occurred?
        if event.type == pygame.QUIT: # Did the window close event occur?
            running = False

# pygame ends
pygame.quit()