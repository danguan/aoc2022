#! /usr/bin/python3.10
import csv
from typing import List


class Solution(object):
    def __init__(self, filename):
        self.filename = filename

    def is_overlapped(
        self, first_pair: List[str], second_pair: List[str]
    ) -> bool:
        """Returns whether first_pair/second_pair overlap at all."""

        first_ints = [int(s) for s in first_pair]
        second_ints = [int(s) for s in second_pair]

        return not (first_ints[1] < second_ints[0] or second_ints[1] < first_ints[0])

    def solve(self):
        with open(self.filename) as f:
            csv_reader = csv.reader(f)
            overlap = 0

            for row in csv_reader:
                first_pair = row[0].split("-")
                second_pair = row[1].split("-")

                if self.is_overlapped(first_pair, second_pair):
                    overlap += 1

        print(overlap)


if __name__ == "__main__":
    sol = Solution("input.csv")
    sol.solve()
