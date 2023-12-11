from enum import Enum

class State(Enum):
    CHOOSE_START = "Choose a starting point!"
    CHOOSE_END = "Choose an ending point!"
    NAVIGATING = "Finding a path using A* search!"