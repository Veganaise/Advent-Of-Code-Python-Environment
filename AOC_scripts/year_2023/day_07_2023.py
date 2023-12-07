from typing import List
import re
from collections import Counter

from src.util.exceptions import SolutionNotFoundException
from src.util.helpers import solution_timer
from src.util.input_helpers import get_input_for_day

types = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
alphabet = 'AKQJT98765432'
alphabet_p2 = 'AKQT98765432J'


@solution_timer(2023, 7, 1)
def part_one(input_data: List[str]):
    hand_types = [[] for _ in range(7)]
    biddings = {}
    p = re.compile(r'(\d+)')
    input_data = [(x, int(y)) for x, y in map(str.split, input_data)]
    for hand, bid in input_data:
        biddings[hand] = bid
        value = sorted(Counter(hand).values(), reverse=True)
        rank = None
        if value[0] == 5:
            rank = 0
        elif value[0] == 4:
            rank = 1
        elif value[0] == 3:
            if value[1] == 2:
                rank = 2
            else:
                rank = 3
        elif value[0] == 2:
            if value[1] == 2:
                rank = 4
            else:
                rank = 5
        else:
            rank = 6

        hand_types[rank].append(hand)

    ranks = []
    for hands in hand_types:
        ranks.extend(sorted(hands, key=lambda word: [alphabet.index(c) for c in word]))

    answer = 0

    for rank, hand in enumerate(reversed(ranks)):
        answer += biddings[hand] * (rank + 1)

    if not answer:
        raise SolutionNotFoundException(2023, 7, 1)

    return answer


@solution_timer(2023, 7, 2)
def part_two(input_data: List[str]):
    hand_types = [[] for _ in range(7)]
    biddings = {}
    p = re.compile(r'(\d+)')
    input_data = [(x, int(y)) for x, y in map(str.split, input_data)]
    for hand, bid in input_data:
        biddings[hand] = bid
        count = Counter(hand)
        nb_jokers = count.get('J', 0)
        value = sorted(count.values(), reverse=True)
        rank = None
        if value[0] == 5:
            rank = 0
        elif value[0] == 4:
            if nb_jokers >= 1:
                rank = 0
            else:
                rank = 1
        elif value[0] == 3:
            if nb_jokers == 1:
                rank = 1
            elif nb_jokers == 2:
                rank = 0
            elif nb_jokers == 3:
                if value[1] == 2:
                    rank = 0
                else:
                    rank = 1
            elif value[1] == 2:
                rank = 2
            else:
                rank = 3
        elif value[0] == 2:
            if value[1] == 2:
                if nb_jokers == 1:
                    rank = 2
                elif nb_jokers == 2:
                    rank = 1
                else:
                    rank = 4
            else:
                if nb_jokers == 2:
                    rank = 3
                elif nb_jokers == 1:
                    rank = 3
                else:
                    rank = 5
        else:
            if nb_jokers == 1:
                rank = 5
            else:
                rank = 6

        hand_types[rank].append(hand)

    ranks = []
    for hands in hand_types:
        ranks.extend(sorted(hands, key=lambda word: [alphabet_p2.index(c) for c in word]))

    answer = 0

    for rank, hand in enumerate(reversed(ranks)):
        answer += biddings[hand] * (rank + 1)

    if not answer:
        raise SolutionNotFoundException(2023, 7, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2023, 7)
    part_one(data)
    part_two(data)
