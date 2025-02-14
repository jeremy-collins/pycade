from time import sleep
import pygame
from controllers.main import getMainController
from utils.colors import YELLOW
from gamePicker import GamePicker


SCREEN_SIZE = (400, 400)
SPEED = 1

screens = []


# define a main function
def main():
    # initialize the pygame module
    pygame.init()
    pygame.joystick.init()
    pygame.display.set_caption("PYCADE")

    clock = pygame.time.Clock()

    # create a surface on screen
    screen = pygame.display.set_mode(SCREEN_SIZE)

    # define a variable to control the main loop
    running = True
    controller = getMainController()
    gameHolder = GamePicker(SCREEN_SIZE, screen)
    frameCount = 0
    lastActions = set()
    lastDrawTime = 0
    shouldUpdateScreen = False

    print("Using Controller", controller)

    # main loop
    while running:

        # Pause for next frame
        deltaTime = clock.tick(30)
        deltaTime = 0
        totalTimeLapsed = pygame.time.get_ticks()
        frameCount += 1
        gameHolder.currentGame.setTimes(frameCount, deltaTime, totalTimeLapsed)

        # If set, can't be unset
        shouldUpdateScreen = gameHolder.currentGame.update() or shouldUpdateScreen

        timeSinceLastDraw = pygame.time.get_ticks() - lastDrawTime

        # 60 frames a second
        if timeSinceLastDraw > 1000 / 60 and shouldUpdateScreen:
            lastDrawTime = pygame.time.get_ticks()
            shouldUpdateScreen = False
            screen.fill(YELLOW)
            gameHolder.currentGame.draw()
            pygame.display.update()

        actions = controller.getActions()
        gameHolder.currentGame.setActions(actions)


        # event handling, gets all event from the event queue
        # for event in pygame.event.get():
        #     # only do something if the event is of type QUIT
        #     if event.type == pygame.QUIT:
        #         # change the value to False, to exit the main loop
        #         running = False


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
