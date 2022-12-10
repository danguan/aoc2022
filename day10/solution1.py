#! /usr/bin/python3.10
import csv

class Solution(object):
    def __init__(self, filename):
        self.filename = filename
        self.seen = set()
    
    def solve(self):
        with open(self.filename) as f:
            csv_reader = csv.reader(f)
            signal_strength = 0
            register_value = 1
            next_breakpoint = 20
            cycle = 0
            
            for row in csv_reader:
                value = 0
                if row[0] == "noop":
                    cycle += 1
                else:
                    value = int(row[0].split(" ")[1])
                    cycle += 2

                while cycle >= next_breakpoint and next_breakpoint <= 220:
                    signal_strength += next_breakpoint * register_value
                    next_breakpoint += 40

                if next_breakpoint > 220:
                    break
                
                register_value += value

        print(signal_strength)


if __name__ == "__main__":
    sol = Solution("input.csv")
    sol.solve()
