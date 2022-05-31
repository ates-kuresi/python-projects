import random


available = {"rock", "paper", "scissors"}
user_choice = input("\nSelect your item: rock, paper, scissors: \n")
comp_choice = random.choice(tuple(available))
print("You've selected:", user_choice)
print("Comp selected:", comp_choice)


if user_choice == 'rock':
    if comp_choice == 'scissors':
        print("You Win.")
    elif comp_choice == 'paper':
        print("You Lose.")
    else:
        print("Tie Game.")


elif user_choice == 'paper':
    if comp_choice == 'scissors':
        print("You Lose.")
    elif comp_choice == 'rock':
        print("You Win.")
    else:
        print("Tie Game.")


elif user_choice == 'scissors':
    if comp_choice == 'paper':
        print("You Win.")
    elif comp_choice == 'rock':
        print("You Lose.")
    else:
        print("Tie Game.")
