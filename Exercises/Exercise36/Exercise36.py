import pandas as pd

def extract_and_compile(filename):
    vocab = dict()
    """ _summary_:

        _description_:
            This function extracts and compile vocabulary list.
            
        _args_:
            filename (_type_) : (_csv_)
    """
    
    country_list = pd.read_csv(filename)
    
    countries = country_list["Country"]
    capitals = country_list["Capital"]
    
    country_and_capital = {}
    
    for i in range(len(country_list)): 
        country_and_capital[countries[i]] = capitals[i]
                
    
    return country_and_capital
  
def end_game(decision):
    """_summary_

    _description_:
        Allows the user to end the game.
        
    _args_:
        decision (_type_): decision of the user (_string_)
    """
    
    #if decision.lower() == "end":
    print(decision)
    exit(0) 

def play_game(country_and_capital):
    countries = list(country_and_capital.keys())
    
    for i in range(len(country_and_capital)):
        country = countries[i]
        print("\nWhat is the capital of %s?\n" % country)
        ans = input('> ')
        
        if country_and_capital[country].lower() != ans.lower():
            end_game("""
                     Your answer is wrong.
                     The capital of %s is %s.
                     """ % (country, country_and_capital[country]))
    
    print("Congratulations! You have memorised all the capital of each country.")
            
        
def start_game(filename):
    """ _summary_

        _args_:
            filename: _csv_ file containing the countries and capitals
          
        _run_:      
        >>> start_game(filename)
    """
    
    print("""
          \nThis game is a mini flash card game which asks you
          for the capital of the country. If your answer is
          wrong, the game will end automatically. Good luck!\n
          """)
    
    country_and_capital = extract_and_compile(filename)
    play_game(country_and_capital)