#!/usr/bin/python3
"""
a script that reads stdin line by line and computes metrics
"""
from sys import stdin

statusCodes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
               "404": 0, "405": 0, "500": 0}

size = 0


def print_stats():
    """outputs the accumulated logs"""
    print("File size: {}".format(size))
    for stats in sorted(statusCodes.keys()):
        if statusCodes[stats]:
            print("{}: {}".format(stats, statusCodes[stats]))


if __name__ == "__main__":
    count = 0
    try:
        for line in stdin:
            try:
                items = line.split()
                size += int(items[-1])
                if items[-2] in statusCodes:
                    statusCodes[items[-2]] += 1
            except:
                pass
            if count == 9:
                print_stats()
                count = -1
            count += 1
    except KeyboardInterrupt:
        print_stats()
        raise
    print_stats()
