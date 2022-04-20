#settings.py
class Settings:
    """Initialize game settings."""
    
    def __init__(self):
        #Screen Settings:
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230,230,230)

        #Ship settings:
        self.ship_speed = 1.5
        self.ship_limit = 3

        #Bullet settings:
        self.bullet_speed = 10.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 5

        #Alien Settings
        self.alien_speed = 10.0
        self.fleet_drop_speed = 50
        self.fleet_direction = 1 #1=right; -1=left
        #Adding fleet_direction*fleet_speed will automatically move l/r
