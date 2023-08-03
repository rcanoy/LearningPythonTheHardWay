def break_words(stuff, sep=' '):
    """ _summary_
    
    _description_:
        Splits words int different elements.
    
    _args_:  
        stuff (_type_): _str_
        sep (_type_): _str
    
    Notes:
        str.split('') does not accept an empty seperator.
    """
    words = stuff.split(sep)
    return words

def sort_words(words):
    """ _summary_
    
    _description_:
        Sorts a list.
    
    _args_:
        words (_type_) : _list_
    """
    return sorted(words)

def print_first_word(words):
    """_summary_
    
    _description_:
        Prints the first element of a list.
    
    _args_:
        words (_type_): _list_
    """
    return words.pop(0)

def print_last_word(words):
    """ _summary_
    
    _description_:
        Prints the last element of a list
        
    _args_:
        words (_type_) : _list_
    """
    
    return words.pop(-1)

def sort_sentence(sentence):
    """_summary_
    
    _description_:
        Takes a full sentencee and returns the sorted words.
        
    _args_:
        sentence (_type_) = _str_
    """
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """_summary_
    
    _desciption_:
        Prints the first and last elements in a sentence.
    
    _args_:
        sentence (_type_) : _str_
    """
    #words = break_words(sentence)
    words_sorted = sort_sentence(sentence.lower())
    return print_first_word(words_sorted), print_last_word(words_sorted)


    