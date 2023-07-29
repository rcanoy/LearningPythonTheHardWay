# functions
def add(*args):
    a, b = args
    print("Adding %d + %d" % (a, b))
    return (a + b)

def subtract(*args):
    a, b = args
    print("Subtracting %d + %d" % (a, b))
    return (a - b)

def multiply(*args):
    a, b = args
    print("Multiplying %d * %d" % (a, b))
    return (a * b)

def divide(*args):
    a, b = args
    print("Dividing %d / %d" % (a, b))
    return (a / b)

# execution
age = add(20, 8)
height = add(multiply(32, 5), 3)
mass = add(divide(120, 2), 5)
iq = multiply(subtract(70, 50), 7)

print("""
    Age: %d,
    Height: %d,
    Mass: %d,
    IQ: %d    
""" % (age, height, mass, iq))

print("Here is a puzzle.")
what = add(subtract(multiply(mass, divide(iq, 2)), height), age)

print("That becomes: ", what, "Can you do it by hand?")