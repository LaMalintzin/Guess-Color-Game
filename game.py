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







