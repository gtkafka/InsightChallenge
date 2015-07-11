# This is a submission to the InsightData Challege written by Gene Kafka.

This script was written using the PyCharm IDE and complied with python 2.7 on Mac OSX 10.10.3

The file run.sh specifies the input file tweet_input/eecummings.txt. This file contains a collection of ee. cummings poetry and is for all intents and purposes used in lieu of a twitter stream.

run.sh calls src/main.py which creates out_input/eecummings.txt.

#Dependcies
python modules:
heapq     -- a heap module used for calculating the median.
fileinput -- used to handle multiple input files.
string    -- used to specify charaters to be excluded
