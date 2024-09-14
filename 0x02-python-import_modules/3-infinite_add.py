#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    total_sum = 0

    for t in range(1, len(sys.argv)):
        total_sum += int(sys.argv[t])
    print(total_sum)
