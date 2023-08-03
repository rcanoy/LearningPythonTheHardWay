people = 30
cars = 40
buses = 15

if people > cars:
    print("Great. Not too much traffic.")
elif people < cars:
    print("Some people may have more than one car.")
else:
    print("There is one car per person.")

if people > buses:
    print("There's not much any problem.")
elif people < buses:
    print("Not fine. It'll createy morey traffic and waste of oil resources.")
else:
    print("It defies the concept of public transportation.")

if cars > buses:
    print("""Cool! Possibly we're experiencing economic boom. 
          \nBut if few individuals have more cars, 
          \nthen the resources are monopolised by few individuals.""")
elif cars < buses:
    print("""People are now trusting the public transportation.
          \nWe can now protect our environment.""")
else:
    print("Some cars might be useless.")
    