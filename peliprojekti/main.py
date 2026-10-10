import os

User = input("Input your name: ")
Age = input('Input your age: ')
ageCheck = 1
AwesomeList = []

def clear(): 
    os.system("cls")

if int(Age) >= 12:
    print("Hello " + User + f", age {Age}. Select from the commands below.")
def Sum(): #Function for calculating sum of numbers
    print("Input numbers divided by a space to get their sum.")
    text = input()
    numbers = text.split()
    sum = 0
    numOfLoops = 0
    print("Total sum of ", end='')
    for n in numbers:
        sum += int(n)
        numOfLoops += 1
        print(n, end=' ')
        if numOfLoops != len(numbers):
            print("+", end=' ')
    print(f"= {sum}")
    
def chgeName(): #Function for changing user's name
    User = input("Input your name: ")
    print(f"Name set to {User}.")
    return User

def chgeAge(): #Function for changing user's age
    Age = input("Input your age: ")
    print(f"Age set to {Age}.")
    return Age  

def newObject():
    print("Type your favourite object to add to the Awesome List:")
    obj = input()
    print(f"{obj} added to the list.")
    return str(obj)

def printList(coolList):
    print("\nThe Awesome list includes: ")
    numOfLoops = 0
    for n in coolList:
        numOfLoops += 1
        print(f"{numOfLoops}. {n}")

def gameIntro():
    try:
        with open("intro.txt", "r") as intro:
            introTxt = intro.read()
            print(introTxt)
    except FileNotFoundError:
        print("intro not found")
    except IOError:
        print("Error occured while handling intro text")
    
