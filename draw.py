import pygame

def draw_matrix(screen, column_items, pre_rendered_chars, BG_COLOR, shade_steps):
    
    screen.fill(BG_COLOR)

    for i, items in enumerate(column_items):
        for j, item in enumerate(items):
            # calculate shade index
            shade_index = min(shade_steps - 1, j)
            char = item[2]

            # set char on surface
            pre_rendered_surface = pre_rendered_chars[char][shade_index]

            # draw char on screen
            screen.blit(pre_rendered_surface, (item[0], item[1]))

    pygame.display.flip()
