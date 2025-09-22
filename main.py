from random import randint
from rock import Rock
from paper import Paper
from scissors import Scissors

# 1. Turn on the application -> X
# 2. Ask if user wants to play -> X
# 3. If they don't want to play, shut off application -> X

# 4. If they do want to play, asking what move they want -> X
# 5. Decide computer's move -> X
# 6. Handle winner -> X
# 7. Repeat steps 2-7 -> X

def decideWinner(pChoice, cChoice):
    win = pChoice.winTable[str(cChoice)]
    if win == 1:
        print("You win!")
    elif win == -1:
        print("You lose!")
    else:
        print("Tie game!")


def main():
    gameOn = True

    choices = {1: Rock(),
               2: Paper(),
               3: Scissors()}

    while gameOn:
        play = input("Would you like to play rock, paper, scissors? (y/n): ").lower()

        if (play == "n" or play == "no"):
            gameOn = False
        else: 
            playerChoice = input("Choose a move (rock/paper/scissors): ").lower()
            if playerChoice == "rock":
                pMove = Rock()
            elif playerChoice == "paper":
                pMove = Paper()
            elif playerChoice == "scissors":
                pMove = Scissors()
            else:
                print("Invalid choice!")
                continue
            computerChoice = choices[randint(1, 3)]

            print(f"Your choice was: {pMove}")
            print(f"The computer's choice was: {computerChoice}")

            decideWinner(pMove, computerChoice)





main()
