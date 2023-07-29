from sys import argv

# $ python script, filename
script, filename = argv

# opens the file
file = open(filename, 'w')

# assigns values to the variables
print(
    """
    We're going to write on an empty file.
    Please write three lines below.
    """)
line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

# writes the values of the variables on an empty file
file.write(
    """
    \n%s
    \n%s
    \n%s
    """ % (line1, line2, line3)
)