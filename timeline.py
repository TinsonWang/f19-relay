#!/usr/bin/env python3

import sys

##Usage: ./timeline.py INPUT [OUTPUT]
##INPUT is path of file. They will be plain text, new-line delimited files
##OUTPUT is an optional path to the output file
##Output is a graph based on contents of input.

##Eric
#you will accept an input like "(0,1;2,5;6,9)"
#then make output to be "/\/||"
# a number or symbol like 0 or 1 or 2 or ; or , corresponds to a symbol. either /\ or _ or / or \ or |
if(argv[1][1] == '0')
    #print one of the symbols

if(argv[1][2] == ';')
    #print symbol

def main(args):
    print("Hello world!")

    return 0

if __name__ == "__main__":
    main(sys.argv)


##Reading from command-line arguments for input
with open(args[1], 'r') as input:
    for line in input:
        print(line)

##Reading from command-line arguments for output
##Write _ to indicate idle state
##/ to indicate resuming from idle
##| to indicate activity
##\ to indicate returning to idle
with open(args{2}, 'w') as output:
    f.write("...")
