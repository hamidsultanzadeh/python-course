import random as r
counter = 0
choice = int(input("Welcome ! I chose my number, your turn (1-100) : "))

comp = r.randint(1,100)

while True:

    if choice == comp:
        print("You Win!!! Congratulations. My number is",comp)
        print("Your try count :",counter)
        break
    elif choice > comp:
        print("Your number is higher")
    else:
        print("Your number is lower")

    counter += 1

    choice = int(input("Try again :"))