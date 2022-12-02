#! /usr/bin/python3.10
import csv
from heapq import heappushpop


class Solution(object):
    def __init__(self, filename):
        self.filename = filename

    def solve(self):
        MAX_SIZE = 3

        with open(self.filename) as f:
            csv_reader = csv.reader(f)

            calories = [0 for _ in range(MAX_SIZE)]
            curr_calories = 0

            for row in csv_reader:
                # Rows with numbers
                if len(row) > 0:
                    curr_calories += int(row[0])
                else:
                    heappushpop(calories, curr_calories)
                    curr_calories = 0
            
            heappushpop(calories, curr_calories)

        print(sum(calories))


if __name__ == "__main__":
    sol = Solution("input.csv")
    sol.solve()
