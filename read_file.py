#!/usr/bin/python3

import sys

if len(sys.argv) < 2:
    print("Not enough arguments... exiting")
    print("Usage: python3", sys.argv[0], "filename")
    sys.exit(99)

inFile = open(sys.argv[1], "r")
while True:
    getLine = inFile.readline()
    print(getLine, end="")
    if getLine == "":
        break
