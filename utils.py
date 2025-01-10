import random
import string
from settings import FONT_FACTOR

# calculate font size depending on screen size
def calculate_font_size(w, h, factor=FONT_FACTOR):
    # factor param is percentage size of screen 
    font_size = min(w, h) * factor
    return int(font_size)

def get_random_char():
    return random.choice(unicode_set)

# calculate font color
def fade_color(color, factor):
    r, g, b = color
    r = int(max(0, min(255, r * factor)))
    g = int(max(0, min(255, g * factor)))
    b = int(max(0, min(255, b * factor)))
    return (r, g, b)

def pre_render_chars_with_colors(font, chars, base_color, steps):
    
    rendered_chars = {}
    for char in chars:
        rendered_chars[char] = {}
        for step in range(steps):
            
            factor = 1 - (step / (steps - 1))  

            if step == 0:
                color = base_color # if its bottom char set color to base color
            else:
                color = fade_color(base_color, factor) # fade color gradually

            # render char
            text_surface = font.render(char, True, color)
            rendered_chars[char][step] = text_surface

    return rendered_chars

# generate unicode char set, u can add more
def generate_unicode_set():
    unicode_set = []

    # latin
    for code in range(0x41, 0x5A + 1):  
        unicode_set.append(chr(code))
    for code in range(0x61, 0x7A + 1): 
        unicode_set.append(chr(code))

    # greek
    for code in range(0x391, 0x3A9 + 1):  
        unicode_set.append(chr(code))
    for code in range(0x3B1, 0x3C9 + 1):  
        unicode_set.append(chr(code))

    return unicode_set

unicode_set = generate_unicode_set()
