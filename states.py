from enum import Enum

class State(Enum):
    CREATE_OBSTACLES = "Place some obstacles on the board then press enter!"
    CHOOSE_START = "Choose a starting point!"
    CHOOSE_END = "Choose an ending point!"
    NAVIGATING = "Finding a path using A* search!"
    DONE = "Done!"