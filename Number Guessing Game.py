## Number Guess Game by Shaharear
import random
# to create a range of random numbers between 1-10
n = random.randrange(1,100)
# input to enter a number
f = int(input("Guess any number: "))
while n!= f: 
    # if smaller than n
    if f < n:
        print("Its Too low")
        # to again ask for input
        f = int(input("Guess the number again: "))
    # if greater than n
    elif f > n:
        print("Its Too high!")
        # to again ask for the user input
        f = int(input("Guess the number again: "))
    # if equals to n End the while loop
    else:
        break
print("Congratulations! you guessed it right!!")
