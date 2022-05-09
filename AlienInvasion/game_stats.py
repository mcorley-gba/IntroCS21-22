#game_stats.py
class GameStats:
    """Track stats for Alien Invasion"""

    def __init__(self, ai_game):
        """Initialize Stats"""
        self.settings = ai_game.settings
        self.reset_stats()

        #Start Alien Invasion in an inactive state.
        self.game_active = False

        #High Score (Should never be reset)
        self.high_score = 0

    def reset_stats(self):
        """Initialize stats that can change during the game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0