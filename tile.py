import math

class Tile:
    def __init__(self):
        self.g = None
        self.h = None
        self.f = None
        self.is_start_point = False
        self.is_end_point = False

    def toggle_start_point(self):
        self.is_start_point = not self.is_start_point

    def toggle_end_point(self):
        self.is_end_point = not self.is_end_point