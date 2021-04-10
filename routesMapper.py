#!/usr/bin/env python3

import sys

airlines={"B6","G4","MQ"}
# input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.strip()
    # split the line into words
    info = line.split(',')
    # increase counters
    try:
        airline = info[1].strip('"')
        if  airline in airlines:
            #orgin, dest, arrival_delay
            print('{0}, {1}, {2}, {3}'.format(airline, info[4].strip('"') , info[9].strip('"'), info[14]))
    except:
        pass   