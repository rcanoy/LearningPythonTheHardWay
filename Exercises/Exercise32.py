# lists
hairs = ["black", "brown", "blonde", "red"]
eyes = ["brown", "blue", "green"]
weights = [1, 2, 3, 4]

the_count = [1, 2, 3, 4, 5]
fruits = ["apples", "oranges", "pears", "apricots"]
change = [1, 'pennies', 2, 'dimes', '3', 'quarters']

# loops through a list that contains numbers
for number in the_count:
    print("The number is %d." % number)
    
# loops through a list that contains strings
for fruit in fruits:
    print("The fruit is %s" % fruit)
    
# loops through a list that contains both integers and strings
for val in change:
    print("The value is %r" % val)
    
    
# building the list
elements = []
for element in range(0, 6):
    print("Appending %d into a list" % element)
    elements.append(element)

# looping through each element in a list
for element in elements:
    print("""
          The element is %d.
          """ % element)
    

# extra credit: one liner list construction
elements_new = [val for val in range(0, 6)]
print(elements_new)