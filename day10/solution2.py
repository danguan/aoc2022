#! /usr/bin/python3.10
import csv

class Solution(object):
    def __init__(self, filename):
        self.filename = filename
        self.seen = set()
    
    def solve(self):
        with open(self.filename) as f:
            csv_reader = csv.reader(f)
            WIDTH_IN_PIXELS = 40
            HEIGHT_IN_PIXELS = 6
            SPRITE_WIDTH = 3
            sprite_head_pos = 0
            cycle = 0
            output = [["." for _ in range(WIDTH_IN_PIXELS)] for _ in range(HEIGHT_IN_PIXELS)]
            
            for row in csv_reader:
                if sprite_head_pos <= (cycle % WIDTH_IN_PIXELS) <= sprite_head_pos + SPRITE_WIDTH - 1:
                    output[cycle // WIDTH_IN_PIXELS][cycle % WIDTH_IN_PIXELS] = "#"
                cycle += 1
                
                if row[0] == "noop":
                    continue
                
                value = int(row[0].split(" ")[1])
                if sprite_head_pos <= (cycle % WIDTH_IN_PIXELS) <= sprite_head_pos + SPRITE_WIDTH - 1:
                    output[cycle // WIDTH_IN_PIXELS][cycle % WIDTH_IN_PIXELS] = "#"
                cycle += 1
                sprite_head_pos += value


        print("\n".join([" ".join(row) for row in output]))


if __name__ == "__main__":
    sol = Solution("input.csv")
    sol.solve()
