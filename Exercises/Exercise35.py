from sys import exit

def gold_room():
    """_summary_:
    
       _args_:
            empty (_none_)
    """
    
    print("This room is full of gold. How much do you take?")
    
    next = input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")
    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")

def bear_room():
    print("""
          There is a bear here.
          The bear has a bunch of honey.
          The fat bear is in front of another door.
          How are you going to move the bear?
          """)
    bear_moved = False
    
    while True:
        next = input("> ")
        
        if next == "take honey":
            dead("The bear looks at you then slaps your face off.")  
        elif next == "taunt bear" and not bear_moved:
            print("The bear has moved from the door. You can go through it now.")
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")
            

def cthulu_room():
    print("""
          Here you see the great evil Cthulu.
          He, it, whatever stares at you and you go insane.
          Do you flee for your life or eat your head?
          """)

    next = input("> ")
    
    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulu_room

def dead(why):
    """_summary_

    _description_:
        This function provides the reason on why the player dies.
    
    _args_
        why (_type_): reason (_str_)
    """
    print(why, "Good job!")
    exit(0)
    
def start():
    """ _summary_:
    
        _description_:
            Begins the game with two doors.
    """
    
    print("""
          You are in a dark room.
          There is a door to your right and left.
          Which one do you take?
          """)
    
    next = input("> ")
    
    if next == "left":
        bear_room()
    elif next == "right":
        cthulu_room()
    else:
        dead("You stumble around the room until you starve.")
        
start()