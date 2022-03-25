import random
answer = random.randint(1,9)
chances = 0
while chances<=5 :
    guess = int(input("Guess the correct number: "))

    if(chances >= 5):
        print("You lose! The Answer is: ", answer)
    else:
        if(guess == answer):
            print("Congratulations! You guessed the correct answer")
            break
        elif(guess > answer):
            print("Your Guess is too High. Try to guess a smaller number than ", guess)
            chances = chances+1
        else:
            print("Your Guess is too Low. Try to guess a higher number than ", guess)
            chances = chances+1


