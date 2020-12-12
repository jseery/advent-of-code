from pathlib import Path


ROWS = 128

PARTITIONS = [64, 32, 16, 8, 4, 2, 1]


def get_puzzle_input(fname: str):
    input = Path(__file__).parent.joinpath(fname).read_text().splitlines()
    return input



def find_row(seq: str) -> int:
    print(seq)
    remaining_rows = list(range(ROWS))
    for p in zip(seq, PARTITIONS):
        print(p)
        if s == 'F':
            remaining_rows = remaining_rows[:p]
            print(remaining_rows)
        elif s == 'B':
            remaining_rows = remaining_rows[p:]
    assert len(remaining_rows) == 1, f"{remaining_rows=}"
    print(remaining_rows)
    return remaining_rows


def main():

    pz = get_puzzle_input("test.txt")
    print(pz)

    rows = map(lambda l: l[:7], pz)
    print(list(rows))

    for r in rows:
        found = find_row(r)
        print(found)

    return


if __name__ == "__main__":
    main()
