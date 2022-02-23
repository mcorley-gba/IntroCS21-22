#alien_invasion.py -- make a new folder called AlienInvasion 
# in IntroCS

import sys #Gives more control for system resources (e.g., windowing)

import pygame

from settings import Settings

class AlienInvasion:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game, and create all game resources"""
        pygame.init() #Initializes background settings that 
                        #Pygame needs to do its job(s)

        self.settings = Settings()
            #Pulls in the settings from the "Settings"
            # class. So they are accessible from the main file

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )

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

            self.screen.fill(self.settings.bg_color)
                #Redraw the screen with correct bg color each loop

            #Make the game screen visible
            pygame.display.flip()

if __name__ == '__main__':
    #Make a game instance, and run the game
    ai = AlienInvasion() #Initializes a game
    ai.run_game() #Runs the game