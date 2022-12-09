#! /usr/bin/python3.10
import csv
from typing import Tuple


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

    def move(self, head: Tuple[int], tail: Tuple[int], motion: str) -> Tuple[Tuple[int], Tuple[int]]:
        """Move head and tail according to motion and update seen coords."""
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
            head = (head[0] + diff[0], head[1] + diff[1])
            tail = self.move_tail(head, tail)
            self.seen.add(tail)
        
        return (head, tail)

    def solve(self):
        with open(self.filename) as f:
            csv_reader = csv.reader(f)
            head = (0, 0)
            tail = (0, 0)

            for row in csv_reader:
                head, tail = self.move(head, tail, row[0])

        print(len(self.seen))


if __name__ == "__main__":
    sol = Solution("input.csv")
    sol.solve()
