# -*- coding: utf-8 -*-

import argparse
import os, sys
from pathlib import Path
import random

def read_bases():
    folder_path = Path(__file__).parent.parent / "words"
    if not folder_path.is_dir():
        raise SystemExit("Not found a folder with words!!!")
    files = {}
    for f in folder_path.iterdir():
        if f.is_file() and str(f).endswith(".txt"):
            files[f.name.replace(".txt", "")] = str(f)
    return files


def main():
    words = read_bases()
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-s', '--start', required=True,nargs='?', help='start signal index', type=int)
    parser.add_argument('-c', '--count', required=True, nargs='?', help='limit generated signals', type=int)
    parser.add_argument('-w', '--word', required=True, action='append', nargs='?', choices=words.keys(), help='word types', type=str)

    args = parser.parse_args()
    for signal in generate(args.start, args.count, [v for k, v in words.items() if k in args.word]):
        print(signal)


def generate(start_digit, count, files):
    words = []
    for f in files:
        with open(f) as ff:
            words += [line.strip() for line in ff]
    if count > len(words):
        raise SystemExit("There are words less than needed limit")
    words = list(set(words))
    random.shuffle(words)

    for i in range(count):
        word =words[i]
        if not word.isdigit():
            word += "-" + str(start_digit + i)
        yield word.upper()



main()
