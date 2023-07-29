def cheese_and_crackers(*args):
    cheese_count, boxes_of_crackers = args
    print("""
        You have %r cheeses.
        You have %r boxes of crackers.
        Man that's enough for a party.
        Get a blanker.
          """ % (cheese_count, boxes_of_crackers))


print("We can just give the function numbers directly.")
cheese_and_crackers(20, 30)

print("OR, we can use variables from our script:")
cheeses = 10
crackers = 50
cheese_and_crackers(cheeses, crackers)

print("We can combine the two, variables and math:")
cheese_and_crackers(cheeses+10, crackers+10)