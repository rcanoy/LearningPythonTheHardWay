# close(): closes the file.
# read(): reads the contents of the file, and assigns the results to a variable
# readline(): reads just one line of a text file
# truncate(): empties the file, watch out if you care about the file
# write(stuff): writes stuff to the file

# imports argv
from sys import argv

# assigns the value of script and filename to argv
# $ python Exercise16.py Exercise16_test.txt
script, filename = argv

print("We're going to erase %r." % filename)
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
# open(): opens the file
target = open(filename, 'w')

print("Truncating the file. Goodbye.")
# file.truncate(): removes the contents
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")
# file.write(): writes values on the file
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close()