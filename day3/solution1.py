#! /usr/bin/python3.10
import csv


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

    def solve(self):
        with open(self.filename) as f:
            csv_reader = csv.reader(f)
            priority_total = 0

            for row in csv_reader:
                first_compartment = set()

                for item_idx in range(len(row[0]) // 2):
                    first_compartment.add(row[0][item_idx])

                for item_idx in range(len(row[0]) // 2, len(row[0])):
                    if row[0][item_idx] in first_compartment:
                        priority_total += self.convert_priority(
                            row[0][item_idx]
                        )
                        break

        print(priority_total)


if __name__ == "__main__":
    sol = Solution("input.csv")
    sol.solve()
