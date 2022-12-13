#! /usr/bin/python3.10
import csv
from collections import deque


class Solution(object):
    def __init__(self, filename):
        self.filename = filename
        self.grid = []
        self.queue = deque()
        self.end = (0, 0)
        self.seen = set()

    def shortest_path(self) -> int:
        """Finds shortest path and return the length of the path."""
        DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while self.queue:
            (curr_r, curr_c), dist = self.queue.popleft()

            for r_delta, c_delta in DIRS:
                new_r = curr_r + r_delta
                new_c = curr_c + c_delta

                if (new_r, new_c) in self.seen:
                    continue

                if 0 <= new_r < len(self.grid) and 0 <= new_c < len(
                    self.grid[0]
                ):
                    new_height = self.grid[new_r][new_c]

                    if new_height - self.grid[curr_r][curr_c] <= 1:
                        if (new_r, new_c) == self.end:
                            return dist + 1
                        self.queue.append(((new_r, new_c), dist + 1))
                        self.seen.add((new_r, new_c))

        return -1

    def solve(self):
        with open(self.filename) as f:
            csv_reader = csv.reader(f)

            for row in csv_reader:
                curr_row = []

                for idx, c in enumerate(row[0]):
                    if c == "S" or c == "a":
                        start = (len(self.grid), idx)
                        self.queue.append((start, 0))
                        curr_row.append(0)
                        self.seen.add(start)
                    elif c == "E":
                        self.end = (len(self.grid), idx)
                        curr_row.append(25)
                    else:
                        curr_row.append(ord(c) - ord("a"))

                self.grid.append(curr_row)
            print(self.shortest_path())


if __name__ == "__main__":
    sol = Solution("input.csv")
    sol.solve()
