from random import *

user_points=0  # initialize user points to 0
computer_points=0  # initialize computer points to 0
print("The first player to reach 5 points wins!")

while user_points!=5 and computer_points!=5: # while loop until either user or computer wins.
    user_choice = input("Enter your choice 'r' for Rock,'s' for Scissors or 'p' for Papers.(r/s/p): ")
    # user input to choose rock/paper/scissor
    computer_choice = choice(['r', 's', 'p']) # computer choice for rock/paper/scissor

    if user_choice==computer_choice: # if both choose same
        print("Its a tie! User has now",user_points,"points and computer has now",computer_points,"points.")

    elif (user_choice=='r' and computer_choice=='s')  or (user_choice=='p' and computer_choice=='r') or (user_choice=='s' and computer_choice=='p'):
        user_points += 1
        # if user wins
        print("User got it this time! User now has",user_points,"points.")

    elif (computer_choice=='r' and user_choice=='s')  or (computer_choice=='p' and user_choice=='r') or (computer_choice=='s' and user_choice=='p'):
        computer_points+=1
        # if computer wins
        print("Computer got it this time! Computer now has",computer_points,"points.")

if user_points==5: # if user wins the game
    print("User won the game!")

elif computer_points==5: # if computer wins the game
    print("Computer won the game!")

