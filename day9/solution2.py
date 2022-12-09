#! /usr/bin/python3.10
import csv
from typing import List, Tuple


class Solution(object):
    def __init__(self, filename):
        self.filename = filename
        self.seen = set()
    
    def move_tail(self, head: Tuple[int], tail: Tuple[int]) -> Tuple[int]:
        """Move tail to be within one space of head and return new position."""
        new_tail = list(tail)
        x_distance = abs(head[0] - tail[0])
        y_distance = abs(head[1] - tail[1])

        if x_distance == 2:
            new_tail[0] = (head[0] + tail[0]) // 2

            if y_distance == 1:
                new_tail[1] = head[1]
        if y_distance == 2:
            new_tail[1] = (head[1] + tail[1]) // 2

            if x_distance == 1:
                new_tail[0] = head[0]
        return tuple(new_tail)

    def move(self, knots: List[Tuple[int]], motion: str) -> List[Tuple[int]]:
        """Move knots according to motion and update seen coords for tail."""
        diff = (0, 0)

        if motion[0] == "U":
            diff = (0, 1)
        elif motion[0] == "R":
            diff = (1, 0)
        elif motion[0] == "D":
            diff = (0, -1)
        else:
            diff = (-1, 0)
        
        for _ in range(int(motion[2:])):
            knots[0] = (knots[0][0] + diff[0], knots[0][1] + diff[1])

            for knot_idx in range(1, len(knots)):
                knots[knot_idx] = self.move_tail(knots[knot_idx - 1], knots[knot_idx])
            self.seen.add(knots[-1])
        
        return knots

    def solve(self):
        with open(self.filename) as f:
            csv_reader = csv.reader(f)
            knots = [(0, 0) for _ in range(10)]

            for row in csv_reader:
                knots = self.move(knots, row[0])

        print(len(self.seen))


if __name__ == "__main__":
    sol = Solution("input.csv")
    sol.solve()
