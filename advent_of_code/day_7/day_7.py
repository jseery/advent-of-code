from advent_of_code import utils
import re
from typing import List
from dataclasses import dataclass
from collections import defaultdict, deque


def parse_rules_pt1(text: str) -> List:

    source_color_expr = re.compile(r'(?P<color>[a-z\s]+) bags contain')
    source_color = source_color_expr.match(text).group('color')

    no_target = True if re.search(r'no other bags', text) else False
    has_target = not no_target

    target_expr = re.compile(r'(?:contain|,) ([0-9] [a-z\s]+ bags*)')
    children = [' '.join(t.split()[1:-1]) for t in target_expr.findall(text)]

    return source_color, children


def part_1():

    ruleset = {b[0]: b[1] for b in map(parse_rules_pt1, utils.get_puzzle_input('input.txt').splitlines())}
    print("RULES")
    print(*ruleset.items(), sep='\n')

    # build a dict of inner_bag -> possible outer bags
    nodes = []  # just a list of all possible bag colors, we'll pop from this 
    parents = defaultdict(list)
    for color, t in ruleset.items():
        nodes.append(color)
        for c in t:
            parents[c].append(color)

    # print("PARENTS")
    # print(*parents.items(), sep='\n')

    to_visit = deque(parents['shiny gold'])
    visited = set()
    i=0
    while (to_visit) and (i < 1000):
        v = to_visit.popleft()
        if i % 10 == 0:
            print(i)
            print(f"visiting {v=}")
            print(parents[v])
        to_add = [p for p in parents[v] if p not in to_visit]
        if not to_add:
            print(f"parents for {v=} empty")
        to_visit.extend(to_add)
        visited.update([v])
        i += 1
        
    answer = len(visited)
    return answer


def parse_rules_pt2(text: str):

    source_color_expr = re.compile(r'(?P<color>[a-z\s]+) bags contain')
    source_color = source_color_expr.match(text).group('color')

    no_target = True if re.search(r'no other bags', text) else False
    has_target = not no_target

    target_expr = re.compile(r'(?:contain|,) ([0-9] [a-z\s]+ bags*)')
    children = {' '.join(t.split()[1:-1]): int(t.split()[0]) for t in target_expr.findall(text)}

    return source_color, children


def main():

    # answer_1 = part_1()
    # print(answer_1)

    pz = {r[0]: r[1] for r in map(parse_rules_pt2, utils.get_puzzle_input('test.txt').splitlines())}
    print(*pz.items(), sep='\n')

    to_visit = deque(pz['shiny gold'])
    i = 0
    while (to_visit) and (i < 10):
        
        i += 1


    
    


if __name__ == "__main__":
    main()

