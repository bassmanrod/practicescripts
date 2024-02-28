import re
import sys
import argparse

#parser = argparse.ArgumentParser()
parser = argparse.ArgumentParser(
    description='Extract the accounts and their home directories from the passwd file.',
    epilog="End"
)

parser.add_argument('filename')
parser.add_argument('--version', '-v', action='version', version='%(prog)s 1.0')

args = parser.parse_args()

with open(args.filename) as file:
    
    for line in file:
        
        match = re.search(r'\S+:', line)
        if match:
            values = line.split(":")
            print("{:<30} {:<30}".format(values[0],values[5]))

