#! /usr/bin/python3.10
import csv
from collections import defaultdict


class Solution(object):
    def __init__(self, filename):
        self.filename = filename

    def solve(self):
        with open(self.filename) as f:
            csv_reader = csv.reader(f)
            NUM_CHARS = 14

            for row in csv_reader:
                buffer = row[0]
                counts = defaultdict(int)

                for idx, c in enumerate(buffer):
                    counts[c] += 1

                    if idx > NUM_CHARS - 1:
                        counts[buffer[idx - NUM_CHARS]] -= 1

                        if counts[buffer[idx - NUM_CHARS]] == 0:
                            del counts[buffer[idx - NUM_CHARS]]

                    if len(counts) == NUM_CHARS:
                        print(idx + 1)
                        return


if __name__ == "__main__":
    sol = Solution("input.csv")
    sol.solve()
