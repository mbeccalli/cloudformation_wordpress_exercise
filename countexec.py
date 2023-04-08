#!/usr/bin/env python3
import argparse
import os
from collections import defaultdict

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--directory", type=str, required=True, help="Directory to search into")

args = parser.parse_args()

def countexec(dir_) -> None:
    # taking only files from the directory
    files_ = [f for f in os.listdir(dir_) if os.path.isfile(os.path.join(dir_, f))]
    counter_dict = defaultdict(int)

    for f in files_:
    # catching non-text data and pass
        try:
            with open(os.path.join(dir_, f), "r", encoding='utf-8') as opened_file:
                shebang_ = opened_file.readline()
                if shebang_[:2] == "#!":
                    counter_dict[shebang_] += 1
        except UnicodeDecodeError:
            pass

    # printing results
    for c, s in counter_dict.items():
        print(f"{s} {c}")

if __name__ == '__main__':
    countexec(args.directory)
