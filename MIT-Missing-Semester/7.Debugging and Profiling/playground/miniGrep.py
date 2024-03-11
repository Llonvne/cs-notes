#!/usr/bin/env python
import sys, re

from line_profiler import profile


@profile
def grep(pattern, file):
    pattern = re.compile(pattern)
    with open(file, 'r') as f:
        # print(file)
        for i, line in enumerate(f.readlines()):
            match = pattern.search(line)
            if match is not None:
                # print("{}: {}".format(i, line), end="")
                pass

if __name__ == '__main__':
    times = int(sys.argv[1])
    pattern = sys.argv[2]
    for i in range(times):
        for file in sys.argv[3:]:
            grep(pattern, file)

