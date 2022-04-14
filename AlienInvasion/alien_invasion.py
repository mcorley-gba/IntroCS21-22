"""
alien_invasion.py --.

 make a new folder called AlienInvasion in IntroCS.
"""

import sys  # Gives more control for system resources (e.g., windowing)
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create all game resources."""
        pygame.init()
        # Initializes background settings that
        # Pygame needs to do its job(s)

        self.settings = Settings()
        # Pulls in the settings from the "Settings"
        # class. So they are accessible from the main file

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion")
        #Creating a caption at the top of the new window

        #Initialize stats:
        self.stats = GameStats(self)
        
        self.ship = Ship(self)
            #Create a ship attribute for the game by instantiating
            #   the ship class   .
        
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
            self._update_screen()

    def _update_bullets(self):
        """Update position of bullets and get rid of off-screen bullets."""
        #First, update positions
        self.bullets.update()

        #Get rid of off-screen bullets:
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        
        #Check if any bullets have hit alien ships
        #If yes, get rid of bullet and the alien
        self._check_bullet_alien_collisions()
    
    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions"""
        #Remove bullets and aliens that have collided
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        #Respawn the fleet if all aliens are destroyed
        if not self.aliens:
            #Destroy existing bullets; create new fleet
            self.bullets.empty()
            self._create_fleet()


    def _update_aliens(self):
        """Check if the fleet is at an edge
            Then update all alien positions accordingly."""
        self._check_fleet_edges()
        self.aliens.update()

        #Look for alien-ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        
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
        self.aliens.draw(self.screen)

        #Make the game screen visible
        pygame.display.flip()

    def _create_fleet(self):
        """Create the fleet of aliens using the Sprite
        Group abilities"""
        #Make one alien and add it to the group of aliens
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2*alien_width)
        number_aliens_x = available_space_x // (2*alien_width)

        #Determine the number of rows that will fit.
        ship_height = self.ship.rect.height
        available_space_y = self.settings.screen_height - (3*alien_height) - ship_height
        number_rows = available_space_y //(2*alien_height)

        #Create the fleet
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number,row_number):
        #create an alien and place in the new row.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + (2*alien_width*alien_number)
        alien.rect.x = alien.x
        alien.rect.y = alien_height + (2*alien.rect.height*row_number)
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the fleet, then move the other direction horizontally."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1 

    def _ship_hit(self):
        """Respond appropriately to the ship being hit by an alien"""
        #Decrease the number of ships remaining
        self.stats.ships_left -= 1

        #Remove aliens and bullets
        self.aliens.empty()
        self.bullets.empty()

        #Make a new fleet & center a new ship
        self._create_fleet()
        self.ship.center_ship()

        #Pause to let player get ready for a new round
        sleep(0.5)



if __name__ == '__main__':
    #Make a game instance, and run the game
    ai = AlienInvasion() #Initializes a game
    ai.run_game() #Runs the game
