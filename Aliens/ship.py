import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """A Class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize ship, set starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #Load the ship, get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #Start each ship at bottom center of screen
        self.rect.midbottom = self.screen_rect.midbottom

        #Store decimal value for horiz position
        self.x = float(self.rect.x)

        #Movement Flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flags."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        #Update rect object from self.x
        self.rect.x = self.x

    def center_ship(self):
        """center the ship on the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)


    def blitme(self):
        """Draw the ship at current location."""
        self.screen.blit(self.image, self.rect)