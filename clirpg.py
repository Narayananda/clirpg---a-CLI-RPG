# Build a CLI RPG game following the instructions from the course.
import random


inventory = []                                              # Create an inventory for your player, where they can add and remove items.
attributes = {"attack":1,"defence":1,"speed":1,"intuition":1}
player_health = 5

# name = input("Please let us know your name: ")              # Ask the player for their name.


# print(f"Welcome {name} to this world of games!")            # Display a message that greets them and introduces them to the game world.

dragon_power = 8
sorcerer_power = 7
soldier_power = 6
beast_power = 5


ok_input = set(["y","n"])                    # Save the user input options you allow e.g. in a set that you can check against when your user makes a choice.








def fights(attributes:dict,opponent_power:int):                       # Implement some logic that decides whether or not your player can beat the opponent depending on what items they have in their inventory
    player_power=sum(attributes.values())
    if player_power>= opponent_power:
        dif = (player_power+1)-opponent_power
        dice_roll = random.randint(dif,6)                            # difference in strength betweeen the player and opponant. the stronger you are, the greater the chance of winning
        print("To beat your opponent you must roll higher than 3 with the dice")
        if dice_roll > 3:                       # Use the random module to add a multiplier to your battles, similar to a dice roll in a real game. This pseudo-random element can have an effect on whether your player wins or loses when battling an opponent.
            outcome = "win"
            print(f"You rolled {dice_roll}!")
        else:
            outcome = "lose"
            print(f"You rolled {dice_roll}...\n")
    else:
        outcome = "lose"
        print("Your power doesnt compare to your opponents")
        player_health = 0
        return player_health, outcome
    
    return outcome


def encounter(opponent:str,opponent_power:int,attributes:dict,item:str,inventory:list,player_health:int):
    print("\nFIGHTING\n")
    print(f"Player's power level: {sum(attributes.values())}\n{opponent}'s power level: {opponent_power}")
    player_health_temp = player_health
    for i in range(player_health_temp):
        outcome = fights(attributes,opponent_power)
        if outcome == "win":
            pick_up = input(f"You defeated the {opponent}.\nRemaining health = {player_health}. Do you take the {opponent}'s {item} (y/n): ")
            if pick_up == "y":
                pick_up_item(item,attributes, inventory)
                print(f"You have equiped the {item}\n{attributes}\n")  
            else:
                print(f"you left the {item} behind\n")
            return attributes, inventory, player_health
        elif outcome == "lose":
            print(f"You fought the {opponent} but the {opponent} is not defeated")
            player_health -= 1
            print(f"Remaining health = {player_health}")
        else:
            break
    print("You have been defeated and blackout\n")
    return "lose"


def pick_up_item(item:str,attributes:dict, inventory:list): # Players should be able to collect items they find in rooms and add them to their inventory.
    if item =="sword":
        inventory.append("sword")
        attributes["attack"] += 1
    elif item == "shield":
        inventory.append("shield")
        attributes["defence"] += 1
    elif item == "boots":
        inventory.append("Boots")
        attributes["speed"] += 1
    elif item == "amulet":
        inventory.append("amulet")
        attributes["intuition"] += 1
    elif item == "heart":
        inventory.append("dragon's heart")
        attributes["attack"] += 2

    return(attributes,inventory)











while True:                                                 # Present them with a choice between two doors.In both cases, they have the option to return to the previous room or interact further.
                                                            
    door = input("Two doors are before you. Do you choose the left door (y) or the right door (n)?: ")
    if door == "y":                                         # If they choose the left door, they'll see an empty room.


        #---------------------------------------------------Room 1 (empty room)--------------------------------------------------------
        ex_ba = input("You entered what appears as an empty room. Do you wish to stay and explore (y) or go back (n): ")
        if ex_ba == 'y':                                    # When in the seemingly empty room, they can choose to look around. If they do so, they will find a sword. They can choose to take it or leave it.
            sword = input("You've found a sword, do you take (y) it or leave (n) it: ")
            if sword == "y":
                pick_up_item("sword",attributes, inventory)
                print("You've added the sword to your inventory, you feel stronger as you leave the room.")
                print(attributes)
            elif sword == "n":
                print("You*ve left the sword behind")
            
            while True:
                rooms = input("As you explore the room further you discover another set of doors. Do you wish to enter the metal door (y) or the other made of wood(n): ")
            #---------------------------------------------------Room 2 (metal door)--------------------------------------------------------    
                if rooms == "y":
                    room2 = input("You encounter a soldier. Do you wish to fight (y) or go back (n): ")
                    if room2 == "y":
                        encounter("soldier",soldier_power,attributes,"shield",inventory,player_health)
                    else:
                        print("You go back")
                        break
            #---------------------------------------------------Room 3 (wooden door)------------------------------------------------------            
                else:
                    room3 = input("You encounter a beast. Do you wish to fight (y) or go back (n): ")
                    if room3 == "y":
                        encounter("beast",beast_power,attributes,"boots",inventory,player_health)
                    else:
                        print("you go back")
                        break
            
        elif ex_ba == 'n':
            print("You exit the room. It can be explored some other time.")


  #------------------------------------------------------------Room 4 (dragon)-------------------------------------------------------------
    elif door == "n":                                       # If they choose the right door, then they encounter a dragon. When encountering the dragon, they have the choice to fight it.
        choice = input("You've come across a slumbering dragon. Do you wish to stay and fight (y) or go back (n): ")
        if choice == "y":
            finale = encounter("dragon",dragon_power,attributes,"heart",inventory,player_health)                    # If they lose a fight against the dragon, then they should lose their inventory items.
            if finale != "lose":
                print("Congratulations you have obtained the dragon's heart and won")
                break
            else:
                inventory.clear()
                attributes = {"Attack":1,"Defence":1,"Speed":1,"intuition":1}
                continue

        else:
            print("You leave the room.")

            

 





# Add more rooms to your game and allow your player to explore.
# Some rooms can be empty, others can contain items, and yet others can contain an opponent.

#------------------------------------------------notes to self:-----------------------------------------------------------
#make it so that one you have defeated a monster or found an item, they disappear
#add the last room
#when the player blackout they should start from the beginning with empty inventory
#after a battle health should not return to 5, but remain how it was at the conclution of the battle



#