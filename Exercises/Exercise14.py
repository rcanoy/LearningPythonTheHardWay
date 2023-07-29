## ======================================================================================================
#  Author: Raymart Jay E. Canoy
#  Date: 22 July 2023
## ======================================================================================================

from sys import argv

## (01) Initialization
script, user_name = argv
prompt = '> '
binary_options = ["y", "n"]
direc_question = "Where do you wanna go next?"
end_message = "Bye! Thanks for dropping by."
west_message = """
If you go further, you can see a fence on your left.
The bottom fence is made up of concrete while the top fence is made of square-based iron rods.
The iron rods are arranged perpendicular to each other, so you can see the outside through the fence.
On your right, you can see a wooden square window.
It's closed, so you cannot enter through the window.
Heading further, you can see the front door.
It's made up of wood and painted using color brown.
The door is not locked, so can enter by pushing the door. 
"""
welcome_message = """
Welcome! You have successfully entered the house.
You are welcomed by a white dog.
It smells like a stuffed toy.
Her name is Tala, which means star.
She likes to climb on our visitor.
So be careful. Your clothes might be stained.
Just don't mind the dog.
As you enter, you can see the door heading to the kitchen.
Before you go to the kitchen, go to the center.

Let's just call this space as the living room.
On your right, you can see the two square wooden windows.
On your left, you can see another wooden window.
Then, you can see a glass table.
On top of the table, you can see a televison.
I don't know it's dimension, so don't dare ask.
You can also see my laptop on the table.
It's color is silver.
There are also some books on the table.

When you turn left, you can see a refrigerator.
Just don't open it. It's stinky when it's turned off.
It's located between the front door and the square wooden window.

If you face again the door heading to the kitchen,
you can see a wooden stair heading to the second floor on the right.
Under the stair, you can find a black dog.
Her name is Luna, which means moon.
You can smell her if you want, but she stinks sometimes.
You're not allowed to climb the stairs.
I don't have time to explain it to you.

If you move your head upwards, you can see the base of the second floor.
It's made of wood. My father built that alone.
He might have basic engineering skills.
Who knows. I think it's built well.
You can ask him if you want.

Now, we have just finished the tour in our living room.
This time, I won't ask you where you wanna go.
I don't have time to do that.

On the right side of the door heading to the kitchen, you can find a sofa.
Please sit there for a while until further notice.
"""

## (02) Game
print("Hi %s! I'm the %s, your tour guide." % (user_name, "Raymart"))
print("""
    Welcome to Abode 1.0.
    Note: This game is based on Zork I.
    Purpose: This game is intended to provide you a tour of my simple abode.
    Would you like to continue with the tour?        
""")
start_response = input("Y/N: ")
start_response.lower()

if len(start_response) > 1:
    start_response = input("You can only input Y/N. %s" % end_message)
else:
    if start_response == "N":
        print("\n%s" % end_message)
    else:
        message = print(
            """
            You've decided to continue with the house tour.
            Make sure you won't regret your decision.

            You're currently in the front gate.
            The gate is made up of thin square-based iron rods.
            They are arranged parrallel to each other.
            You can see the inside through the space between them.
            The right side of the gate is a concrete fence.
            The gate is not locked, so you can enter by just pushing the gate.
            
            Directions: east, west, go straight, go back
            """
        )

        options = ["east", "west", "go straight", "go back"]

        print("After entering, %s?" % direc_question.lower())
        resp1 = input(prompt)

        # The option is not in the list or the user wants to go back
        if ((resp1 in options) == False) or (resp1 == options[3]):
            print("\n%s" % end_message)
        # The option[2]: going straight
        elif (resp1 == options[0]):
            print("\nYou're not using your head.")
            print("%s" % end_message)
        elif (resp1 == options[2]):
            # If you go straight, you need to go back
            print("""
                You can see two wooden square windows on your left.
                The windows are all closed.
                On your right, you can see a concrete fence.
                And if you go further, you can see one of the three doors.
                But the door is closed, so you cannot enter.
                """)
            print("Where do you wanna go next?")
            resp2 = input(prompt)
            # If you have chosen other directions, the tour will end
            if (resp2 == options[0]) or (resp2 == options[1]) or (resp2 == options[2]):
                print("""
                Opps! You're not using your head.
                Just go home by going back.
                %s
                """ % end_message) 
            # You have chosen to go back
            else:
                print("\nYou're back at the gate.")
                # Going back, means going home
                if ((resp2 in options) == False) or (resp1 == options[3]):
                    print("\n%s" % end_message)
                # There's a concrete fence on your right.
                elif (resp2 == options[0]):
                    print("""
                    You've chosen the wrong direction.
                    There's a fence here. You've not used your eyes. 
                    Head west!
                    """)
                # There's a 
                elif (resp2 == options[2]):
                    print("""
                    You've been there already. 
                    Why would you go back.
                    Just go home.
                    %s
                    """ % end_message)
                print("\nWhere do you wanna go next?")
                resp3 = input(prompt)
                if (resp3 == options[0]) and (resp3 == options[3]):
                    print("""
                    You're not thinking. Just go home.
                    Bye! Thanks for dropping by!
                    """)
                elif resp3 == options[2]:
                    print("""
                        You've been there already.
                        Why would you go back.
                        Just go home.
                        %s
                    """ % end_message)
                else:
                    print("%s" % west_message)
                    resp4 = input("Do you want to enter [Y/N]: ")
                    if ((resp4.lower() in binary_options) == False) and (resp4 == binary_options[1]):
                        print("Just follow your previous route. %s" % end_message)
                    else:
                        print("%s" % welcome_message)
        else:
            print("%s" % west_message)
            resp4 = input("Do you want to enter [Y/N]: ")
            if ((resp4.lower() in binary_options) == False) and (resp4 == binary_options[1]):
                print("Just follow your previous route. %s" % end_message)
            else:
                print("%s" % welcome_message)