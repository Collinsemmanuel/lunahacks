def print_board(board):
  #outputs the tic-tac-toe table ranging from 1 to 9

  #These are used to form lines of the table of tic-tac-toe game
  print("-------------")
  for x in range(3):
    print("|", end="")
    for y in range(3):
      print(f" {board[x][y]} |", end="")
    print("\n-------------")


#the code gives the mark a player has used to replay the number he/she has choose that is X or 0
def check_win(board, mark):

  # Check rows to give the results if the player won if the 3 rows has the sigh(x or 0) he/she uses to play
  for x in range(3):
    if all(cell == mark for cell in board[x]):
      return True
  # Check columns to give the results if the player won if the 3 columns has the sigh(x or 0) he/she uses to play
  for y in range(3):
    if all(board[x][y] == mark for x in range(3)):
      return True
  # Check diagonals
  if all(board[x][x] == mark for x in range(3)):
    return True
  if all(board[x][2 - x] == mark for x in range(3)):
    return True
  return False


#play tic-tac-toe game now
def play_game():

  # Initialize table of tic-tac-toe game
  board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
  print_board(board)
  # Start game nooooow!!!!!!
  turn = 'X'
  while True:
    print(f"Player {turn}'s turn:")
    cell = input("Enter the number to play with: ")
    # Check if input is available or not
    if not cell.isdigit() or int(cell) < 1 or int(cell) > 9:
      print("Invalid input. Please type a number between 1 and 9")
      continue
    row = (int(cell) - 1) // 3
    col = (int(cell) - 1) % 3
    # Check if cell is already choosen or not
    if board[row][col] in ['X', 'O']:
      print("That cell is already choosen. Please choose another.")
      continue
    # Place mark in cell
    board[row][col] = turn
    print_board(board)
    # Check for gain or draw
    if check_win(board, turn):
      print(f"Player {turn} wins!")
      break
    if all(cell in ['X', 'O'] for row in board for cell in row):
      print("It's a draw!")
      break
    # Switch turn
    turn = 'O' if turn == 'X' else 'X'


# Start game
play_game()
