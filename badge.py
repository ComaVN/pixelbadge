import rgb
import time

# Generally needed code:
FRAME_WIDTH = 32
FRAME_HEIGHT = 8
Frame = [0 for _ in range(256)]
Frame_nr = 0
# [[0 for x in range(FRAME_WIDTH)] for y in range(FRAME_HEIGHT)]
Old_cells = [[0 for x in range(FRAME_WIDTH)] for y in range(FRAME_HEIGHT)]
New_cells = [[0 for x in range(FRAME_WIDTH)] for y in range(FRAME_HEIGHT)]


def cell_to_color(cell):
    return (cell & 0xffffff) << 8 | 0xff


def cells_to_image(cells):
    image = []
    for row in cells:
        for cell in row:
            image.append(cell_to_color(cell))
    return image


def cell_to_led_color(cell):
    return (cell & 0xffffff) << 8


def cells_to_frame(cells, frame):
    idx = 0
    for row in cells:
        for cell in row:
            frame[idx] = cell_to_led_color(cell)
            idx += 1


def render_frame(delay):
    def fn():
        global Frame, Frame_nr, Old_cells, New_cells
        next_cells(Old_cells, New_cells, Frame_nr)
        cells_to_frame(New_cells, Frame)
        rgb.frame(Frame)
        Frame_nr += 1
        Old_cells, New_cells = New_cells, Old_cells
        return delay
    return fn


# app-specific code:
def next_cells(old_cells, new_cells, frame_nr):
    color = (
        (((frame_nr >> 8) & 0x0f) << 20) +  # r
        (((frame_nr >> 4) & 0x0f) << 12) +  # g
        ((frame_nr & 0x0f) << 4))
    print('{:#08x}'.format(color))
    for y in range(FRAME_HEIGHT):
        for x in range(FRAME_WIDTH):
            new_cells[y][x] = color


rgb.background(
    color=(0, 0, 0),
)
rgb.clear()
rgb.disablecomp()
virtualtimers.begin(10)
virtualtimers.new(0, render_frame(10))
