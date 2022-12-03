#! /usr/bin/python3.10
import csv


class Solution(object):
    def __init__(self, filename):
        self.filename = filename

    def calcPlayedRoundPoints(self, player: str, opponent: str):
        """Calculates points gained for the round played by the player."""

        # Points for playing rock, paper, or scissors respectively
        rps_points = [1, 2, 3]
        # Index of opponent's played hand
        opponent_idx = ord(opponent) - ord("A")

        if player == "X":
            return rps_points[opponent_idx - 1]
        elif player == "Y":
            return rps_points[opponent_idx]
        else:
            return rps_points[(opponent_idx + 1) % len(rps_points)]

    def solve(self):
        wdl_scores = {
            "X": 0,
            "Y": 3,
            "Z": 6,
        }

        with open(self.filename) as f:
            csv_reader = csv.reader(f)
            total_score = 0

            for row in csv_reader:
                opponent = row[0][0]
                player = row[0][2]
                total_score += wdl_scores[player] + self.calcPlayedRoundPoints(
                    player, opponent
                )

        print(total_score)


if __name__ == "__main__":
    sol = Solution("input.csv")
    sol.solve()
