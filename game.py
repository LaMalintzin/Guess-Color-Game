import random

print("Start....")

# Constant varibles 
COLORS = {"R", "G", "B", "Y", "W", "O"}
TRIES = 10
CODE_LENGTH = 4

print("Method 1")
# Creating a method which generates the code
def generate_code():
    #List containing 4 elements
    code = []
    # Insert four random colors into the list, where CODE_LENGTH = 4 iterations 
    for _ in range(CODE_LENGTH):
        color = random.choice(list(COLORS))
        code.append(color)
    # code = generate_code()
    return code

print("Method 2")
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

print("Method 3")
#Function which is going to check if the guessed color matches the real color
def check_code(guess, real_code):
    #Creates a dictionary to store the colors
    color_counts = {}
    #Varibles keeping track of colors in the correct position and incorrect position
    correct_pos = 0
    incorrect_pos = 0

    for color in real_code:
        if color not in color_counts:
            color_counts[color] = 0
        color_counts[color] += 1

    #Find the colors which are in the correct position
    for i, (guess_color, real_color) in enumerate(zip(guess, real_code)):
        if guess_color == real_color:
            correct_pos += 1 
            color_counts[real_color] -= 1


    for guess_color in guess:
        if guess_color in color_counts and color_counts[guess_color] > 0:
            incorrect_pos += 1
            color_counts[guess_color] -= 1

    return correct_pos, incorrect_pos

print("Start game method")
#Three main components are done, now we are going to link them together
def game():
    print(f"Welcome to mastermind, you have {TRIES} to guess the code...")
    print("The valid colors are", *COLORS)  

    code = generate_code()
    for attempts in range(1, TRIES + 1):
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess, code)

        if correct_pos == CODE_LENGTH:
            print(f"You guessed the code in {attempts} tries!!")
            break

        print(f"Correct position: {correct_pos} | Incorrect position: {incorrect_pos} ")

    else:
        print("You ran out of tries, the code was: ", *code)


if __name__ == "__main__":
    game()