#alien_invasion.py -- make a new folder called AlienInvasion 
# in IntroCS

import sys #Gives more control for system resources (e.g., windowing)

import pygame

class AlienInvasion:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game, and create all game resources"""
        pygame.init() #Initializes background settings that 
                        #Pygame needs to do its job(s)

        self.screen = pygame.display.set_mode((1200,800))
            #Creates a window for the game at 1200 pixels by 800 pixels
        pygame.display.set_caption("Alien Invasion")
            #Creating a caption at the top of the new window

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            #Tell pygame to watch for keyboard and mouse events
            for event in pygame.event.get():
                    #pygame.event.get() is a function that
                    #returns a list of any key/mouse events that
                    #have taken place
                    #Any keypresses or mouse-clicks will initiate
                    #this loop.
                if event.type == pygame.QUIT:
                    sys.exit()
            #Make the game screen visible
            pygame.display.flip()

if __name__ == '__main__':
    #Make a game instance, and run the game
    ai = AlienInvasion() #Initializes a game
    ai.run_game() #Runs the game