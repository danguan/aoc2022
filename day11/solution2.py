#! /usr/bin/python3.10
import csv
import math
from typing import Callable, List
from heapq import heappushpop, heappush

class Monkey(object):
    """Representation of a Monkey and its various characteristics/operations"""

    def __init__(self):
        self.items = []
        self.operation = None
        self.test = None
        self.test_true_target = -1
        self.test_false_target = -1
        self.inspected = 0
    
    def set_items(self, items: List[int]):
        self.items = items
    
    def set_operation(self, operation: str):
        self.operation = operation
    
    def set_test(self, test: int):
        self.test = test
    
    def set_test_true_target(self, test_true_target: int):
        self.test_true_target = test_true_target

    def set_test_false_target(self, test_false_target: int):
        self.test_false_target = test_false_target

class Solution(object):
    def __init__(self, filename):
        self.filename = filename
    
    def solve(self):
        with open(self.filename) as f:
            csv_reader = csv.reader(f)
            monkeys = []
            curr_monkey = Monkey()
            
            for row in csv_reader:
                if not row:
                    monkeys.append(curr_monkey)
                    curr_monkey = Monkey()
                elif "Starting" in row[0]:
                    items = [int(row[0].split(": ")[1])]
                    for item in row[1:]:
                        items.append(int(item))
                    curr_monkey.set_items(items)
                elif "Operation" in row[0]:
                    curr_monkey.set_operation(row[0].split("= ")[1])
                elif "Test" in row[0]:
                    curr_monkey.set_test(int(row[0].split(" ")[-1]))
                elif "true" in row[0]:
                    curr_monkey.set_test_true_target(int(row[0][-1]))
                elif "false" in row[0]:
                    curr_monkey.set_test_false_target(int(row[0][-1]))
            
            monkeys.append(curr_monkey)
            lcm = math.lcm(*list([monkey.test for monkey in monkeys]))
        
            for round in range(10000):
                for monkey in monkeys:
                    for old in monkey.items:
                        new_item = eval(monkey.operation)
                        new_item %= lcm

                        if new_item % monkey.test == 0:
                            monkeys[monkey.test_true_target].items.append(new_item)
                        else:
                            monkeys[monkey.test_false_target].items.append(new_item)

                        monkey.inspected += 1
                    monkey.set_items([])
            
            max_values = []
            
            for monkey in monkeys:
                if len(max_values) < 2:
                    heappush(max_values, monkey.inspected)
                else:
                    heappushpop(max_values, monkey.inspected)

            print(max_values[0] * max_values[1])


if __name__ == "__main__":
    sol = Solution("input.csv")
    sol.solve()
