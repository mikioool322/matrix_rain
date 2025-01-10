import random
from utils import get_random_char

# init all column info 
def initialize_columns(COLUMNS, AMOUNT, FONT_SIZE):
    active_columns = [random.random() < 0.01 for _ in range(COLUMNS)] # # activate only few columns at start
    column_items = [[] for _ in range(COLUMNS)] # # list of lists containing coordinates and char to display, each nested list represent one column
    coord_list = get_all_coords(AMOUNT, FONT_SIZE, COLUMNS)
    return active_columns, column_items, coord_list

# generate all possible coordinates of screen for char
def get_all_coords(AMOUNT, FONT_SIZE, COLUMNS):
    coord_list = [[] for _ in range(COLUMNS)]
    for i in range(COLUMNS):
        for j in range(AMOUNT + 1):
            coord_list[i].append((i * FONT_SIZE, j * FONT_SIZE, get_random_char()))
    return coord_list

# in each step update column, like active column, add or remove items for column
def update_columns(active_columns, column_items, coord_list, HEIGHT, FONT_SIZE, ROWS):
    for i in range(len(active_columns)):
        y = 0
        if not active_columns[i]:
            if random.random() < 0.003:
                active_columns[i] = True
            continue

        if column_items[i]:
            y = column_items[i][-1][1]
            if y >= HEIGHT - FONT_SIZE*5:
                active_columns[i] = False
                column_items[i] = []

        if not column_items[i] or column_items[i][0][1] < HEIGHT:
            column_items[i].insert(0, coord_list[i][len(column_items[i])])
        
        # empty and deactivate column for more random-like effect 
        if y >= HEIGHT-FONT_SIZE*5:
            active_columns[i] = False
            column_items[i] = []
        
        # pop last item in list if max amount is achieved
        if len(column_items[i]) >= ROWS:
            column_items[i].pop()

       
       

        