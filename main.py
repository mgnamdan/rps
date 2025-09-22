from random import randint

# 1. Turn on the application -> X
# 2. Ask if user wants to play -> X
# 3. If they don't want to play, shut off application -> X

# 4. If they do want to play, asking what move they want -> X
# 5. Decide computer's move -> X
# 6. Handle winner -> X
# 7. Repeat steps 2-7 -> X

def decideWinner(pChoice, cChoice):
    if (pChoice == "rock"):
        if (cChoice == "rock"):
            print("You tied!")
        elif (cChoice == "paper"):
            print("You lose!")
        else:
            print("You win!")

    elif (pChoice == "paper"):
        if (cChoice == "rock"):
            print("You win!")
        elif (cChoice == "paper"):
            print("You tie!")
        else:
            print("You lose!")

    elif (pChoice == "scissors"):
        if (cChoice == "rock"):
            print("You lose!")
        elif (cChoice == "paper"):
            print("You win!")
        else:
            print("You tie!")

    else:
        print("Invalid choice! Try again!")


def main():
    gameOn = True

    choices = {1: "rock",
               2: "paper",
               3: "scissors"}

    while gameOn:
        play = input("Would you like to play rock, paper, scissors? (y/n): ").lower()

        if (play == "n" or play == "no"):
            gameOn = False
        else: 
            playerChoice = input("Choose a move (rock/paper/scissors): ").lower()
            computerChoice = choices[randint(1, 3)]

            print(f"Your choice was: {playerChoice}")
            print(f"The computer's choice was: {computerChoice}")

            decideWinner(playerChoice, computerChoice)





main()
