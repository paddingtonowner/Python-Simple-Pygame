class Settings():
    def __init__(self):
        self.bullet = {
            "speed_factor":1,
            "width":3,
            "height":15,
            "color":(60,60,60),
            "num":1,
            "allowed":3}
        self.ship = {
            "speed_factor":1.5}
        self.screen = {
            "width":1400,
            "height":800,
            "bgcolor":(0,255,0),
            "title":"Alien Invasion"}
        self.alien = {
            "group":[],
            "speed_factor":1,
            "drop_speed":10}
