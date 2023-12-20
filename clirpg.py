# Build a CLI RPG game following the instructions from the course.

# Ask the player for their name.
name = input("Please let us know your name: ")

# Display a message that greets them and introduces them to the game world.
print(f"Welcome {name} to this world of games!")

sword = "L"

while True: 
    # Present them with a choice between two doors.
    door = input("Two doors are before you. Do you choose the left door (L) or the right door (R)?: ")
    # If they choose the left door, they'll see an empty room.
    if door == "L":
        ex_ba = input("You entered what appears as an empty room. Do you wish to stay and explore (E) or go back (B): ")
        if ex_ba == 'E':
            sword = input("You've found a sword, do you take (T) it or leave (L) it: ")
            if sword == "T":
                print("You feel the weigh of the this old artifact in your hands. It's touch banishes your fears and something begins to stir within you as you leave the room.")
            elif sword == "L":
                print("You've left the sword, but as you do so, you begin to doubt")
        elif ex_ba == 'B':
            print("You exit the room. It can be explored some other time.")


    # If they choose the right door, then they encounter a dragon.
    elif door == "R":
        fight = input("You've come across a slumbering dragon. Do you wish to stay and fight (F) or go back (B): ")
        if fight == "F" and sword == "T":
            again = input("""Before the dragon can has a chance to react, you leap towards its throat, severing its head from its body and killing it then and there!
            cogratulations you've ecaped the game world.
            Do yo wish to try again. Yes(Y) or no(N)?""")
            if again == "Y":
                continue
            else:
                break
        elif fight == "F" and sword == "L":
            again = input("You've chosen to take on this beast with your bare hands. You try to aproach the dragon stealthly though i hears you and\n"
            "in an instance it turns you into charcoal. Better luck next time.\n"
            "Do yo wish to try again. Yes(Y) or no(N)?")
            if again == "Y":
                continue
            else:
                break
        else:
            print("You leave the room.")
            


 
# In both cases, they have the option to return to the previous room or interact further.

# When in the seemingly empty room, they can choose to look around. If they do so, they will find a sword. They can choose to take it or leave it.

# When encountering the dragon, they have the choice to fight it.

# If they have the sword from the other room, then they will be able to defeat it and win the game.

# If they don't have the sword, then they will be eaten by the dragon and lose the game.
