#! /usr/bin/python3.10
import csv
from typing import Tuple

X_OFFSET_MIN = 400  # Arbitrarily picked based on input
X_OFFSET_MAX = 600  # Arbitrarily picked based on input
Y_OFFSET_MAX = 200  # Arbitrarily picked based on input

class Solution(object):
    def __init__(self, filename):
        self.filename = filename
        self.grid = []

    def count_fallen_sand(self, start_pos: Tuple[int], lowest_y: int) -> int:
        """Counts number of sand grains that can fall before saturation.
        
        Saturation can be defined as the point at which newly generated sand
        will fall below `lowest_y`."""

        curr_sand = start_pos
        sand_count = 0

        while curr_sand[1] <= lowest_y:
            if self.grid[curr_sand[1] + 1][curr_sand[0]] == ".":
                curr_sand = (curr_sand[0], curr_sand[1] + 1)
            elif self.grid[curr_sand[1] + 1][curr_sand[0] - 1] == ".":
                curr_sand = (curr_sand[0] - 1, curr_sand[1] + 1)
            elif self.grid[curr_sand[1] + 1][curr_sand[0] + 1] == ".":
                curr_sand = (curr_sand[0] + 1, curr_sand[1] + 1)
            else:
                self.grid[curr_sand[1]][curr_sand[0]] = "o"
                curr_sand = start_pos
                sand_count += 1
        return sand_count

    def solve(self):
        with open(self.filename) as f:
            csv_reader = csv.reader(f)
            lowest_y = -1
            SAND_START = (500 - X_OFFSET_MIN, 0)

            for _ in range(Y_OFFSET_MAX):
                curr_row = []

                for _ in range(X_OFFSET_MAX - X_OFFSET_MIN):
                    curr_row.append(".")
                
                self.grid.append(curr_row)

            for row in csv_reader:
                coords = ",".join(row).split(" -> ")
                start_x, start_y = coords[0].split(",")

                for dest_coords_idx in range(1, len(coords)):
                    dest_x, dest_y = coords[dest_coords_idx].split(",")
                    lowest_y = max(lowest_y, int(start_y), int(dest_y))

                    lo_x, hi_x = min(int(start_x), int(dest_x)), max(int(start_x), int(dest_x))
                    lo_y, hi_y = min(int(start_y), int(dest_y)), max(int(start_y), int(dest_y))

                    for y in range(lo_y, hi_y + 1):
                        for x in range(lo_x, hi_x + 1):
                            self.grid[y][x - X_OFFSET_MIN] = "#"
                    
                    start_x, start_y = dest_x, dest_y
            
            print(self.count_fallen_sand(SAND_START, lowest_y))

if __name__ == "__main__":
    sol = Solution("input.csv")
    sol.solve()
