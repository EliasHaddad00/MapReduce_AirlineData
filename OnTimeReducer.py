#!/usr/bin/env python3

from operator import itemgetter
import sys

#current_word = None
#current_count = 0
instances_of_airline=0
total_delay=0
airline = None
temp_airline=None
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    temp_airline, temp_delay = line.split(',', 1)

    # convert count (currently a string) to int
    try:
        #count = int(count)
        temp_delay=float(temp_delay)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue
    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer

    if airline == temp_airline:
        instances_of_airline+=1
        total_delay += temp_delay
    else:
        if airline:
            # write result to STDOUT
            average_delay=total_delay/instances_of_airline
            print('{0} {1}'.format(airline, average_delay))
        #current_count = count
        #current_word = word
        airline=temp_airline
        instances_of_airline=1
        total_delay=temp_delay

# do not forget to output the last word if needed!
if airline == temp_airline:
    average_delay=total_delay/instances_of_airline
    print('{0} {1}'.format(airline, average_delay))