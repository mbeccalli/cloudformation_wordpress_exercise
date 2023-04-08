#!/usr/bin/env python3
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--directory", type=str, required=True, help="Directory to search into")
parser.add_argument("-s1", "--string1", type=str, required=True, help="String to look for in title")
parser.add_argument("-s2", "--string2", type=str, required=True, help="String used to replace the title")

args = parser.parse_args()

def rename_file(dir_: str, str_1: str, str_2: str) -> None:
    for fname in os.listdir(dir_):
        new_fname = fname.replace(str_1, str_2)
        if os.path.isfile(os.path.join(dir_, fname)):
            os.rename(os.path.join(dir_, fname),os.path.join(dir_, new_fname))
        elif os.path.isdir(fname):
            rename_file(os.path.join(dir_, fname), str_1, str_2)

if __name__ == '__main__':
    rename_file(args.directory, args.string1, args.string2)
    print("Renaming completed!")
