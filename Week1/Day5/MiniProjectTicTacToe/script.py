# score = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

def display_board(score):
  print('\nTIC TAC TOE')
  print('*' * 17)
  print('*' + (' ' * 2) + (f'{score[0][0]}') + (' ' * 2) + '|' + f' {score[0][1]} ' + '|' + (' ' * 2) + f'{score[0][2]}' + (' ' * 2) + '*')
  print('*' + (' ' * 2) + '---' + '|' + '---' + '|' + '---' + (' ' * 2) + '*')
  print('*' + (' ' * 2) + (f'{score[1][0]}') + (' ' * 2) + '|' + f' {score[1][1]} ' + '|' + (' ' * 2) + f'{score[1][2]}' + (' ' * 2) + '*')
  print('*' + (' ' * 2) + '---' + '|' + '---' + '|' + '---' + (' ' * 2) + '*')
  print('*' + (' ' * 2) + (f'{score[2][0]}') + (' ' * 2) + '|' + f' {score[2][1]} ' + '|' + (' ' * 2) + f'{score[2][2]}' + (' ' * 2) + '*')
  print('*' * 17)
  print()

def player_input(player):
  print(f"Player {player}'s turn...\n")
  entered_row = input('Enter row: ')
  while entered_row != '1' and entered_row != '2' and entered_row != '3':
    entered_row = input('Enter row (1, 2 or 3): ')
  entered_row = int(entered_row) - 1
  entered_column = input('Enter column: ')
  while entered_column != '1' and entered_column != '2' and entered_column != '3':
    entered_column = input('Enter column (1, 2 or 3): ')
  entered_column = int(entered_column) - 1
  return (player, entered_row, entered_column)

def is_valid_move(score, entered_row, entered_column):
  if score[entered_row][entered_column] == ' ':
    return True
  else:
    return False
def score_update(score, entered_row, entered_column, player):
  score[entered_row][entered_column] = player

def check_win(score):
  for row in score:
    if row[0] == row[1] == row[2] != ' ':
      return row[0]
  for column in range(3):
    if score[0][column] == score[1][column] == score[2][column] != ' ':
      return score[0][column]
  if score[0][0] == score[1][1] == score[2][2] != ' ':
    return score [0][0]
  if score[0][2] == score[1][1] == score[2][0] != ' ':
    return score[0][2]
  return 'no winner'

def turn_switch(whose_turn):
  if whose_turn == 'X':
    return 'O'
  if whose_turn == 'O':
    return 'X'

def play():
  score = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
  print("Welcome to TIC TAC TOE!")
  display_board(score)
  winner = check_win(score)
  whose_turn = 'X'
  move_count = 1
  while winner == 'no winner' and move_count < 10:
    valid_move = False
    while valid_move == False:
      player, entered_row, entered_column = player_input(whose_turn)
      valid_move = is_valid_move(score, entered_row, entered_column)
      if valid_move == False:
        print('\nThat move is invalid!')
    score_update(score, entered_row, entered_column, player)
    display_board(score)
    winner = check_win(score)
    if winner == 'X' or winner == 'O':
      print(f'Congratulations! Player {winner} has won the game.')
    move_count += 1
    if move_count > 9 and winner == 'no winner':
      print('This game ended without a winner.')
    whose_turn = turn_switch(whose_turn)


play()