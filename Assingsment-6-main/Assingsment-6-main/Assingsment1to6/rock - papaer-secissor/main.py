import random
print("welcom to the rock,paper,secissor game")
choices= ["rock","paper","secissor"]
user_scor = computer_scor = 0
print("Let's play")
while True:
    user_input = input("type rock,paper,secissor or q to quit: ").lower()
    if user_input == "q":
        print(f"final score - you: {user_scor},computer: {computer_scor}")
        print("thanks for playing")
        break
    if  user_input not in choices:
        print("invalid input,please try again")
        continue
    computer_chose = random.choice(choices)
    print(f"computer chose {computer_chose}")
    if user_input== computer_chose :
        print("it is  a tie")
    elif(user_input=="rock" and computer_chose=="scissor") or \
          (user_input=="paper" and computer_chose=="rock") or\
          (user_input=="scissor" and computer_chose=="paper"):
        print("you win")
        user_scor+= 1
    else:
        print("computer wins")
        computer_scor += 1
    print(f'current score - you: {user_scor}, computer: {computer_scor}')

 
