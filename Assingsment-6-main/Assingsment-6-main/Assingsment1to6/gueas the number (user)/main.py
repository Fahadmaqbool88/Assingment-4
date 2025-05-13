import random

print('Welcome to the number guessing game')

secret_number = random.randint(1,10)
print('I have secret number between 1 and 10 can you guess it?')

while True:
    try:
        guess= int(input("interview your guess"))
        if guess>secret_number:
         print("two high try again")
        elif guess<secret_number:
         print("two low try again")
        else: 
           print("congratulations you have guessed the number")
           break
    except ValueError:
       print("invalid input please inter a number between 1 and 10")
       