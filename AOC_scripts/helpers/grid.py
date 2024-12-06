import enum
from enum import Enum
from typing import List, Any, Tuple


class Cardinals(Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)

    @classmethod
    def opposite(cls, direction):
        match direction:
            case cls.UP:
                return cls.DOWN
            case cls.DOWN:
                return cls.UP
            case cls.LEFT:
                return cls.RIGHT
            case cls.RIGHT:
                return cls.LEFT

    @staticmethod
    def coord_in_direction(i: int, j: int, direction):
        if isinstance(direction, Tuple):
            return i + direction[0], j + direction[1]
        else:
            di, dj = direction.value
            return i + di, j + dj


def iterate(grid: List[Any]):
    for i, row in enumerate(grid):
        for j, value in enumerate(row):
            yield i, j, value


class Grid:
    def __init__(self, grid: List[List[Any]]):
        self.n = len(grid)
        if self.n > 0:
            self.m = len(grid[0])
        self.grid = grid

    def iterate_without_borders(self):
        for i, row in enumerate(self.grid):
            if i == 0 or i == self.n - 1: continue
            for j, value in enumerate(row):
                if j == 0 or j == self.m - 1: continue
                yield i, j, value

    def value_in_direction(self, i, j, direction):
        ci, cj = Cardinals.coord_in_direction(i, j, direction)
        if 0 <= ci < self.n and 0 <= cj < self.m:
            return ci, cj, self.grid[ci][cj]
        else:
            return None
