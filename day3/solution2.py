#! /usr/bin/python3.10
import csv
from typing import List


class Solution(object):
    def __init__(self, filename):
        self.filename = filename

    def convert_priority(self, item: str) -> int:
        """Returns priority of item based on casing.

        e.g.
            'a' -> 'z' = 1 -> 26
            'A' -> 'Z' = 27 -> 52
        """
        if ord("z") >= ord(item) >= ord("a"):
            return ord(item) - ord("a") + 1

        return ord(item) - ord("A") + 27

    def get_shared_item_priority(self, seen_sets: List[set]) -> int:
        """Finds the shared item across seen_sets and return its priority"""
        for item in seen_sets[-1]:
            found_in_sets = 0

            for seen_set in seen_sets:
                if item in seen_set:
                    found_in_sets += 1

                    if found_in_sets == len(seen_sets):
                        return self.convert_priority(item)

        return -1

    def solve(self):
        with open(self.filename) as f:
            csv_reader = csv.reader(f)
            priority_total = 0
            seen_sets = []

            for idx, row in enumerate(csv_reader):
                seen_sets.append(set())

                for item in row[0]:
                    seen_sets[-1].add(item)

                if (idx + 1) % 3 == 0:
                    priority_total += self.get_shared_item_priority(seen_sets)
                    seen_sets = []

        print(priority_total)


if __name__ == "__main__":
    sol = Solution("input.csv")
    sol.solve()
