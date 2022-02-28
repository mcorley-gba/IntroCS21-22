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
