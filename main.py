import pygame
from settings import BG_COLOR, FG_COLOR, FPS, DISPLAY, FONT
from utils import calculate_font_size, pre_render_chars_with_colors, generate_unicode_set
from draw import draw_matrix
from columns import initialize_columns, update_columns

def main():
    pygame.init()

    # screen info
    displays = pygame.display.get_desktop_sizes() # return list of available screen size
    display = DISPLAY # number of display selected to render window (0 is main display)
    WIDTH, HEIGHT = displays[display][0], displays[display][1]
    
    # set font size and determine amount of columns and rows
    FONT_SIZE = calculate_font_size(WIDTH, HEIGHT)
    COLUMNS = WIDTH // FONT_SIZE
    ROWS = HEIGHT // FONT_SIZE
    print(pygame.font.get_fonts())
    
    # init display module and set font
    screen = pygame.display.set_mode((WIDTH, HEIGHT), display=display)
    pygame.display.set_caption("Matrix Rain")
    font = pygame.font.SysFont([FONT, "Arial"], FONT_SIZE) # arial as backup font

    # list of chars
    chars = generate_unicode_set()

    pre_rendered_chars = pre_render_chars_with_colors(font, chars, FG_COLOR, ROWS)

    # init needed lists
    active_columns, column_items, coord_list = initialize_columns(COLUMNS, ROWS, FONT_SIZE)

    # main loop
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False

        update_columns(active_columns, column_items, coord_list, HEIGHT, FONT_SIZE, ROWS)
        draw_matrix(screen, column_items, pre_rendered_chars, BG_COLOR, ROWS)
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()