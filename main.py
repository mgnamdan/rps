# 1. Turn on the application -> X
# 2. Ask if user wants to play -> X
# 3. If they don't want to play, shut off application -> X
# 4. If they do want to play, asking what move they want
# 5. Decide computer's move
# 6. Handle winner
# 7. Repeat steps 2-7

def main():
    gameOn = True

    while gameOn:
        play = input("Would you like to play rock, paper, scissors? (y/n): ").lower()

        if (play == "n" or play == "no"):
            gameOn = False
        else: 
            pass




main()
