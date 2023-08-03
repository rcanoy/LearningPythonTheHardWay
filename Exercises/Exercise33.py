def generate_num(num_start, num_inc, num_end):
    """_summary_
    
    _description_:
        This function generates a number from num_start to num_end,
        with an increment of num_inc. This function uses while loop.
    
    _args_:
        num_start (_type_) : starting point (_int_ or _float)
        num_inc (_type_) : increment (_int or _float)
        num_end (_type_) : ending point (_int_ or _float)
    """
    
    # initialisation
    i = num_start
    numbers = []

    # generates numbers from num_start to num_end
    while i <= num_end:
        print("At the top is %d" % i)
        numbers.append(i)
        i += num_inc
        print("The number list now contains: ", numbers)
        print("At the bottom i is %d", i)
        
    #print("The numbers are:")
    #for num in numbers:
    #    print(num)
    

    return numbers

def generate_num_v2(num_start, num_inc, num_end):
    """_summary_
    
    _description_:
        This functions generates numbers from num_start to num_end,
        with an increment of num_inc. This function uses for loop.
        
    _args_:
        num_start (_type_) : starting point (_int_ or _float)
        num_inc (_type_) : increment (_int_ or _float)
        num_end (_type_) : ending point (_int_ or _float)
    """
    
    numbers = []
    
    for num in range(num_start, num_end+1, num_inc):
        numbers.append(num)
        
        
    return numbers