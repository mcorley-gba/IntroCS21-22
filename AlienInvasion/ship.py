#ship.py
import pygame

class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set starting location"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #Load the ship image, and get its rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
    
    def blitme(self):
        """Draw the ship on the screen at its current location"""
        self.screen.blit(self.image, self.rect)

        #Pygame sees the screen as a coordinate grid with (0,0)
        #is in the top left corner. So the point (1200,800) is the 
        #bottom right corner

