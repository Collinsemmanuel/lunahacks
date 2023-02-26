import random

# Define the cards
cards = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

# Duplicate the cards to create a matching pair
cards *= 2

# Shuffle the cards
random.shuffle(cards)

# Initialize the game state
board = ['*'] * len(cards)
matched = set()

# Define a function to print the current state of the board
def print_board():
    print(' '.join(board))

# Define a function to handle a player's turn
def play_turn():
    print_board()
    print("Enter the indices of two cards to flip: ")
    i, j = map(int, input().split())

    # Check if the selected cards are already matched or flipped
    if i == j or board[i] != '*' or board[j] != '*':
        print("Invalid selection.")
        return

    # Flip the cards over and reveal their value
    board[i] = cards[i]
    board[j] = cards[j]
    print_board()

    # Check if the cards match
    if cards[i] == cards[j]:
        print("Match!")
        matched.add(cards[i])
    else:
        print("No match.")

    # Check if the game is over
    if len(matched) == len(set(cards)):
        print("You win!")
        return True

# Play the game
while True:
    if play_turn():
        break
