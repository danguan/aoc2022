#! /usr/bin/python3.10
import csv


class Solution(object):
    def __init__(self, filename):
        self.filename = filename

    def calcWDLPoints(self, player: str, opponent: str):
        """Calculates points gained for a win/draw/loss."""

        player_opponent_win = {
            "X": "C",
            "Y": "A",
            "Z": "B",
        }

        if player_opponent_win[player] == opponent:
            return 6
        elif (ord(player) - ord("X")) == (ord(opponent) - ord("A")):
            return 3
        else:
            return 0

    def solve(self):
        played_scores = {
            "X": 1,
            "Y": 2,
            "Z": 3,
        }

        with open(self.filename) as f:
            csv_reader = csv.reader(f)
            total_score = 0

            for row in csv_reader:
                opponent = row[0][0]
                player = row[0][2]
                total_score += played_scores[player] + self.calcWDLPoints(
                    player, opponent
                )

        print(total_score)


if __name__ == "__main__":
    sol = Solution("input.csv")
    sol.solve()
