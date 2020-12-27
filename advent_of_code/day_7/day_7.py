from advent_of_code import utils
import re
from typing import List
from dataclasses import dataclass
from collections import defaultdict, deque
from pprint import pprint
import json


def parse_rules_pt1(text: str) -> List:

    source_color_expr = re.compile(r"(?P<color>[a-z\s]+) bags contain")
    source_color = source_color_expr.match(text).group("color")

    no_target = True if re.search(r"no other bags", text) else False
    has_target = not no_target

    target_expr = re.compile(r"(?:contain|,) ([0-9] [a-z\s]+ bags*)")
    children = [" ".join(t.split()[1:-1]) for t in target_expr.findall(text)]

    return source_color, children


def part_1(filename: str):

    ruleset = {
        b[0]: b[1]
        for b in map(parse_rules_pt1, utils.get_puzzle_input(filename).splitlines())
    }
    print("RULES")
    print(*ruleset.items(), sep="\n")

    # build a dict of inner_bag -> possible outer bags
    nodes = []  # just a list of all possible bag colors, we'll pop from this
    parents = defaultdict(list)
    for color, t in ruleset.items():
        nodes.append(color)
        for c in t:
            parents[c].append(color)

    # print("PARENTS")
    # print(*parents.items(), sep='\n')

    to_visit = deque(parents["shiny gold"])
    visited = set()
    i = 0
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

    source_color_expr = re.compile(r"(?P<color>[a-z\s]+) bags contain")
    source_color = source_color_expr.match(text).group("color")

    no_target = True if re.search(r"no other bags", text) else False
    has_target = not no_target

    target_expr = re.compile(r"(?:contain|,) ([0-9] [a-z\s]+ bags*)")
    children = {
        " ".join(t.split()[1:-1]): int(t.split()[0]) for t in target_expr.findall(text)
    }

    return source_color, children


class Node(object):

    def __init__(self, color: str, quantity: int):
        self.color = color
        self.quantity = quantity
        self.children: List['Node'] = []
        
    def add_children(self, children: List['Node']):
        self.children.extend(children)

    def total_quantity_contained(self):
        print(f"resolving contents of {(self.color, self.quantity)}...")
        if self.children:
            total_contents = sum([c.total_quantity_contained() for c in self.children])
            result = (total_contents * self.quantity) + self.quantity
        else:
            result = self.quantity
        print(f"resolved: {self.color=}, {self.quantity=}, {result=}")
        if self.color == 'shiny gold':
            result -= 1
        return result
            
    def __repr__(self):
        return json.dumps(
            dict(
                color=self.color, quantity=self.quantity, total_children=len(self.children), children_colors=[c.color for c in self.children]
            )
        )


def main():

    filename = "input.txt"
    # answer_1 = part_1(filename)
    # print(answer_1)

    pz = {
        r[0]: r[1]
        for r in map(parse_rules_pt2, utils.get_puzzle_input(filename).splitlines())
    }
    print(*pz.items(), sep="\n")

    head = Node(color='shiny gold', quantity=1)
    to_visit = deque([head])
    print(f"{to_visit=}")
    i = 0
    while (to_visit):
        print(f"{i=}")
        current_node = to_visit.popleft()

        children = pz[current_node.color].items()
        print(f"{children=}")

        current_node.add_children([
            Node(color=c[0], quantity=c[1])
            for c in children
        ])
        print(f"{current_node=}")
        to_visit.extend(current_node.children)
        # print(f"{to_visit=}")

        i += 1

    answer_2 = head.total_quantity_contained()
    print(answer_2)

    


if __name__ == "__main__":
    main()
