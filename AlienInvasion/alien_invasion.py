#alien_invasion.py -- make a new folder called AlienInvasion 
# in IntroCS

import sys  # Gives more control for system resources (e.g., windowing)

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create all game resources."""
        pygame.init()  # Initializes background settings that 
                       # Pygame needs to do its job(s)

        self.settings = Settings()
            #Pulls in the settings from the "Settings"
            # class. So they are accessible from the main file

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion")
            #Creating a caption at the top of the new window
        
        self.ship = Ship(self)
            #Create a ship attribute for the game by instantiating
            #   the ship class.
        
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()

            #Check to see if bullets are off the screen.
            #If yes, delete them.
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    #y-value less than zero = off top of screen
                    self.bullets.remove(bullet)
            print(len(self.bullets)) #will comment out later
            
            self._update_screen()
        
    def _check_events(self):
        """Respond to keypresses and mouse clicks"""
        #Tell pygame to watch for keyboard and mouse events
        for event in pygame.event.get():
                #pygame.event.get() is a function that
                #returns a list of any key/mouse events that
                #have taken place
                #Any keypresses or mouse-clicks will initiate
                #this loop.
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN: #Check if a key was pressed
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP: #Check if a key has been release
                self._check_keyup_events(event)
    
    def _check_keydown_events(self,event):
        """Respond to keypresses"""
        if event.key == pygame.K_RIGHT: #If key was right arrow, then...
            #Move the ship right
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            #Move the ship left
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit() #Now the user can press q to quit.
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to key releases"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the 
            Bullet Sprite Group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def _update_screen(self):
        """Update images on the screen, show(flip) new screen"""
        self.screen.fill(self.settings.bg_color)
            #Redraw the screen with correct bg color each loop
        self.ship.blitme() 
            #draw the ship in the game instance
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
            #Draw the bullets 1 by 1 using for loop
        #Make the game screen visible
        pygame.display.flip()



if __name__ == '__main__':
    #Make a game instance, and run the game
    ai = AlienInvasion() #Initializes a game
    ai.run_game() #Runs the game
