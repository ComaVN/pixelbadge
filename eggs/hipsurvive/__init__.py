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
    return (cell % 0x01000000) << 8 | 0xff


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
def split_cell_to_rgb(cell):
    return ((cell & 0xff0000) >> 16, (cell & 0x00ff00) >> 8, cell & 0x0000ff)


def rgb_to_cell(rgb):
    return (rgb[0] << 16) | rgb[1] << 8 | rgb[2]


def score(rgb_1, rgb_2):
    red_green_1 = rgb_1[0] - rgb_1[1]  # positive means more red than green
    red_green_2 = rgb_2[0] - rgb_2[1]  # positive means more red than green
    green_blue_1 = rgb_1[1] - rgb_1[2]  # positive means more green than blue
    green_blue_2 = rgb_2[1] - rgb_2[2]  # positive means more green than blue
    blue_red_1 = rgb_1[2] - rgb_1[0]  # positive means more blue than red
    blue_red_2 = rgb_2[2] - rgb_2[0]  # positive means more blue than red
    s = (
        (red_green_1 - red_green_2) +
        (green_blue_1 - green_blue_2) +
        (blue_red_1 - blue_red_2))
    print("score: {}".format(s))
    return s


def next_cells(old_cells, new_cells, frame_nr):
    for y, row in enumerate(old_cells):
        if y == 0:
            print("ignore first row")
            continue
        if y == FRAME_HEIGHT - 1:
            print("ignore last row")
            continue
        for x, cell in enumerate(row):
            if x == 0:
                print("ignore first column")
                continue
            if x == FRAME_WIDTH - 1:
                print("ignore last row")
                continue
            rgb_cell = split_cell_to_rgb(cell)
            rgb_left = split_cell_to_rgb(old_cells[y][x-1])
            rgb_right = split_cell_to_rgb(old_cells[y][x+1])
            rgb_above = split_cell_to_rgb(old_cells[y-1][x])
            rgb_below = split_cell_to_rgb(old_cells[y+1][x])
            rgb_best_neighbor = max(
                rgb_left,
                rgb_right,
                rgb_above,
                rgb_below,
                key=lambda rgb: score(rgb, rgb_cell),
            )
            print("winner ({},{}): {}".format(x, y, rgb_best_neighbor))
            new_cells[y][x] = rgb_to_cell(rgb_best_neighbor)


Old_cells[2][9] = 0xff
rgb.background(
    color=(0, 0, 0),
)
rgb.clear()
rgb.disablecomp()
virtualtimers.begin(10)
virtualtimers.new(0, render_frame(10))
