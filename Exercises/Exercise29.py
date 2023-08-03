people = 50
cats = 30
dogs = 20

if people < cats:
    print("Too man cats! The world is doomed!")
elif people > cats:
    print("Not many cats! The world is saved!")
elif people < dogs:
    print("The world is drooled on!")
elif (people > dogs) and (people > cats):
    print("The world is dry!")

dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")
if people <= dogs:
    print("People are less than or equal to dogs.")
if people == dogs:
    print("People are dogs.")
