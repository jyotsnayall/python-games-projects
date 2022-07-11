
import getpass

options = ['r','p','s','rock','paper','scissors']

win = {'rock':'scissors', 'paper':'rock', 'scissors':'paper', 'r':'s', 'p':'r', 's':'p'}


def check_valid_move():
    #Checking if the moves are valid
    move = getpass.getpass('Rock(R), Paper(P), Scissors(S) -> Choose One ')
    if (move.lower() in options):
        return move.lower()
    else:
        print("Invalid move. Please enter new move: ")
        check_valid_move()

def game():

    player1 = input("Enter your name first player: ")
    player2 = input("Enter your name second player: ")

    victory = {player1 : 0, player2 : 0}


    rounds = input("How many rounds do you want to play? ")

    for i in range(int(rounds)):

        print(f"Round - {i+1}")
        print("-------------")

        turn = player1

        print(f"It's {turn}'s turn")
        move1 = check_valid_move()

        #Changing turns
        if turn == player1:
            turn = player2
        else:
            turn = player1


        print(f"It's {turn}'s turn")
        move2 = check_valid_move()

        #printing chosen moves
        print(f"{player1} = {move1.upper()}\tvs\t{player2} = {move2.upper()}")

        #Checking the winner in each round
        if move1 == move2:
            print("Sheesh\nITS A TIE!\n")
            continue

        elif move2 in win[move1]:
            print(f"{player1} SCORES!\n")
            victory[player1] += 1

        else:
            print(f"{player2} SCORES!\n")
            victory[player2] += 1


    #Declaring Winner
    if victory[player1] > victory[player2]:
        print(" -        GAME OVER             -")
        print(f"{player1} = {victory[player1]} \t {player2} = {victory[player2]}")
        print(" ------ WINNER :"+ player1 + "----------")
        

    if victory[player1] < victory[player2]:
        print(" -        GAME OVER             -")
        print(f"{player1} = {victory[player1]} \t {player2} = {victory[player2]}")
        print(" ------ WINNER :"+ player2 + "----------")
        

    if victory[player1] == victory[player2]:
        print(" -        GAME OVER             -")
        print(f"{player1} = {victory[player1]} \t {player2} = {victory[player2]}")
        print(" ------ IT'S A TIE! YOU BOTH LOSE! HAH! SUCKERS!----------")
        



    restart = input("Do you wanna play again ? (y/n)")

    if restart == 'Y' or restart == 'y':
        game()

    

if __name__ == "__main__":
    game()