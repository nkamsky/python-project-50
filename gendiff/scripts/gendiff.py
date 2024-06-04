#!/usr/bin/env python3

import argparse
import json


def get_files():
    parser = argparse.ArgumentParser(description=
                                     'Compares two configuration files\
                                    and shows a difference.')
    parser.add_argument('first_file', help='first_file')
    parser.add_argument('second_file', help='second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    return args.first_file, args.second_file


def generate_diff(file1, file2):
    data1 = json.load(open(file1))
    data2 = json.load(open(file2))
    keys1 = set(data1.keys())
    keys2 = set(data2.keys())
    all_keys = keys1.union(keys2)
    result = ''
    for key in sorted(all_keys):
        if key in data1 and key not in data2:
            result += f' - {key}: {data1[key]}\n'
        elif key not in data1 and key in data2:
            result += f' + {key}: {data2[key]}\n'
        else:
            if data1[key] != data2[key]:
                result += f' - {key}: {data1[key]}\n'
                result += f' + {key}: {data2[key]}\n'
            else:
                result += f'   {key}: {data2[key]}\n'
    return result


def main():
    file1, file2 = get_files()
    generate_diff(file1, file2)


if __name__ == '__main__':
    main()
