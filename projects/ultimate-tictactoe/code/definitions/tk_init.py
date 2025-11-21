from typing import Tuple


# Opponent setting
TWO_PLAYER = "2 Player"
BEGINNER = "Beginner"
MCTS = "MCTS"
FOO1 = "Foo 1"
FOO2 = "Foo 2"
FOO3 = "Foo 3"

# Turn order
RANDOM_ORDER = "Random"
PLAYER_FIRST = "First"
PLAYER_SECOND = "Second"


# board Dimensions
SQUARESIZE = 50  # size of each square
WHITESPACE = 12  # space in between local boards
BOARDERSIZE = 400+ WHITESPACE // 2  # boarder between edge of screen and local boards
LOCALBOARDSIZE = SQUARESIZE * 3  # total size of each local board
GLOBALBOARDSIZE = SQUARESIZE * 9 + WHITESPACE * 3  # width of the global board, not including the menu
MENUWIDTH = LOCALBOARDSIZE + 2 * BOARDERSIZE  # the width of the menu area
DIFF = int(SQUARESIZE * 0.4)  # determines size of the 'X's and 'O's. Must be less than half of SQUARESIZE

# color Definitions
RGBColor = Tuple[str, str]  # color type hint

BLACK = '#000000'
WHITE = '#ffffff'

VIOLET = '#61298B'

LIGHT_GRAY = '#eeeeee'
MEDIUM_GRAY = '#bcbcbc'
GRAY = '#E4E2DD'
DARK_GRAY = '#5b5b5b'

LIGHT_RED = '#f4cccc'
MEDIUM_RED = '#e06666'
RED = '#990000'

LIGHT_GREEN = '#d9ead3'
MEDIUM_GREEN = '#93c47d'
GREEN = '#1b5e23'

ORANGE = '#da760e'
LIGHT_ORANGE = '#ffd4a6'

LIGHT_BLUE = '#cfe2f3'
MEDIUM_BLUE = '#6fa8dc'
BLUE = "#4a438b"

import tkinter as tk
from typing import Tuple


def draw_diamond(canvas,x,y,size,color,outline):
    x1 = x-10
    y1 = y-10
    x2 = x1 + size
    y2= y1 
    x3 = x2 + size/4
    y3 = y2 + size/4.1
    x4 = x1 + size/2
    y4 = y3 + size 
    x5 = x1 - size/4
    y5 = y3
    
    x7 = x1 + size/7.5
    y7 = y3
    x8 = x1 + size/2
    y8 = y1
    x9 = x2 - size/7.5
    y9 = y3
    x10 = x2 - size/2
    y10 = y1
    diamond_id = canvas.create_polygon(((x1,y1),(x2,y2),(x3,y3),(x4,y4),(x5,y5)), outline=outline, fill= color,width=3)
    l1 = canvas.create_line(x3,y3,x5,y5,fill= outline,width=3)
    l2 = canvas.create_line(x1,y1,x4,y4,fill= outline,width=3)
    l3 = canvas.create_line(x2,y2,x4,y4,fill= outline,width=3)
    l4 = canvas.create_line(x7,y7,x8,y8,fill= outline,width=3)
    l5 = canvas.create_line(x9,y9,x10,y10,fill= outline,width=3)
    return [diamond_id,l1,l2,l3,l4,l5]


def delete_in_zone(canvas, tag, zone_x1, zone_y1, zone_x2, zone_y2):
  element_ids = canvas.find_withtag(tag)
  for element_id in element_ids:
    bbox = canvas.bbox(element_id)
    if (bbox[0] >= zone_x1 and bbox[1] >= zone_y1 and
        bbox[2] <= zone_x2 and bbox[3] <= zone_y2):
      canvas.delete(element_id)

def change_color(canvas,root,perm_color):
  canvas.config(bg=LIGHT_GREEN)  # Change to red
  root.after(1000, lambda: canvas.config(bg=perm_color))

def draw_and_erase_diamond(canvas,root,lr,lc):
  # Define line coordinates
  x,y = SQUARESIZE*(lc)+30, SQUARESIZE*(lr)+30
  line_ids = draw_diamond(canvas,x,y,SQUARESIZE//3,LIGHT_GRAY,GRAY)

  # Schedule line deletion after 2 seconds
  root.after(500, lambda: [canvas.delete(line_id) for line_id in line_ids])
