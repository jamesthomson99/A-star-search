from tile import Tile
from states import State
from constants import *
import pygame
import sys
import time


# Function to draw board on screen with pygame
def draw_board(screen, board, last_click_time, current_state):

    # Get mouse coordinates and detect click
    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()

    clicked_cell_coords = None

    current_time = time.time()

    for row_index, row in enumerate(board):
        for col_index, cell in enumerate(row):
            x = col_index * (CELL_SIZE+ CELL_BORDER)
            y = row_index * (CELL_SIZE + CELL_BORDER)

            cell_rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            cell_border_size = CELL_BORDER

            # Check for mouse hover/click on cell and style as necessary
            if cell_rect.collidepoint(mouse_x, mouse_y):
                if mouse_click[0] and current_time - last_click_time > 0.5:
                    cell.toggle_start_point()
                    last_click_time = current_time
                    clicked_cell_coords = (mouse_x, mouse_y)
                cell_border_size = 2 * CELL_BORDER
            if cell.is_start_point:
                cell.color = BLUE
            else:
                cell.color = WHITE

            # Draw cell and border
            pygame.draw.rect(screen, cell.color, cell_rect)
            pygame.draw.rect(screen, BLACK, cell_rect, cell_border_size)

    return last_click_time, clicked_cell_coords


def main():

    # Create and populate board with tiles
    board = []
    for i in range(BOARD_DIMENSIONS[0]):
        row = []
        for j in range(BOARD_DIMENSIONS[1]):
            tile = Tile()
            row.append(tile)
        board.append(row)

    # Pygame initialization
    pygame.init()

    rows, cols = len(board), len(board[0])
    window_size = (cols * (CELL_SIZE + CELL_BORDER) - CELL_BORDER, rows * (CELL_SIZE + CELL_BORDER) - CELL_BORDER + INFO_BAR_HEIGHT)
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption("A* Search Visualization")
    clock = pygame.time.Clock()

    # State initialization
    current_state = State.CHOOSE_START

    # Info bar
    pygame.font.init()
    font_size = 24
    info_bar_text = current_state.value
    font = pygame.font.Font(None, 24)

    # A* Search initialization
    starting_point = None
    ending_point = None

    # Main loop
    last_click_time = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Draw board and render info bar text
        screen.fill(WHITE)
        text = font.render(current_state.value, True, BLACK)
        text_rect = text.get_rect(midleft=(10, window_size[1] - (INFO_BAR_HEIGHT / 2)))
        screen.blit(text, text_rect)
        last_click_time, clicked_cell_coords = draw_board(screen, board, last_click_time, current_state)

        # State management
        if clicked_cell_coords:
            if current_state == State.CHOOSE_START:
                starting_point = clicked_cell_coords
                current_state = State.CHOOSE_END
            elif current_state == State.CHOOSE_END:
                ending_point = clicked_cell_coords
                current_state = State.NAVIGATING

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()