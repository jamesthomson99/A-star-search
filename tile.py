import math

class Tile:
    def __init__(self):
        self.g = 0
        self.h = 0
        self.f = 0
        self.index = (-1, -1)
        self.is_start_point = False
        self.is_end_point = False
        self.is_obstacle = False
        self.connection = None

    def toggle_is_start_point(self):
        self.is_start_point = not self.is_start_point

    def toggle_is_end_point(self):
        self.is_end_point = not self.is_end_point

    def toggle_is_obstacle(self):
        self.is_obstacle = not self.is_obstacle

    def set_g(self, val):
        self.g = val
        self.calc_f()

    def set_h(self, val):
        self.h = val
        self.calc_f()
    
    def calc_f(self):
        self.f = self.g + self.h

    def set_index(self, val):
        self.index = val

    def set_connection(self, tile):
        self.connection = tile