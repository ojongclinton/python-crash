class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings"""
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1.5
        self.alien_speed = 7.0
        self.bullet_width = 5
        self.bullet_speed = 4
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5
        self.ship_limit = 3
        self.fleet_drop_speed = 10
        #fleet direction
        self.fleet_direction = 1
