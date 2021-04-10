#!/usr/bin/env python3

from operator import itemgetter
import sys

info = None
airlines ={}
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    #info, count = line.split(',', 1)
    current_airline, arrive_delay=line.split(',')
    # convert count (currently a string) to int
    #print(info, count)
    try:
        arrive_delay = float(arrive_delay)
        #count=int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue
    #airline, arrive_delay = info.split(',')
    #print('{0}, {1}'.format(current_airline, arrive_delay))
    try:
        if current_airline in airlines:
            airlines[current_airline].append(arrive_delay)
        else:
            airlines[current_airline] = []
            #airlines[current_airline].append(int(depart_delay))
            airlines[current_airline].append(arrive_delay)
    except:
        pass

for airline in airlines.keys():
    average_delay = sum(airlines[airline])*1.0 / len(airlines[airline])
    print('{0}, {1}'.format(airline, average_delay))