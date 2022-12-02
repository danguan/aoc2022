#! /usr/bin/python3.10
import csv


class Solution(object):
    def __init__(self, filename):
        self.filename = filename

    def solve(self):
        with open(self.filename) as f:
            csv_reader = csv.reader(f)

            calories = [0]

            for row in csv_reader:
                # Rows with numbers
                if len(row) > 0:
                    calories[-1] += int(row[0])
                else:
                    calories.append(0)

        print(max(calories))


if __name__ == "__main__":
    sol = Solution("input.csv")
    sol.solve()
