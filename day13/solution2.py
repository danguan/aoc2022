#! /usr/bin/python3.10
import csv
import json
from typing import List

class Solution(object):
    def __init__(self, filename):
        self.filename = filename

    def sort_packets(self, packets):
        """Flattens and sorts input packets in place."""
        for idx, packet in enumerate(packets):
            packets[idx] = self.packet_value(packet)

        packets.sort()
        

    def packet_value(self, packet) -> List[int]:
        """Flattens packet and returns it as a 1D list."""
        flat_packet = []

        if not packet:
            return [0]

        for item in packet:
            if isinstance(item, int):
                flat_packet.append(item)
            else:
                flat_packet.extend(self.packet_value(item))
        
        return flat_packet
        


    def solve(self):
        with open(self.filename) as f:
            csv_reader = csv.reader(f)
            packets = []
            two_idx = -1
            six_idx = -1

            for row in csv_reader:
                if not row:
                    continue
                s_1 = ",".join(row)
                packets.append(json.loads(s_1))
            packets.append([[2]])
            packets.append([[6]])
            self.sort_packets(packets)
            
            for idx, packet in enumerate(packets):
                if packet == [2]:
                    two_idx = idx + 1
                if packet == [6]:
                    six_idx = idx + 1
                    break
            
            print(two_idx * six_idx)


if __name__ == "__main__":
    sol = Solution("input.csv")
    sol.solve()
