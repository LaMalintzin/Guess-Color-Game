import random

# Constant varibles 
COLORS = {"R", "G", "B", "Y", "W", "O"}
TRIES = 10
CODE_LENGTH = 4

# Creating a method which generates the code
def generate_code():
    #List containing 4 elements
    code = []
    # Insert four random colors into the list, where CODE_LENGTH = 4 iterations 
    for _ in range(CODE_LENGTH):
        color = random.choice(COLORS)
        code.append(color)
    # code = generate_code()
    return code

# Function which allow the user to guess the colors
def guess_code():
    #.split(" ") does removing spaces in a string and putting them in a list eg. "G G G G" -> ["G", "G", "G", "G"]
    while True:
        guess = input("Guess: ").upper().split(" ")

        if len(guess) != CODE_LENGTH:
            print(f"You need to guess {CODE_LENGTH} colors.")
            continue

        #Check for colors in the colors list
        for color in guess:
            if color not in COLORS:
                print(f"Invalid color: {color}. Try again")
                break
        # Just to check if you broke out of the for loop
        else:
            break
    
    return guess





