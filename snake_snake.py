import sys
import pygame
from snake_cube import Cube


class Snake:
    body = []
    turns = {}

    def __init__(self, color, pos):
        self.color = color
        self.head = Cube(pos)
        self.body.append(self.head)
        self.dirn_x = 0
        self.dirn_y = 1

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            keys = pygame.key.get_pressed()

            for _ in keys:
                if keys[pygame.K_LEFT]:
                    self.dirn_x = -1
                    self.dirn_y = 0
                    self.turns[self.head.position[:]] = [self.dirn_x, self.dirn_y]
                elif keys[pygame.K_RIGHT]:
                    self.dirn_x = 1
                    self.dirn_y = 0
                    self.turns[self.head.position[:]] = [self.dirn_x, self.dirn_y]
                elif keys[pygame.K_UP]:
                    self.dirn_x = 0
                    self.dirn_y = -1
                    self.turns[self.head.position[:]] = [self.dirn_x, self.dirn_y]
                elif keys[pygame.K_DOWN]:
                    self.dirn_x = 0
                    self.dirn_y = 1
                    self.turns[self.head.position[:]] = [self.dirn_x, self.dirn_y]

        for idx, cube in enumerate(self.body):
            p = cube.position[:]
            if p in self.turns:
                turn = self.turns[p]
                cube.move(turn[0], turn[1])
                if idx == len(self.body) - 1:
                    self.turns.pop(p)
            else:
                if cube.direction_x == -1 and cube.position[0] <= 0:
                    cube.position = (cube.rows - 1, cube.position[1])
                elif cube.direction_x == 1 and cube.position[0] >= cube.rows - 1:
                    cube.position = (0, cube.position[1])
                elif cube.direction_y == 1 and cube.position[1] >= cube.rows - 1:
                    cube.position = (cube.position[0], 0)
                elif cube.direction_y == -1 and cube.position[1] <= 0:
                    cube.position = (cube.position[0], cube.rows - 1)
                else:
                    cube.move(cube.direction_x, cube.direction_y)

    def reset(self, pos):
        self.head = Cube(pos)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.dirn_x = 0
        self.dirn_y = 1

    def add_cube(self):
        tail = self.body[-1]
        dx, dy = tail.direction_x, tail.direction_y

        if dx == 1 and dy == 0:
            self.body.append(Cube((tail.position[0] - 1, tail.position[1])))
        elif dx == -1 and dy == 0:
            self.body.append(Cube((tail.position[0] + 1, tail.position[1])))
        elif dx == 0 and dy == 1:
            self.body.append(Cube((tail.position[0], tail.position[1] - 1)))
        elif dx == 0 and dy == -1:
            self.body.append(Cube((tail.position[0], tail.position[1] + 1)))

        self.body[-1].direction_x = dx
        self.body[-1].direction_y = dy

    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw(surface, True)
            else:
                c.draw(surface)
