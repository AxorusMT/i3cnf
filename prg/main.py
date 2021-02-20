import pygame

pygame.init()


PROG_RUN = True

def ON_PROG_QUIT(EXITCODE=1):
    print("The Program has quit\nProgram Information: Exitcode = " + EXITCODE)

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 700
WINDOW_TITLE = "Test Window"
WINDOW_DIM = (WINDOW_WIDTH, WINDOW_HEIGHT) #kinda pointless, but why not?
WINDOW = pygame.display.set_mode((WINDOW_DIM))
pygame.display.set_caption(WINDOW_TITLE)


#Main Game Loop
while PROG_RUN:
    for event in pygame.event.get():
        if event.type == pygame.QUIT():
            PROG_RUN = False

ON_PROG_QUIT()
