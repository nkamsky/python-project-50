#!/usr/bin/env python3

import argparse
from gendiff.modules.generate_diff import generate_diff


def get_files():
    parser = argparse.ArgumentParser(description='\
                                    Compares two configuration files\
                                    and shows a difference.')
    parser.add_argument('first_file', help='first_file')
    parser.add_argument('second_file', help='second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    return args.first_file, args.second_file


def main():
    file1, file2 = get_files()
    generate_diff(file1, file2)


if __name__ == '__main__':
    main()
