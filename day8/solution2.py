#! /usr/bin/python3.10
import csv
from typing import List


class Solution(object):
    def __init__(self, filename):
        self.filename = filename

    def handle_blocks(self, grid: List[List[List[int]]]):
        """Updates grid with distance to taller trees in each direction."""

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                tree_height = grid[r][c][0]

                # Initialize visibility [top, bot, left, right]
                grid[r][c][1] = [r, len(grid) - r - 1, c, len(grid[0]) - c - 1]

                for other_tree_r in range(len(grid)):
                    if grid[other_tree_r][c][0] >= tree_height:
                        if r > other_tree_r:
                            grid[r][c][1][0] = min(
                                grid[r][c][1][0],
                                abs(r - other_tree_r),
                            )
                        elif r < other_tree_r:
                            grid[r][c][1][1] = min(
                                grid[other_tree_r][c][1][1],
                                abs(r - other_tree_r),
                            )

                for other_tree_c in range(len(grid[0])):
                    if grid[r][other_tree_c][0] >= tree_height:
                        if c > other_tree_c:
                            grid[r][c][1][2] = min(
                                grid[r][c][1][2],
                                abs(c - other_tree_c),
                            )
                        elif c < other_tree_c:
                            grid[r][c][1][3] = min(
                                grid[r][c][1][3],
                                abs(c - other_tree_c),
                            )

    def solve(self):
        with open(self.filename) as f:
            csv_reader = csv.reader(f)
            grid = []
            max_scenic_score = 0

            for row in csv_reader:
                grid.append([])
                for c in row[0]:
                    grid[-1].append([int(c), [-1, -1, -1, -1]])

            self.handle_blocks(grid)

            for r in range(len(grid)):
                for c in range(len(grid[0])):
                    max_scenic_score = max(
                        max_scenic_score,
                        grid[r][c][1][0]
                        * grid[r][c][1][1]
                        * grid[r][c][1][2]
                        * grid[r][c][1][3],
                    )

            print(max_scenic_score)


if __name__ == "__main__":
    sol = Solution("input.csv")
    sol.solve()
