# Decorative menu for Python Pizza Deliveries
def pizza_delivery():
    print("           THE ULTIMATE PYTHON PIZZA DELIVERIES ")
    print("SMALL PIZZA (S): $15\nMEDIUM PIZZA (M): $20\nLARGE PIZZA (L): $25")
    print("\n-->> Additionals <<-- ")
    print("1) Pepperoni for small pizza: +$2\nPepperoni for medium or large pizza: +$3")
    print("2) EXTRA CHEESE: +$1")

    # Code for conditional statements
    bill = 0
    print("\nWelcome to Python Pizza Deliveries!\n")
    size = input("What size pizza do you want? S, M, or L: ").upper()

    if size == "S":
        bill += 15
        pepperoni = input("Do you want pepperoni on your pizza? (Y or N): ").upper()
        if pepperoni == "Y":
            bill += 2
        ex_cheese = input("Do you want extra cheese? (Y or N): ").upper()
        if ex_cheese == "Y":
            bill += 1

    elif size == "M":
        bill += 20
        pepperoni = input("Do you want pepperoni on your pizza? (Y or N): ").upper()
        if pepperoni == "Y":
            bill += 3
        ex_cheese = input("Do you want extra cheese? (Y or N): ").upper()
        if ex_cheese == "Y":
            bill += 1

    elif size == "L":
        bill += 25
        pepperoni = input("Do you want pepperoni on your pizza? (Y or N): ").upper()
        if pepperoni == "Y":
            bill += 3
        ex_cheese = input("Do you want extra cheese? (Y or N): ").upper()
        if ex_cheese == "Y":
            bill += 1

    else:
        print("Invalid size selected!")

    print(f"Your final bill is: ${bill}")
    print("\nEnjoy your pizza!\n")


# Treasure Island Game
def treasure_island_game():
    print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_ 
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_ 
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_______/
*******************************************************************************''')
    print("  Welcome To Treasure Island  ")
    print("Your mission is to find the treasure ")

    left_or_right = input("Choose (left or right):\n").lower()
    if left_or_right == "right":
        print("Ohk! You chose the right path.")
        key_or_pese = input("Choose (key or $10):\n").lower()
        if key_or_pese == "key":
            print("Crazy!!")
            wait_or_swim = input("Choose (wait or swim):\n").lower()
            if wait_or_swim == "wait":
                print("$$ You are playing well $$")
                print("Choose a color to find GOLD!!")
                red_yel_bl = input("red, yellow, blue):\n").lower()
                if red_yel_bl == "red":
                    print("Burned by fire.. Game Over!!")
                elif red_yel_bl == "yellow":
                    print("Yaahh! You Win the Ultimate Treasure of GOLD!")
                elif red_yel_bl == "blue":
                    print("Eaten by beasts.. Game Over!!")
                else:
                    print("DANGER AHEAD! You chose the wrong path!")
            else:
                print("Eaten By Crocodile!!\nGAME OVER!!")
        else:
            print("You got $10 but no treasure.\nGame Over!")
    else:
        print("Ohk! You chose the left path.")
        key_or_pese = input("Choose (key or $10):\n").lower()
        if key_or_pese == "key":
            print("Crazy!!")
            wait_or_swim = input("Choose (wait or swim):\n").lower()
            if wait_or_swim == "wait":
                print("$$ You are playing well $$")
                print("Choose a color to find GOLD!!")
                red_yel_bl = input("red, yellow, blue):\n").lower()
                if red_yel_bl == "red":
                    print("Burned by fire.. Game Over!!")
                elif red_yel_bl == "yellow":
                    print("Yaahh! You Win the Ultimate Treasure of GOLD!")
                elif red_yel_bl == "blue":
                    print("Eaten by beasts.. Game Over!!")
                else:
                    print("DANGER AHEAD! You chose the wrong path!")
            else:
                print("Eaten By Crocodile!!\nGAME OVER!!")
        else:
            print("You got $10 but no treasure.\nGame Over!")


# Main program
print("Welcome! First, you can order your pizza. Then, enjoy the Treasure Island game for fun!\n")
pizza_delivery()

play_game = input("\nDo you want to play the Treasure Island game? (Y or N): ").upper()
if play_game == "Y":
    treasure_island_game()
else:
    print("Thank you for visiting! Have a great day!")
