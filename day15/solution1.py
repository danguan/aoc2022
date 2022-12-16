#! /usr/bin/python3.10
import csv
from typing import List, Tuple

Y_TARGET = 2000000


class Solution(object):
    def __init__(self, filename):
        self.filename = filename

    def dist(self, x1: int, y1: int, x2: int, y2: int) -> int:
        """Returns Manhattan distance between input set of coordinates."""

        return abs(x1 - x2) + abs(y1 - y2)

    def occupied_range_for_target_y(
        self, x: int, y: int, dist: int, target_y: int
    ) -> Tuple[int, int]:
        """Returns tuple representing range of occupied x coords for target y.

        Uses principle that each additional dist past y is equal to one dist
        in each x direction.

        If point + dist cannot reach target y, return (0, 0), i.e. Tuple of
        range size = 0.
        """
        dist_from_target = abs(target_y - y)

        if dist_from_target > dist:
            return (0, 0)

        excess_dist = dist - dist_from_target
        return (x - excess_dist, x + excess_dist + 1)

    def merge_ranges(
        self, ranges: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        """Merge overlapping input sorted ranges and return merged output."""
        merged_ranges = []
        lo = ranges[0][0]
        hi = ranges[0][1]

        for idx in range(len(ranges)):
            curr = ranges[idx]

            if hi >= curr[0]:
                hi = max(hi, curr[1])
            else:
                merged_ranges.append([lo, hi])
                lo = curr[0]
                hi = curr[1]

            if idx == len(ranges) - 1 and (
                not merged_ranges
                or merged_ranges[-1][0] != lo
                or merged_ranges[-1][1] != hi
            ):
                merged_ranges.append([lo, hi])

        return merged_ranges

    def solve(self):
        with open(self.filename) as f:
            csv_reader = csv.reader(f)
            sensors_dists = []
            occupied_ranges = []
            target_y_beacons = set()
            positions_occupied = 0

            for row in csv_reader:
                sensor_x = int(row[0].split("=")[1])
                sensor_y = int(row[1].split(":")[0][3:])
                beacon_x = int(row[1].split("=")[2])
                beacon_y = int(row[2].split("=")[1])

                sensors_dists.append(
                    (
                        sensor_x,
                        sensor_y,
                        self.dist(sensor_x, sensor_y, beacon_x, beacon_y),
                    )
                )
                if beacon_y == Y_TARGET:
                    target_y_beacons.add(beacon_x)

            for x, y, dist in sensors_dists:
                occupied_ranges.append(
                    self.occupied_range_for_target_y(x, y, dist, Y_TARGET)
                )

            occupied_ranges.sort(
                key=lambda interval: (interval[0], interval[1])
            )
            occupied_ranges = self.merge_ranges(occupied_ranges)

            for lo, hi in occupied_ranges:
                positions_occupied += hi - lo

                # Do not count spaces where beacons already occupy
                for x in target_y_beacons:
                    if lo <= x < hi:
                        positions_occupied -= 1

            print(positions_occupied)


if __name__ == "__main__":
    sol = Solution("input.csv")
    sol.solve()
