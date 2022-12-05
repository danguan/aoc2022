#! /usr/bin/python3.10
import csv
from typing import List


class Solution(object):
    def __init__(self, filename):
        self.filename = filename

    def build_stacks(self, stacks: List[List], csv_reader: csv.reader):
        """Creates Python stack representation of boxes from `csv_reader`."""
        for row in csv_reader:
            # Terminate early, i.e. when all box rows have been processed
            if row and row[0][1].isnumeric():
                # Flip stacks due to reverse processing (top -> bottom)
                for stack in stacks:
                    stack.reverse()
                break

            stack_idx = 0
            for idx in range(1, len(row[0]), 4):
                if len(stacks) == stack_idx:
                    stacks.append([])
                if row[0][idx] != " ":
                    stacks[stack_idx].append(row[0][idx])
                stack_idx += 1

    def process_moves(self, stacks: List[List], csv_reader: csv.reader):
        """Parses moves from `csv_reader` and moves boxes within `stacks`."""
        for row in csv_reader:
            # Scan for "move" to identify moves
            if row and row[0][0] == "m":
                split_instruction = row[0].split(" ")
                count, source, dest = (
                    int(split_instruction[1]),
                    int(split_instruction[3]) - 1,  # 0-index stack
                    int(split_instruction[5]) - 1,  # 0-index stack
                )
                for _ in range(count):
                    stacks[dest].append(stacks[source].pop())

    def solve(self):
        with open(self.filename) as f:
            csv_reader = csv.reader(f)
            stacks = []
            res = ""

            self.build_stacks(stacks, csv_reader)
            self.process_moves(stacks, csv_reader)

            for stack in stacks:
                res += stack[-1]

            print(res)


if __name__ == "__main__":
    sol = Solution("input.csv")
    sol.solve()
