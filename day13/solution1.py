#! /usr/bin/python3.10
import csv
import json

class Solution(object):
    def __init__(self, filename):
        self.filename = filename

    def pairs_correctly_ordered(self, pair_1, pair_2) -> bool:
        """Determines if the given pairs are correctly ordered."""
        for idx in range(max(len(pair_1), len(pair_2))):
            # First pair is longer
            if idx > len(pair_2) - 1:
                return False
            # Second pair is longer
            elif idx > len(pair_1) - 1:
                return True
            
            curr_1 = pair_1[idx]
            curr_2 = pair_2[idx]

            if isinstance(curr_1, int) and isinstance(curr_2, int):
                if curr_1 < curr_2:
                    return True
                elif curr_1 > curr_2:
                    return False
            else:
                if isinstance(curr_1, int):
                    curr_1 = [curr_1]
                elif isinstance(curr_2, int):
                    curr_2 = [curr_2]

                res = self.pairs_correctly_ordered(curr_1, curr_2)
                if res is not None:
                    return res
                
        return None


    def solve(self):
        with open(self.filename) as f:
            csv_reader = csv.reader(f)
            pair_1 = [(), False]
            pair_2 = [(), False]
            pair_idx = 1
            sum_pair_idx = 0

            for row in csv_reader:
                if not row:
                    continue
                if not pair_1[1]:
                    s_1 = ",".join(row)
                    pair_1 = (json.loads(s_1), True)
                elif not pair_2[1]:
                    s_2 = ",".join(row)
                    pair_2 = (json.loads(s_2), True)

                    if self.pairs_correctly_ordered(pair_1[0], pair_2[0]):
                        print("correct: ",pair_1,"---",pair_2)
                        sum_pair_idx += pair_idx

                    pair_idx += 1
                    pair_1 = [(), False]
                    pair_2 = [(), False]
            print(sum_pair_idx)


if __name__ == "__main__":
    sol = Solution("input.csv")
    sol.solve()
