#! /usr/bin/python3.10
import csv
import sys
from typing import List, Optional


class File(object):
    """Representation of a file in a filesystem."""

    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size


class Folder(object):
    """Representation of a folder in a filesystem."""

    def __init__(self, name: str, parent: Optional["Folder"]):
        self.name = name
        self.files: List[File] = []
        self.subfolders: List[Folder] = []
        self.parent = parent

    def size(self) -> int:
        """Returns total size of all files and subfolders' files."""
        total_size = 0

        for f in self.files:
            total_size += f.size

        for folder in self.subfolders:
            total_size += folder.size()

        return total_size

    def add_file(self, f: File):
        """Adds given file to current folder's files."""
        self.files.append(f)

    def add_folder(self, folder: "Folder"):
        """Adds given folder to current folder's subfolders."""
        self.subfolders.append(folder)

    def get_subfolder(self, name: str) -> "Folder":
        """Returns Folder object with given name in subfolders."""
        for folder in self.subfolders:
            if folder.name == name:
                return folder


class Solution(object):
    def __init__(self, filename):
        self.filename = filename
        self.root = Folder("/", None)
        self.curr = self.root

    def handle_command(self, command: str):
        """Parses terminal entry and handles output appropriately.

        In particular, there are 2 base commands:
        - cd
        - ls

        Since "ls" is handled by `solve()`, this function specifically handles
        "cd", which has the following sub-commands:
        - cd /
        - cd <folder>
        - cd ..
        """

        # Do nothing for ls
        if command == "$ ls":
            return
        elif command[:6] == "$ cd /":
            self.curr = self.root
        elif command[:6] == "$ cd .":
            self.curr = self.curr.parent
        else:
            self.curr = self.curr.get_subfolder(command[5:])

    def find_smallest_over_size(self, size: int) -> int:
        """Returns size of smallest folder of size over `size`.

        Uses BFS to check each folder's size and iteratively check all
        child folders to identify folders with size >= `size`."""

        min_size_over_req = sys.maxsize

        queue = [self.root]
        next_queue = []

        while queue:
            for folder in queue:
                folder_size = folder.size()

                if folder_size >= size:
                    min_size_over_req = min(min_size_over_req, folder_size)

                next_queue.extend(folder.subfolders)

            queue = next_queue
            next_queue = []

        return min_size_over_req

    def solve(self):
        with open(self.filename) as f:
            csv_reader = csv.reader(f)
            TOTAL_SIZE = 70000000
            REQ_SIZE = 30000000

            for row in csv_reader:
                # cd or ls command
                if row[0][0] == "$":
                    self.handle_command(row[0])
                # Directory
                elif row[0][0] == "d":
                    self.curr.add_folder(Folder(row[0][4:], self.curr))
                # File
                elif row[0][0].isnumeric():
                    size, name = row[0].split(" ")
                    self.curr.add_file(File(name, int(size)))
            
            unused_space = TOTAL_SIZE - self.root.size()
            remaining_size_to_free = REQ_SIZE - unused_space
            
            print(self.find_smallest_over_size(remaining_size_to_free))


if __name__ == "__main__":
    sol = Solution("input.csv")
    sol.solve()
