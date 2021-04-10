#!/usr/bin/env python3

from operator import itemgetter
import sys

routes ={}
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    current_airline, origin, dest, arrive_delay = line.split(',')
    #print('{0}, {1}, {2}, {3}'.format(current_airline, origin, dest, arrive_delay))
    route = "-".join([current_airline, origin, dest])
    #airline, arrive_delay=line.split(',',1)
    #print('{0}'.format(route))
    # convert count (currently a string) to int
    try:
        #arrive_delay = int(arrive_delay)
        arrive_delay=float(arrive_delay)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue
    try:
        if route in routes:
            routes[route].append(arrive_delay)

        else:
            routes[route] = []
            #routes[current_airline].append(int(depart_delay))
            routes[route].append(arrive_delay)
    except:
        pass

for route in routes.keys():
    average_delay = sum(routes[route])*1.0 / len(routes[route])
    print('{0}, {1}'.format(route, average_delay))