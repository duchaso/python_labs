import random

colors = ["blue", "white", "yellow", "green", "black"]
random_color = random.choice(colors)
hint_list = ['_']*6

def hint(used_letters):
    random_letter = random.choice(random_color)
    while(random_letter in used_letters):
        random_letter = random.choice(random_color)
    n_letter = random_color.find(random_letter)
    hint_list[n_letter] = random_letter
    print(" ".join(hint_list))
    return random_letter


for color in colors:
    print(color, end=' ')
print()
usr_choice = input("Guess color: ")

used_letters = []
correct = False
while not correct:
    if usr_choice == random_color:
        print("Well done!")
        correct = True
    else:
        print("Wrong. Take a hint and try again")
        used_letters.append(hint(used_letters))
        usr_choice = input("Guess color: ")