command = ''
while command != 'lopeta': 
    if int(Age) < 12:
        #print("You're underage. Shutting down program.")
        #exit()
        if ageCheck == 1:
            print("You're underage. Only a selected number of commands available.")
        ageCheck = 0
        print(
            "\nCommands:" 
            "\nlopeta: Shuts down program." 
            "\nname: Change your name." 
            "\nage: Change your age." 
            "\ngame: Start Text Adventure Game"
        "\n")
    else:
        ageCheck = 1
        print(
            "\nCommands:" 
            "\nlopeta: Shuts down program." 
            "\nsum: Calculate sum of numbers." 
            "\nname: Change your name." 
            "\nage: Change your age." 
            "\nadd: Add an object to the Awesome List." 
            "\nprint: Print every object in the Awesome List."
            "\ngame: Start Text Adventure Game"
        "\n")
    command = input(">")
    if command == 'sum' and ageCheck == 1:
        Sum()
    if command == 'name':
        User = chgeName()
    if command == 'age':
        Age = chgeAge()
    if command == 'add' and ageCheck == 1:
        AwesomeList.append(newObject())
    if command == 'print' and ageCheck == 1:
        printList(AwesomeList)
    if command == 'game':
        while command != 'lopeta':
            clear()
            gameIntro()
            #print(
            #    "Commands:"
            #    "\nnew game: Start a new game from the very beginning."
            #    "\nload: Continue from a previous save file.\n"
            #    )
            inventory = []
            glass_shard = 0
            wooden_stool = 0
            islandMap = {
                "west lake": {
                    "item" : "metal scrap",
                    "rooms" : ["cliffs", "vines", "south roads"]
                },
                "cliffs" : {
                    "item" : "glass shard",
                    "rooms" : ["west lake", "north roads"],
                    "hint" : "It looks like you could almost get on top of these cliffs, but it's just beyond your reach.\n",
                    "usable" : {
                        "wooden stool" : ["With the stool down and could now jump on top from here!\n", 1]
                    }
                },
                "vines" : {
                    "rooms" : ["west lake", "north roads"],
                    "usable" : {
                        "glass shard" : ["You sliced a way open with the sharp piece of glass! You can now go through.\n", 1]
                    },
                    "unlockable" : "behind vines"
                },
                "behind vines" : {
                    "item" : "wooden stool",
                    "rooms" : ["vines"]
                },
                "north roads" : {
                    "rooms" : ["cliffs", "vines"]
                },
                "south roads" : {
                    "rooms" : ["west lake", "boulder", "east lake"]
                },
                "boulder" : {
                    "item" : "binoculars",
                    "rooms" : ["south roads"]
                },
                "east lake" : {
                    "rooms" : ["south roads"],
                    "hint" : "There's something at the distant, but you can't quite make it out.\n",
                    "usable" : {
                        "binoculars" : ["There's a stool behind some vines in the distance! Maybe you can figure out a way to get past the vines.\n", "There's a stool behind the recently cut vines. Did you really return here to admire your work from afar?\n","There's not a stool behind some vines in the distance. It also looks like some of the vines got shorter.\n"]
                    }
                }
            }
            currentRoom = "west lake"
            action = ''
            hint = ''
            itemUsed = ''
            def error(reason):
                if reason == "g-item":
                    print("There is no such item.")
                elif reason == "command":
                    print("That move isn't in your arsenal.")
                elif reason == "useless":
                    print(f"The {command[1]} doesn't seem too useful here.")
                elif reason == "wrong-item":
                    print(f"You searched for the {command[1]} but you couldn't find such a thing.")
                elif reason == "parameter":
                    print(f"'{command[0]}' requires a parameter divided by a space")
                elif reason == "go":
                    print(f"you tried to '{command[0]}', but didn't know where.")
                else:
                    print("Invalid move!")
            def status(action = '',hint = '', item_used = '', item_spotted = ''):
                print(
f'''{action}{hint}{item_used}{item_spotted}---------------------
Currently in: {currentRoom}
Inventory: {inventory}
---------------------
commands:
go {roomInfo["rooms"]}
get ["item name"]
use ["item name"]
---------------------
''')
            class Player:
                def __init__(self, name, currentRoom, items):
                    self.name = name
                    self.currentRoom = currentRoom
                    self.items = items
            while True:
                roomInfo = islandMap[currentRoom]
                if "hint" in roomInfo:
                    hint = roomInfo["hint"]
                else :
                    hint = ''
                if "item" in roomInfo:
                    itemSpotted = f"You see {roomInfo['item']} littered on the ground.\n"
                else :
                    itemSpotted = ''
                status(action, hint, itemUsed, itemSpotted) #Prints the status message with each loop with actions and special messages as parameters
                action = ''

                command = input('>')
                clear()
                command = command.split(" ", 1)
                try :
                    if command[0] == "go": #Checks the player's commands and acts accoringly
                            check = 0
                            for n in roomInfo["rooms"]:
                                if command[1] == n:
                                    currentRoom = command[1]
                                    action = f"You walked to the {currentRoom}.\n"
                                    check = 1
                            if check == 0:
                                error("go")
                    elif command[0] == "get" and command[1] != '':
                        try :
                            if command[1] == roomInfo["item"]:
                                inventory.append(command[1])
                                del islandMap[currentRoom]["item"]
                                action = f"You got the {command[1]}!\n"
                            else :
                                error()
                        except :
                            error("g-item")
                    elif command[0] == "use" :
                            if command[1] in inventory:
                                try :
                                    if command[1] in roomInfo["usable"] :
                                        itemUsed = roomInfo["usable"][command[1]][0]
                                        if "hint" in roomInfo:
                                            del islandMap[currentRoom]["hint"]
                                        if "unlockable" in roomInfo:
                                            islandMap[currentRoom]["rooms"].append(roomInfo["unlockable"])
                                            del islandMap[currentRoom["unlockable"]]
                                        action = f"You used the {command[1]}!\n"
                                        continue
                                except :
                                    error("useless")
                            else :
                                error("wrong-item")
                    else:
                        error("command")
                    itemUsed = ''
                except :
                    error('parameter')