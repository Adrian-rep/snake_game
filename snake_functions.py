import pygame
import random
import tkinter as tk
from tkinter import messagebox


def draw_grid(width, rows, surface):
    size_between = width // rows

    x = 0
    y = 0
    for _ in range(rows):
        x = x + size_between
        y = y + size_between

        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, width))  # ||
        pygame.draw.line(surface, (255, 255, 255), (0, y), (width, y))  # =


def redraw_window(surface, window_rows, window_width, window_snake, window_snack):
    surface.fill((0, 0, 0))
    window_snake.draw(surface)
    window_snack.draw(surface)
    draw_grid(window_width, window_rows, surface)
    pygame.display.update()


def random_snack(random_rows, snake):
    positions = snake.body

    while True:
        x = random.randrange(random_rows)
        y = random.randrange(random_rows)
        if len(list(filter(lambda z: z.position == (x, y), positions))) > 0:  # snack not on snake
            continue
        else:
            break

    return x, y


def message_box(subject, content):
    root = tk.Tk()
    root.attributes('-topmost', True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    root.destroy()

