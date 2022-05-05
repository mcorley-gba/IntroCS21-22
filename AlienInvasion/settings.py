#settings.py
class Settings:
    """Initialize game settings."""
    
    def __init__(self):
        """Initialize settings"""
        #Initialize Static Settings
        #Screen Settings:
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230,230,230)

        #Ship settings:
        self.ship_limit = 3

        #Bullet settings:
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 5

        #Alien Settings
        self.fleet_drop_speed = 50

        #Game speed-up amount
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize Settings that change through the game"""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        self.fleet_direction = 1 #1=right; -1=left
        #Adding fleet_direction*fleet_speed will automatically move l/r
        self.alien_points = 10

    def increase_speed(self):
        """Increase speed settings"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
