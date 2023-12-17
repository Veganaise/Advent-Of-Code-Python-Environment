from enum import Enum
from typing import List

from src.util.exceptions import SolutionNotFoundException
from src.util.helpers import solution_timer
from src.util.input_helpers import get_input_for_day


class dirs(Enum):
    LEFT: tuple = (0, -1)
    UP: tuple = (-1, 0)
    RIGHT: tuple = (0, 1)
    DOWN: tuple = (1, 0)


matchslash = {dirs.LEFT: dirs.DOWN,
              dirs.UP: dirs.RIGHT,
              dirs.DOWN: dirs.LEFT,
              dirs.RIGHT: dirs.UP}

matchbackslash = {dirs.LEFT: dirs.UP,
                  dirs.DOWN: dirs.RIGHT,
                  dirs.UP: dirs.LEFT,
                  dirs.RIGHT: dirs.DOWN}


def print_energised(n, m, energised: set):
    cells = {v[0] for v in energised}
    for i in range(n):
        line = ''
        for j in range(m):
            if (i, j) in cells:
                line += '█'
            else:
                line += '.'
        print(line)


@solution_timer(2023, 16, 1)
def part_one(input_data: List[str]):
    n, m = len(input_data), len(input_data[0])
    starting_beam = ((0, -1), dirs.RIGHT)

    answer = get_nb_energised(input_data, m, n, starting_beam)

    if not answer:
        raise SolutionNotFoundException(2023, 16, 1)

    return answer


def get_nb_energised(input_data, m, n, starting_beam):
    energised = set()
    beams = [starting_beam]
    while beams:
        pos, d = beams.pop(0)

        value = d.value
        new_pos = (pos[0] + value[0], pos[1] + value[1])
        if 0 <= new_pos[0] < n and 0 <= new_pos[1] < m and not ((new_pos, d) in energised):
            energised.add((new_pos, d))
            tile = input_data[new_pos[0]][new_pos[1]]
            if tile == '.':
                beams.append((new_pos, d))
            elif tile == '|':
                if d == dirs.UP or d == dirs.DOWN:
                    beams.append((new_pos, d))
                else:
                    beams.append((new_pos, dirs.UP))
                    beams.append((new_pos, dirs.DOWN))
            elif tile == '-':
                if d == dirs.UP or d == dirs.DOWN:
                    beams.append((new_pos, dirs.LEFT))
                    beams.append((new_pos, dirs.RIGHT))
                else:
                    beams.append((new_pos, d))
            elif tile == '/':
                d = matchslash[d]
                beams.append((new_pos, d))
            else:
                d = matchbackslash[d]
                beams.append((new_pos, d))
    answer = len({v[0] for v in energised})
    return answer


@solution_timer(2023, 16, 2)
def part_two(input_data: List[str]):
    answer = -1
    n, m = len(input_data), len(input_data[0])
    starting_beam = ((0, -1), dirs.RIGHT)

    answer = get_nb_energised(input_data, m, n, starting_beam)

    for i in range(n):
        answer=max(answer,
                   get_nb_energised(input_data,n,m,((i,-1),dirs.RIGHT)),
                   get_nb_energised(input_data,n,m,((i,n),dirs.LEFT))
                   )
    for j in range(m):
        answer = max(answer,
                     get_nb_energised(input_data, n, m, ((-1, j), dirs.DOWN)),
                     get_nb_energised(input_data, n, m, ((m, j), dirs.UP))
                     )

    if not answer:
        raise SolutionNotFoundException(2023, 16, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2023, 16)
    part_one(data)
    part_two(data)
