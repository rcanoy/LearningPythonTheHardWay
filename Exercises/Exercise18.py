# this one is like your scripts with argv
## *args: similar to argv, but for function
def print_two(*args):
    arg1, arg2 = args
    print("Prints %s and %s." % (arg1, arg2))

def print_two_again(arg1, arg2):
    print("Prints %s and %s." % (arg1, arg2))

def print_one(arg):
    print("Prints a single argument %s" % arg)

def print_none():
    print("Does not hold any argument.")

print_two("arg1", "arg2")
print_two_again("arg1", "arg2")
print_one("arg")
print_none()