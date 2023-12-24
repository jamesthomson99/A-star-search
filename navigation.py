import numpy as np
from tile import Tile
from constants import *


class AStarSearch():

    def __init__(self):
        self.start_tile = None
        self.end_tile = None
        self.to_search = []
        self.processed = []

    
    # Function to set start and end tiles once they have been set on GUI
    def initialize(self, start_tile, end_tile):
        self.start_tile = start_tile
        self.end_tile = end_tile
        self.to_search.append(self.start_tile)


    # Function to perform a single step of the A* search algorithm
    def step(self, board):

        # Perform next step as long as there are still tiles left to search
        if len(self.to_search) > 0:

            # Find tile in search list with lowest f
            current_tile = self.to_search[0]
            for t in self.to_search:
                if t.f < current_tile.f or (t.f == current_tile.f and t.h < current_tile.h):
                    current_tile = t

            # Add the current tile to the processed list and remove it from the search list
            self.processed.append(current_tile)
            if not (current_tile == self.start_tile or current_tile == self.end_tile):
                current_tile.color = GRAY
            self.to_search.remove(current_tile)

            # If the current tile is the end tile, find the path using established connections and return path
            if current_tile == self.end_tile:
                current_path_tile = self.end_tile
                path = []
                while(current_path_tile != self.start_tile):
                    path.append(current_path_tile)
                    current_path_tile = current_path_tile.connection

                path.append(self.start_tile)
                return path

            # Get current tile neighbours
            neighbours = self.get_neighbours(board, current_tile)

            # For each neighbor that isn't an obstacle and hasn't been processed
            for neighbour in [t for t in neighbours if not t.is_obstacle and t not in self.processed]:
                # Check if current neighbor is in to_search list 
                in_search = neighbour in self.to_search

                # Get total cost from start node to current neighbor
                cost_to_neighbour = current_tile.g + self.calculate_distance(current_tile, neighbour)

                # If current neighbor isn't in search list or the new cost to neighbor is less than the neighbor's G (distance from start)
                if not in_search or cost_to_neighbour < neighbour.g:
                    # Update neighbor with new G distance and set a connection between current tile and current neighbor
                    neighbour.set_g(cost_to_neighbour)
                    neighbour.set_connection(current_tile)

                    # If current neighbor isn't in search list add it to search list and set it's H distance (estimated distance to end)
                    if not in_search:
                        neighbour.set_h(self.calculate_distance(neighbour, self.end_tile))
                        self.to_search.append(neighbour)
                        if not (neighbour == self.start_tile or neighbour == self.end_tile):
                            neighbour.color = LIGHT_GRAY

            return None   


    # Function that receives the board and a tile and returns a list of all the tiles neighbours
    def get_neighbours(self, board, current_tile):

        rows, cols = len(board), len(board[0])
        row, col = current_tile.index[0], current_tile.index[1]
        neighbours = []

        for i in range(-1, 2):
            for j in range(-1, 2):

                if i == 0 and j == 0:
                    continue

                new_row, new_col = row + i, col + j

                if 0 <= new_row < rows and 0 <= new_col < cols:
                    neighbours.append(board[new_row][new_col])

        return neighbours


    # Function that calculates the euclidean distance between two tiles
    def calculate_distance(self, tile1, tile2):
        index1, index2 = tile1.index, tile2.index
        x1, y1, x2, y2 = index1[0], index1[1], index2[0], index2[1]
        h = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        return h


    # Function to print tile in nice, readable way
    def print_tile(self, caption, input):
        if isinstance(input, Tile):
            print(caption, input.index)
        elif isinstance(input, list) and isinstance(input[0], Tile):
            result_string = caption
            for item in input:
                result_string += str(item.index) + ", "

            print(result_string.rstrip(', '))