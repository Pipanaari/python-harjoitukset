User = input("Input your name: ")
Age = input('Input your age: ')
AwesomeList = []

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
    
command = ''
while command != 'lopeta': 
    if int(Age) < 12:
        print("You're underage. Shutting down program.")
        exit()
    print("\nCommands:\nlopeta: Shuts down program.\nsum: Calculate sum of numbers.\nname: Change your name.\nage: Change your age.\nadd: Add an object to the Awesome List.\nprint: Print every object in the Awesome List.")
    command = input()
    if command == 'sum':
        Sum()
    if command == 'name':
        User = chgeName()
    if command == 'age':
        Age = chgeAge()
    if command == 'add':
        AwesomeList.append(newObject())
    if command == 'print':
        printList(AwesomeList)
        