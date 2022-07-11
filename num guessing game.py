
import random

num = random.randint(1,101)

def rules():
    print("WELCOME TO GUESS ME!")
    print("I'm thinking of a number between 1 and 100")
    print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
    print("If your guess is within 10 of my number, I'll tell you you're WARM")
    print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
    print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
    print("LET'S PLAY!")

def game():

    rules()

    guesses = [0]

    while True:

        guess = int(input("What is your guess? "))
        
        if guess<1 or guess>100:
            print("Invalid guess. It's a number between 1 and 100")
            continue
        
        if guess == num:
            print(f"THAT'S RIGHT, YOU GUESSED IT IN ONLY {len(guesses)} GUESSES!!")
            break
            
            
        guesses.append(guess)
        
        # when testing the first guess, guesses[-2]==0, which evaluates to False
        # and brings us down to the second section
        
        if guesses[-2]:
            if abs(num-guess) < abs(num-guesses[-2]):
                print('WARMER!')
            else:
                print('COLDER!')
    
        else:
            if abs(num-guess) <= 10:
                print('WARM!')
            else:
                print('COLD!')


if __name__ == "__main__":
    game()