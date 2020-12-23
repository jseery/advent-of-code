from advent_of_code import utils
import re
from typing import List
from dataclasses import dataclass


def parse_rule(text: str) -> List:

    source_color_expr = re.compile(r'(?P<color>[a-z\s]+) bags contain')
    source_color = source_color_expr.match(text).group('color')

    no_target = True if re.search(r'no other bags', text) else False

    target_expr = re.compile(r'(?:contain|,) ([0-9] [a-z\s]+ bags*)')
    targets = [' '.join(t.split()[1:-1]) for t in target_expr.findall(text)]

    return source_color, no_target, targets


class Rule(object):

    def __init__(self, text: str):

        parsed = parse_rule(text)
        self.color = parsed[0]
        self.no_target = parsed[1]
        self.targets = parsed[2]
        return

    def __repr__(self):
        return str(dict(color=self.color, no_target=self.no_target, targets=self.targets))


class Bag(object):

    def __init__(self, data):
        self.data = data
        self.children = []

    def pack_bag(self, b: Bag):
        self.children.append(b)
        

def main():

    pz = list(map(Rule, utils.get_puzzle_input('test.txt').splitlines()))

    print(*pz, sep='\n')

        

        


if __name__ == "__main__":
    main()

