from IPython.display import clear_output

# ==== set globals
# board = dict() with key : value from 0 - 9
# players = ()

players = []

board = {1: '1', 2: '2', 3: '3', 4: '4',
         5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}


def print_board():
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-|-|-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-|-|-')
    print(board[7] + '|' + board[8] + '|' + board[9])


# ===== write function to make choice(players)
 # declare globals players
 # while true
    # input = ask player 1 to pick X or O
    # if input not x or o upper(): continue
    # else
    # assign and print player 1 and player 2
    # return players[0]  = X; players[1] = O
    # return tuple here

def choose():
    global players
    while True:
        choice = input('please choose between X and O:')
        if choice.upper() not in ('X', 'O'):
            continue
        elif choice.upper() == 'X':
            players.extend(['X', 'O'])
            print(
                f'player_{players[0]}: {players[0]} \nplayer_{players[1]}: {players[1]}')
            break
        else:
            players.extend(['O', 'X'])
            print(
                f'player_{players[0]}: {players[0]} \nplayer_{players[1]}: {players[1]}')
            break

# ===== function to choose position(board, players)
  # turn = players[0]
  # print the board
  # for loop the length of board
    # ask player:turn to pick any number position on the board
    # update the board
    # clear canvas
    # check for a win with win()
    # print the board
    # switch player with if
      # if turn == player[0]; then turn = player[1]
      # else turn = player[0]
  # call draw()


def position():
    global board, players
    turn = players[0]
    print_board()
    for i in range(1, len(board)+1):
        while True:
            try:
                choice = int(
                    input(f'player_{turn}, pick any number on the board to play {turn} there:'))
                if board[choice] not in players:
                    board[choice] = turn
                    break
                else:
                    print(
                        f'position {choice} already taken. \npick any number on the board to play {turn} there')
                    continue
            except ValueError:
                print('please input an integer.')
                continue

        clear_output()

        if win(turn):
            return

        print_board()

        if turn == players[0]:
            turn = players[1]
        else:
            turn = players[0]

    draw()

# ===== function to check_win(board,players)
  # if rows, columns and diagonals are equal to players[0 or 1];
    # print the board
    # print the player that won
    # ask for a rematch or end_game
  # else :  pass


def win(whose_turn):
    move = True
    if board[1] == board[2] == board[3] or \
       board[4] == board[5] == board[6] or \
       board[7] == board[8] == board[9] or \
       board[1] == board[4] == board[7] or \
       board[2] == board[5] == board[8] or \
       board[3] == board[6] == board[9] or \
       board[1] == board[5] == board[9] or \
       board[3] == board[5] == board[7]:
        print_board()
        print(f'player_{whose_turn} is the winner !!!!')
        while move:
            choice = input('do you want to play again? [y/n]:')
            if choice.lower() in ('y', 'n'):
                move = False
                if choice.lower() == 'y':
                    start_game()
                else:
                    end_game()
                    return True
            else:
                continue
    else:
        pass

# ===== function for draw
# ask for rematch() or end_game()


def draw():
    move = True
    print_board()
    print('There was a tie !!!!')
    while move:
        choice = input('do you want to play again? [y/n]:')
        if choice.lower() in ('y', 'n'):
            move = False
            if choice == 'y':
                start_game()
            else:
                end_game()
        else:
            continue


# ===== function end_game
  # clear board
  # print GAME OVER

def end_game():
    reset_game()
    print('GAME OVER !!!!!!')


def reset_game():
    board = {1: '1', 2: '2', 3: '3', 4: '4',
             5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
    clear_output()


# ===== function to start game start_game()
  # clear board
  # choice()
  # position()

def start_game():
    reset_game()
    choose()
    position()


# uncomment the line below and run this script to play game
# start_game()
