#!/usr/bin/env python3
import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split(',')
    # increase counters
    #for word in words:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
    '''
    #first attempt
    if(words[14]==None):
        words[14]="0"
    print("{0},{1}".format(words[1].strip('"'),  words[14]))
    '''
    '''
    #second attempt
    if not len(words[14]):
        continue
    print("{0},{1}".format(words[1].strip('"'),  words[14]))
    '''
    #third attempt
    try:
        print("{0},{1}".format(words[1].strip('"'),  words[14]))
    except:
        continue
                    