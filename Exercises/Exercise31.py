print("""
      You enter a dark room with two doors.
      Do you go through door #1 or door #2?
      """)

door = input("Input either 1 or 2 >>> ")

if door == "1":
    print("""
          There's a giant bear here eating a cheese cake.
          What do you do?
          1: Take the cake.
          2: Scream at the bear.
          3: Tame the bear by controlling its mind. This is difficult so be careful.
          """)
    
    bear = input("Enter either 1 or 2 >>> ")
    
    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":   
        print("The bear eats your leg off. Good job!")
    elif bear == "3":
        print("""
              The outcome depends on your capability.
              What do you see?
              """)

        vision = input("Enter what you are seeing >>> ")

        if vision == "cheese cake" or vision == "cake":
            print("Congratulations. You have tamed the bear. It has become your pet.")
        elif vision == "myself":
            print("""
                  WOW! You have managed to control the bear to look at you.
                  You're a fast learner. You have so much potential.
                  """)
        elif vision == "bear":
            print("Good luck! You are inside the bear's stomach.")
        else:
            print("Bye world!")      
    else:
        print("""
              Well, doing %s is probably better.
              Bear runs away.
              """ % bear)
elif door == "2":
    print("""
          You stare into the endless abyss at the Cthuhlu's retina.
          1. Blueberries.
          2. Yellow jacket clothespins.
          3. Understanding revolvers yelling melodies.
          """)
    insanity = input("Enter either 1, 2 or 3 >>> ")
    
    if insanity == "1" or insanity == "2":
        print("""
              Your body survives powered by a mind of a jello.
              Good job.
              """)
    else:
        print("""
              The insanity rots your eyes into a pool of muck.
              Good job!
              """)
else:
    print("""
          You stumble around and fall on a knife and die.
          God job!
          """)    