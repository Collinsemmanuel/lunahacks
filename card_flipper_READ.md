Memory Matching Game
This is a simple implementation of a memory matching game in Python. The game is played by flipping over two cards at a time to reveal their value. If the two cards match, they remain face up, and the player earns a point. If the two cards do not match, they are flipped face down again. The game ends when all cards have been matched.

Usage
To play the game, simply run the Python script memory_game.py. The game will start and prompt you to enter the indices of two cards to flip. Enter the indices separated by a space (e.g. "1 3") and press enter. The script will display the current state of the board and indicate whether the selected cards match or not.

Implementation Details
The game is implemented using a list of cards that are duplicated to create a matching pair. The cards are shuffled using the random module, and the game state is represented using another list of the same length as the cards list. The play_turn function handles the logic for each turn of the game, and the while loop in the main block controls the flow of the game until it ends.
