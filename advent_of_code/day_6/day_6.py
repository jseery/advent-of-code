from pathlib import Path
from typing import List
from collections import Counter
from toolz import keyfilter, valfilter


def get_puzzle_input(fname: str):
    input = Path(__file__).parent.joinpath(fname).read_text()
    return input


# part 1
def count_yes_any(puz: List) -> int:

    group_counts: List[int] = []
    group_running_set = set()
    for line in puz:
        if line == "":
            group_counts.append(len(group_running_set))
            group_running_set = set()
        group_running_set.update(line)
    group_counts.append(len(group_running_set))

    return sum(group_counts)


def count_yes_all(puz) -> List:

    group_counts: List[int] = []

    group_total_people = 0
    group_running_answers = Counter()
    for line in puz:
        if line == "":
            group_counts.append(
                len(
                    [
                        k
                        for k, v in group_running_answers.items()
                        if v == group_total_people
                    ]
                )
            )
            group_running_answers = Counter()
            group_total_people = 0
        else:
            group_total_people += 1
            group_running_answers.update(list(line))

    group_counts.append(
        len([k for k, v in group_running_answers.items() if v == group_total_people])
    )
    return sum(group_counts)


def main():

    puz = get_puzzle_input("input.txt").splitlines()

    answer_1 = count_yes_any(puz)
    print(f"{answer_1=}")

    answer_2 = count_yes_all(puz)
    print(f"{answer_2=}")

    return


if __name__ == "__main__":
    main()
