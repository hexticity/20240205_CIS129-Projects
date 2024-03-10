import random

def roll_dice():
    return random.randint(1, 6)

def get_player_names():
    player1 = input("Enter player 1 name: ")
    player2 = input("Enter player 2 name: ")
    return player1, player2

def determine_winner(player1, player2, roll1, roll2):
    if roll1 == roll2:
        return "It's a tie!"
    elif roll1 > roll2:
        return player1 + " wins!"
    else:
        return player2 + " wins!"

def main():
    print("Welcome to the Dice Game!")
    player1, player2 = get_player_names()
    
    play_again = True
    while play_again:
        input("Press Enter to roll the dice...")
        roll1 = roll_dice()
        roll2 = roll_dice()
        
        print(player1, "rolled:", roll1)
        print(player2, "rolled:", roll2)
        
        print(determine_winner(player1, player2, roll1, roll2))
        
        play_again_input = input("Do you want to play again? (yes/no): ")
        play_again = play_again_input.lower() == "yes"

    print("Thanks for playing!")

if __name__ == "__main__":
    main()
