from pathlib import Path

import itertools
from functools import reduce


def find_items_sum_to_2020(filename: str, tuple_size: int):

    input = map(int, Path(__file__).parent.joinpath(filename).read_text().splitlines())

    for combo in itertools.combinations(input, tuple_size):
        if sum(combo) == 2020:
            print(combo)
            answer = reduce(lambda x, y: x * y, combo)
            print(answer)

    return answer


def main():

    fname = "input.txt"

    find_items_sum_to_2020(fname, 2)

    find_items_sum_to_2020(fname, 3)

    return


if __name__ == "__main__":
    main()
