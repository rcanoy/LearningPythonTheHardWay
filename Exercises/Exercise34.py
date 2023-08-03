animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']

label = ['The animal at 1: ', 'The 3rd animal: ',
         'The 1st animal: ', 'The animal at 3: ', 
         'The 5th animal: ', "The animal at 2: ", 
         "The 6th animal: ", 'The animal at 4: ']
order = [1, 2, 0, 3, 4, 2, 5, 4]


print('animals: ', animals)

for i in range(0, len(order)):
    print('\n', label[i], animals[order[i]])