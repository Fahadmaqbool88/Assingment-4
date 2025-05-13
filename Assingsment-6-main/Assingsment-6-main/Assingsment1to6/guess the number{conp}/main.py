import random
print("welcom to number guessing game")
low = 1 
high = 10
print("think of  a number between 1 to 10 and computer will be guess it")
if low <= high:
    guess = random.randint(low,high)
    print(" computer  guess is " , guess)
    while True:
        feedback = input("is a guess too high (h) too low(l) are correct(c)?").strip().upper()
        if feedback == 'C' :
            print("yay the computer guess your number")
            break
        elif feedback == "H" : 
            high= guess-1
            guess=random.randint(low, high)
            print('computer guess is : ', guess)
        elif feedback == "L" : 
            high= guess+1
            guess=random.randint(low, high)
            print('computer guess is : ', guess)
        else: 
            print("Invalid input. Please enter H, L, or C.")

if low > high:
    print('the number is not in thhe range. Please try again.')