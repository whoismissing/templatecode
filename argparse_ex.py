#!/usr/bin/python3

import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target"
        , help="Specify a target host: Default is 192.168.1.1"
        , type=str, action="store", default="192.168.1.1")
    parser.add_argument("-d", "--debug"
        , help="Turn debug output on: Default is 0"
        , type=int, action="store", default=0)
    args = parser.parse_args()

    target = args.target
    debug = args.debug

    print("Target = ", target)
    print("Debug = ", debug)

if __name__ == "__main__":
    main()
