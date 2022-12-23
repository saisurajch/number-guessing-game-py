import random

numbers = []
#making numbers list with 1 to 100
for i in range(0,101):
    numbers.append(i)
def game():
    print("Welcome to number guessing game !")
    #choosing a number by random
    computer_pick = random.choice(numbers)
    #asking user to choose
    difficulty_level = input("Choose your difficulty level.... easy or hard : ")
    if (difficulty_level == 'easy'):
        print("You have 10 attempts to guess the number")
        i = 0
        loop = True
        while loop == True:
            user_guess = int(input("Make a guess : "))
            if(user_guess > computer_pick):
                print("Wrong Guess")
                print("Your guess is higher than the original number")
            elif(user_guess < computer_pick):
                print("Wrong Guess")
                print("Your guess is lower than the original number")
            elif (user_guess == computer_pick):
                print("Your guess is correct...! You won the game")
                break
            i = i + 1
            if (i == 10):
                print("Your are out of turns. You lost the game")
                loop = False
    elif (difficulty_level == 'hard'):
        print("You have 5 attempts to guess the number")
        i = 0
        loop = True
        while loop == True:
            user_guess = int(input("Make a guess : "))
            if (user_guess > computer_pick):
                print("Wrong Guess")
                print("Your guess is higher than the original number")
            elif (user_guess < computer_pick):
                print("Wrong Guess")
                print("Your guess is lower than the original number")
            elif (user_guess == computer_pick):
                print("Your guess is correct...! You won the game")
                break
            i = i + 1
            if (i == 5):
                print("Your are out of turns. You lost the game")
                loop = False
    play_again = input("Do you want to play the game again: Type 'y' for yes and 'n' for exit")
    if play_again == 'y':
        game()
    else:
        print("Thanks For Playing The Game...!")
game()
