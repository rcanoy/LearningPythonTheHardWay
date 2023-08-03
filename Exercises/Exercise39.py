ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Because the number of elements is less than 10, we'll add more")

ten_things = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(ten_things) != 10:
    added_stuff = more_stuff.pop()
    print("Adding: %s" % added_stuff)
    ten_things.append(added_stuff)
    print("There are now %d items." % len(ten_things))

print("The ten items are: ", ten_things)
print(' '.join(ten_things))

    