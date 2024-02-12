# Build a CLI RPG game following the instructions from the course.
import random
import requests
import pandas as pd






inventory = []                                              # Create an inventory for your player, where they can add and remove items.
attributes = {"attack":1,"defence":1,"speed":1,"intuition":1}
player_health = sum(attributes.values())

dragon_power = 8
sorcerer_power = 7
soldier_power = 6
beast_power = 5

player_info = { "inventory":[],
                "attributes":{"attack":1,"defence":1,"speed":1,"intuition":1},
                "player_health":5
    }

enemies = {"dragon":{"opponent":"dragon","power":8,"item":"heart"},
           "sorcerer":{"opponent":"sorcerer","power":7,"item":"amulet"},
           "soldier":{"opponent":"soldier","power":6,"item":"shield"},
           "beast":{"opponent":"beast","power":5,"item":"boots"}
    }


def choose_name():
    choice = input("choose a name (n) or generate a random one (y): ")

    if choice == 'y':
        min_len = 3
        max_len = 7
        URL = f"http://uzby.com/api.php?min={min_len}&max={max_len}"
        response = requests.get(URL)
        player_name = response.text
    
    else:
        player_name = input("Write your name: ")
    return player_name


def fights(attempt:int,attributes:dict,opponent_power:int,player_health:int,opponent_health:int):
    """Logic that decides whether or not the player beats the opponent depending on power level.
    The random module adds a multiplier to the battles, similar to a dice roll in a real game. This pseudo-random element has an effect on whether the player wins or loses the fight.
    The difference in power level betweeen the player and opponant influences the chance of winning

    Args
        attributes:     Determines the players power level
        opponent_power: Determines the opponents power level

    Return
        outcome: This determines the outcome of the fight
        """
    
    # print(f'\n------------- Attmept nr: {attempt} ---------------')
    player_power=sum(attributes.values())
    your_dice_roll = random.randint(0,player_power)
    opponent_dice_roll = random.randint(0,opponent_power)
    if your_dice_roll > opponent_dice_roll:                       
        outcome = "won"
        opponent_health -=1
    elif your_dice_roll == opponent_dice_roll:
        outcome = "draw"
        player_health-=1
        opponent_health -=1
    else:
        outcome = "lost"
        player_health-=1
    
    return outcome,your_dice_roll,opponent_dice_roll,player_health,opponent_health


def encounter(opponent:str,opponent_power:int,attributes:dict,item:str,inventory:list):
    """Logic that encompasses the ecounter with an opponent, including the fight fucntion and the items grained if opponent is defeated.
    
    Args:
        opponent:       opponents name
        opponent_power: oppenents power level
        attributes:     player power level
        item:           item accuired if player defeats opponent
        inventory:      player inventory
        player_health:  player health
    
    Return: 
        1. if player wins. OR 2. if player losses.

        1.
        attributes:     This will be updated according the item accuired
        inventory:      This will also be updated according the item accuired
        player_health:  This will be updated according to the number of attempts it takes for the player to defeat the opponent

        or
        
        2.
        "lose":         If the player losses this string will be the outcome

    """
    
    print(f"\n--------------------------------FIGHTING--------------------------------\nPlayer's power level: {sum(attributes.values())}\n{opponent}'s power level: {opponent_power}\n")
    
    player_health = sum(attributes.values())
    opponent_health = opponent_power
    max_rounds = player_health+opponent_power

    df = pd.DataFrame({'player dice roll': [],
                   f"{opponent}'s dice roll": [],
                   'player health': [],
                   f"{opponent}'s health": []})

    for i in range(max_rounds):
        
        attempt = i+1
        outcome = fights(attempt,attributes,opponent_power,player_health,opponent_health)       
    
        your_dice_roll = outcome[1]
        opponent_dice_roll = outcome[2]
        player_health = outcome[3]
        opponent_health = outcome[4]

        df.loc[len(df.index)] = [your_dice_roll, opponent_dice_roll, player_health,opponent_health] 
        if opponent_health == 0:
            break
        elif player_health ==0:
            break
    
    print(df)
    if opponent_health == 0:
        pick_up = input(f"You defeated the {opponent}.\nRemaining health = {player_health}. Do you take the {opponent}'s {item} (y/n): ")
        if pick_up == "y":
            pick_up_item(item,attributes, inventory)
            print(f"You have equiped the {item}\n{attributes}\n")  
        else:
            print(f"you left the {item} behind\n")
        return attributes, inventory, player_health

    elif player_health == 0:
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
        inventory.append("boots")
        attributes["speed"] += 1
    elif item == "amulet":
        inventory.append("amulet")
        attributes["intuition"] += 1
    elif item == "heart":
        inventory.append("dragon's heart")
        attributes["attack"] += 2

    return(attributes,inventory)




print('\n---------------WELCOME TO THIS CLIRPG---------------')
player_name = ''
accept = 'n'
while accept != 'y':
    player_name = choose_name()
    accept = input(f"Is {player_name} your name?(y/n): ")



while True:                                                 # Present them with a choice between two doors.In both cases, they have the option to return to the previous room or interact further.
                                                            
    door = input(f"Two doors are before you, {player_name}. Do you choose the left door (y) or the right door (n)?: ")
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
                        encounter("soldier",soldier_power,attributes,"shield",inventory)
                    else:
                        print("You go back")
                        break
            #---------------------------------------------------Room 3 (wooden door)------------------------------------------------------            
                else:
                    room3 = input("You encounter a beast. Do you wish to fight (y) or go back (n): ")
                    if room3 == "y":
                        encounter("beast",beast_power,attributes,"boots",inventory)
                    else:
                        print("you go back")
                        break
            
        elif ex_ba == 'n':
            print("You exit the room. It can be explored some other time.")


  #------------------------------------------------------------Room 4 (dragon)-------------------------------------------------------------
    elif door == "n":                                       # If they choose the right door, then they encounter a dragon. When encountering the dragon, they have the choice to fight it.
        choice = input("You've come across a slumbering dragon. Do you wish to stay and fight (y) or go back (n): ")
        if choice == "y":
            finale = encounter("dragon",dragon_power,attributes,"heart",inventory)                    # If they lose a fight against the dragon, then they should lose their inventory items.
            if finale != "lose":
                print("Congratulations you have obtained the dragon's heart and won")
                break
            else:
                print("You feel weaker")
                dragon_power+=1
                inventory.clear()
                attributes = {"attack":1,"defence":1,"speed":1,"intuition":1}
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


#------------------------------------------things that seems unneccecary---------------------------------------------------
# name = input("Please let us know your name: ")              # Ask the player for their name.
# print(f"Welcome {name} to this world of games!")            # Display a message that greets them and introduces them to the game world.
# ok_input = set(["y","n"])                    # Save the user input options you allow e.g. in a set that you can check against when your user makes a choice.
