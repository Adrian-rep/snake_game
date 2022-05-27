import pygame
from snake_functions import redraw_window, random_snack, message_box
from snake_cube import Cube
from snake_snake import Snake


def main():
    width = 500
    rows = 20
    win = pygame.display.set_mode((width, width))
    snake = Snake((255, 0, 0), (10, 10))
    snack = Cube(random_snack(rows, snake), color=(0, 255, 0))   # random_snack zwraca współrzędnie x, y
    flag = True
    clock = pygame.time.Clock()

    while flag:
        pygame.init()
        pygame.display.set_caption(f'Score: {len(snake.body)}')
        pygame.time.delay(50)
        clock.tick(10)
        snake.move()
        if snake.body[0].position == snack.position:
            snake.add_cube()
            snack = Cube(random_snack(rows, snake), color=(0, 255, 0))

        for x in range(len(snake.body)):
            if snake.body[x].position in list(map(lambda z: z.position, snake.body[x+1:])):
                print(f'Score: {len(snake.body)}')
                message_box('You lost!', 'Play again')
                snake.reset((10, 10))
                break

        redraw_window(win, rows, width, snake, snack)


if __name__ == '__main__':
    main()
