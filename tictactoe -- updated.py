
board = { '7' : ' ', '8': ' ', '9' : ' ',
          '4' : ' ', '5': ' ', '6' : ' ',
          '1' : ' ', '2': ' ', '3' : ' ' }

board_keys = []

for key in board:
    board_keys.append(key)


def printboard(the_board):
    print(the_board['7'] + '|' + the_board['8'] + '|' + the_board['9'])
    print("-+-+-")
    print(the_board['4'] + '|' + the_board['5'] + '|' + the_board['6'])
    print("-+-+-")
    print(the_board['1'] + '|' + the_board['2'] + '|' + the_board['3'])


def choose_marker():
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    return marker


def take_input():
    num = input("Tell your move ? (1-9)")
    
    while num not in board_keys:
        num = input("Invalid move. Tell your move ? (1-9)")
        continue
    
    return num


def win_check(turn):
    
    return ((board['7'] == board['8'] == board['9'] != ' ') or
    (board['4'] == board['5'] == board['6'] != ' ') or
    (board['1'] == board['2'] == board['3'] != ' ') or 
    (board['7'] == board['5'] == board['3'] != ' ') or 
    (board['1'] == board['5'] == board['9'] != ' ') or 
    (board['7'] == board['4'] == board['1'] != ' ') or 
    (board['8'] == board['5'] == board['2'] != ' ') or 
    (board['9'] == board['6'] == board['3'] != ' '))


def change_turns(turn):
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    
    return turn


def replay():
    restart = input("Do you wanna play again ? (y/n)")
    
    if restart.lower() == 'y':
        for key in board_keys:
            board[key] = ' '
        game()


def game():

    game_on = True

    turn = choose_marker()
    count = 0
    
    while game_on:
        printboard(board)
        
        print("It's your turn " + turn)
    
        move = take_input()
       # put_input(move)
    
        if board[move] == ' ':
            board[move] = turn
            count += 1
        else:
            print("Invalid move; Position is already occupied. Please enter new move: ")
            continue
    
    
        if win_check(turn):
            printboard(board)
            print(" -        GAME OVER             -")
            print(" ------ WINNER :"+ turn + "----------")
            break
            
                
        if count == 9:
            print(" GAME OVER ")
            print(" GAME TIED ")
            break
            
        turn = change_turns(turn)
                
    
    replay()
    


if __name__ == "__main__":
    game()