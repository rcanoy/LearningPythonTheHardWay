# Book's Codes
#from ast import arg
#from sys import argv
#from os.path import exists

#script, from_file, to_file = argv

#print("Copying from %s to %s" % (from_file, to_file))

#input = open(from_file)
#indata = input.read()

#print("The input file is %d bytes long." % len(indata))

#print("Does the output file exist? %r" % exists(to_file))
#print("Ready, hit RETURN to continue, CTRL-C to abort.")
#input()

#output = open(to_file, 'w')
#output.write(indata)

#print("Alright, all done")

#output.close()
#input.close()


# Personal Codes
from sys import argv
from os.path import exists
import os

# $ python script, from_file, to_file
script, from_file, to_file = argv

# opening message
print("Copying from %s to %s" % (from_file, to_file))

# input file
input = open(from_file, 'r')
indata = input.read()

## calculates the length of the input file
indata_len = len(indata)
print("The length of the inputted data is %r." % (indata_len))

# output file
if exists(to_file):
    output = open(to_file, 'w')
    output = output.write(indata)
else:
    os.mknod(to_file)
    output = open(to_file, 'w')
    output = output.write(indata)

input.close()
output.close()

