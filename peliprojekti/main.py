User = input("Input your name: ")
Age = input('Input your age: ')
if int(Age) < 12 :
    print("You're underage. Shutting down program.")
    exit()
else :
    print("Hello " + User + ". Type from the commands below:\nLopeta: Shuts down program.")

while input() != 'lopeta' :
    print("Kirjoita lopeta kun haluat lopettaa")