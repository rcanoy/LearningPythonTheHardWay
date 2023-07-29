print("How old are you? (years)",)
age = input()
print("How tall are you? (cm)",)
height = input()
print("How much do you weigh (kg)?",)
weight = input()

print(
    """
    So, you're %r years old, %r tall and %r heavy.
    """ % (age, height, weight)
)