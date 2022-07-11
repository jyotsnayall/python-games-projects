
from random import shuffle

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist


def player_guess():
    
    valid_guesses = [0,1,2]
    guess = ''
    
    guess = int(input("Choose a number: 0,1 or 2 "))
    
    while guess not in valid_guesses:
         guess = int(input("Invalid choice. Please enter again (0,1 or 2): "))
    
    return guess


def check_guess(mylist,guess):
    if mylist[guess] == 'O':
        print("\n",mylist)
        print("Correct, You WIN!")
    else:
        print("\nOOF! Wrong choice")
        print(mylist)
        print("Better luck next time!")


def game():
    
    mylist = [' ','O',' ']
    
    mixed_list = shuffle_list(mylist)
    
    guess = player_guess()
    
    check_guess(mixed_list,guess)

    restart = input("\nDo you want to play again? (y/n): ")
    if restart.lower()=='y':
        game()


if __name__ == "__main__":
    game()