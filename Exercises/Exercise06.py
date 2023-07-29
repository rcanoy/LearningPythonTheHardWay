x = ("There are %d types of people." % 10)
binary = 'binary'
do_not = "don't"
y = "Those who know %r and those who %s." % (binary, do_not)

print(x)
print(y)

# %r: Can be anything
print("I said: %r." % x)
print("I just want to reiterate that I said: %s" % x)

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print(joke_evaluation % hilarious)