from sys import argv

# argument variables
script, filename = argv

# assigns the contents of the file to the variable txt
txt = open(filename)

# prints the filename
print("Here's your file %r: " % filename)
# prints the contents of the *.txt file
print(txt.read())

# prints the instruction
print("I'll also ask you to type it again:")
# asks for the filename and assigns it to the variable file_again
file_again = input("> ")

# opens the file
txt_again = open(file_again) # String has no open() attribute
# prints the contents of the file
print(txt_again.read())

# closes the file assigned to the  variable txt
txt.close()
# closes the file assigned to the variable txt_again
txt_again.close()
