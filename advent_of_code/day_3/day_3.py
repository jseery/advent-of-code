from pathlib import Path
from typing import List
import itertools
import operator

def get_puzzle_input(fname: str):
    input = Path(__file__).parent.joinpath(fname).read_text()
    return input.strip().splitlines()


def traverse_trees(one_section: List[List[str]], down_jump: int = 1, right_jump: int = 1) -> int:

    print(f"rows={len(one_section)}")

    one_part_columns = len(one_section[0])
    print(f"{one_part_columns=}")

    tree_count = 0
    row = 0
    column = 0
    while row < len(one_section):
        # print(row, column, column % one_part_columns)
        if one_section[row][column % one_part_columns] == '#':
            tree_count += 1
        row += down_jump
        column += right_jump

    print(f"{tree_count=}")
    return tree_count



def main():

    input = get_puzzle_input('input.txt')

    answer = list(itertools.accumulate(
        [
            traverse_trees(input, right_jump=1),
            traverse_trees(input, right_jump=3),
            traverse_trees(input, right_jump=5),
            traverse_trees(input, right_jump=7),
            traverse_trees(input, down_jump=2)
        ],
        operator.mul
    ))
    print(answer)
    print(answer[-1])

    return


if __name__ == "__main__":
    main()


