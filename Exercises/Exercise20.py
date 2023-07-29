# imports
from sys import argv, orig_argv
from os.path import exists
import os

# argument variables
script, input_file = argv

# functions
def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline())

# execution
if exists(input_file):
    file = open(input_file)
else:
    os.mknod(input_file)

## print the whole file
print_all(file)

## rewind
rewind(file)

## prints three lines
#current_line = 0
#for i in range(len(file.read())):
#    current_line += 1
#    print_a_line(current_line, file)

current_line = 1
print_a_line(current_line, file)

current_line += 1
print_a_line(current_line, file)

current_line += 1
print_a_line(current_line, file)