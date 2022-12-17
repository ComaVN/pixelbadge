import random
import rgb
import time

# Generally needed code:
FRAME_WIDTH = 32
FRAME_HEIGHT = 8
Frame = [0 for _ in range(256)]
FrameNr = 0
Cells = [[0 for x in range(FRAME_WIDTH)] for y in range(FRAME_HEIGHT)]


def cell_to_color(cell):
    return (cell % 0x01000000) << 8 | 0xff


def cells_to_image(cells):
    image = []
    for row in cells:
        for cell in row:
            image.append(cell_to_color(cell))
    return image


def cell_to_led_color(cell):
    return (cell % 0x01000000) << 8


def cells_to_frame(cells):
    frame = [0 for _ in range(256)]
    idx = 0
    for row in cells:
        for cell in row:
            frame[idx] = cell_to_led_color(cell)
            idx += 1
    return frame

def render_frame(delay):
    def fn():
        global Frame, FrameNr, Cells
        Cells = next_cells(FrameNr)
        Frame = cells_to_frame(Cells)
        rgb.frame(Frame)
        FrameNr += 1
        return delay
    return fn

# app-specific code:


def next_cells(idx):
    new_cells = [[0 for x in range(FRAME_WIDTH)] for y in range(FRAME_HEIGHT)]
    for y in range(FRAME_HEIGHT):
        for x in range(FRAME_WIDTH):
            new_cells[y][x] = idx*16
    return new_cells


rgb.background(
    color=(0, 0, 0),
)
rgb.clear()
rgb.disablecomp()
virtualtimers.begin(100)
virtualtimers.new(0, render_frame(500))
