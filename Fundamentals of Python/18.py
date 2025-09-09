# Accepting Arguments from Command lines
import sys 
import argparse

# name = sys.argv[1]
# print("Hello it's me " + name)

parser = argparse.ArgumentParser(
    description='This program prints your gender'
)

parser.add_argument('-g','--gender',metavar='gender', required=True,choices={'male','female','transgender','other'},help='gender that you want to display')

args = parser.parse_args()

print(args.gender)