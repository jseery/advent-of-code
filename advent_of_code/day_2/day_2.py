from pathlib import Path
from typing import Tuple
from collections import Counter

import re

from dataclasses import dataclass


@dataclass
class PolicyPW(object):
    min: str
    max: str
    char: str
    pw: str

    def has_valid_pw(self):
        self.char_count = Counter(self.pw).get(self.char)
        if not self.char_count:
            return False
        elif int(self.char_count) < int(self.min):
            return False
        elif int(self.char_count) > int(self.max):
            return False
        else:
            return True


def parse_password(pw_string: str) -> PolicyPW:
    expr = re.compile(r"(?P<min>[\d]+)-(?P<max>[\d]+) (?P<char>[a-z]): (?P<pw>[a-z]+)")
    output = PolicyPW(**expr.match(pw_string).groupdict())
    return output


def get_puzzle_input(fname: str):
    input = Path(__file__).parent.joinpath(fname).read_text()
    return input.splitlines()


def part_one():
    input = get_puzzle_input("input.txt")

    parsed_pws = list(map(parse_password, input))
    valid_pw = filter(lambda x: x.has_valid_pw(), parsed_pws)
    broken_pw = filter(lambda x: not x.has_valid_pw(), parsed_pws)
    answer = len(list(valid_pw))
    print(f"{answer=}")

    return


@dataclass
class PolicyPartTwo(object):
    pos_first: str
    pos_second: str
    char: str
    pw: str

    def has_valid_pw(self):
        idx_first = int(self.pos_first)
        idx_second = int(self.pos_second)

        char_first = self.pw[idx_first - 1]
        char_second = self.pw[idx_second - 1]

        if bool(char_first == self.char) ^ bool(char_second == self.char):
            return True
        else:
            return False


def parse_part_two(pw_string: str) -> PolicyPartTwo:
    expr = re.compile(
        r"(?P<pos_first>[\d]+)-(?P<pos_second>[\d]+) (?P<char>[a-z]): (?P<pw>[a-z]+)"
    )
    output = PolicyPartTwo(**expr.match(pw_string).groupdict())
    return output


def part_two():

    input_list = get_puzzle_input("input.txt")

    parsed_pws = list(map(parse_part_two, input_list))

    valid_pw = filter(lambda x: x.has_valid_pw(), parsed_pws)
    broken_pw = filter(lambda x: not x.has_valid_pw(), parsed_pws)
    answer = len(list(valid_pw))
    print(f"{answer=}")

    return


def main():
    part_two()


if __name__ == "__main__":
    main()
