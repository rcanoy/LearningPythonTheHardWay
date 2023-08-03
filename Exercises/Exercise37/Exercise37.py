## Keywords
# 1) del keyword
# defining an object
class myClass:
    name = "John"
    
print(myClass)

# defining a variable
x = 'Hello'
print(x)

# defining a list
y = ["apple", "banana", "cherry"]
print(y[0])

# deleting an object and a variable
del myClass, x, y[0]
#print(myClass, x, y[0])


## 2) global keyboard
def myFunc():
    global z 
    z = "This is a global variable"
    
    print(z)
    
myFunc()
print(z)

## 3) assert keyword
a = "Hello"

assert a == "Goodbye", "a should be 'Hello'"

## 4) yield keyword
def find_even(list_):
    for elem in list_:
        if elem % 2 == 0:
            yield elem
            
list_ = [i for i in range(100)]
list_even = []

for j in find_even(list_):
    list_even.append(j)

print(list_even)

# count the number of a word in a string
def find_word(test_string, word_):
    for word in test_string:
        if word == "word_":
            yield word
            
test_string = """
There are many geeks around you,\n
geeks arey known for teaching other geeks
"""
            
count = 0
for count_ in find_word(test_string.lower().split(), "geeks"):
    count += 1

print("The number of 'geeks' in the statement is %d" % count)