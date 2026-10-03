User = input("Input your name: ")
Age = input('Input your age: ')
if int(Age) >= 12:
    print("Hello " + User + f", age {Age}. Select from the commands below.\n")

command = ''
while command != 'lopeta':
    if int(Age) < 12:
        print("You're underage. Shutting down program.")
        exit()
    print("Commands:\nlopeta: Shuts down program\nsum: Calculate sum of numbers\nname: Change your name\nage: Change your age")
    command = input()
    if command == 'sum':
        print("Input numbers divided by a space to get their sum.")
        text = input()
        numbers = text.split()
        sum = 0
        print("Total sum of ", end='')
        for n in numbers:
            sum += int(n)
            print(n, end=' ')
            if n != numbers[len(numbers) - 1]:
                print("+", end=' ')
        print(f"= {sum}\n")
    if command == 'name':
        User = input("Input your name: ")
        print(f"Name set to {User}.\n")
    if command == 'age':
        Age = input("Input your age: ")
        print(f"Age set to {Age}.\n")
        