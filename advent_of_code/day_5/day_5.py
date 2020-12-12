from pathlib import Path
import itertools


ROWS = 128
ROW_PARTITIONS = [64, 32, 16, 8, 4, 2, 1]
COLS = 8
COL_PARTITIONS = [4, 2, 1]



def get_puzzle_input(fname: str):
    input = Path(__file__).parent.joinpath(fname).read_text().splitlines()
    return input



def find_row(seq: str) -> int:
    assert len(seq) == 7
    remaining_rows = list(range(ROWS))
    for s, p in zip(seq, ROW_PARTITIONS):
        if s == 'F':
            remaining_rows = remaining_rows[:p]
        elif s == 'B':
            remaining_rows = remaining_rows[p:]
    assert len(remaining_rows) == 1, f"{remaining_rows=}"
    return remaining_rows[0]


def find_col(seq: str) -> int:
    assert len(seq) == 3
    remaining_cols = list(range(COLS))
    for s, p in zip(seq, COL_PARTITIONS):
        if s == 'L':
            remaining_cols = remaining_cols[:p]
        elif s == 'R':
            remaining_cols = remaining_cols[p:]
    assert len(remaining_cols) == 1, f"{remaining_cols=}"
    return remaining_cols[0]


def find_seat_id(p: str) -> int:
    found_row = find_row(p[:7])
    found_col = find_col(p[7:])
    seat_id = (found_row * 8) + found_col
    # print(f"{found_row=}, {found_col=}, {seat_id=}")
    return seat_id



def main():

    pz = get_puzzle_input("input.txt")

    taken_seat_ids = [find_seat_id(p) for p in pz]
    taken_seat_ids.sort()
    answer_1 = max(taken_seat_ids)
    print(answer_1)


    all_seats = list(range(min(taken_seat_ids), answer_1))

    answer_2 = set(all_seats) - set(taken_seat_ids)
    print(f"{answer_2=}")

    return


if __name__ == "__main__":
    main()
