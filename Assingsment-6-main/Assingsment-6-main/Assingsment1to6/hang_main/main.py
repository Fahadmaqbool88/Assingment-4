import random
stages = [ """ 
  ------ 
  |     |
  |   
  |
  |
  | 
  ------
                                       
""",
"""
    ------
    |     |
    |     
    |
    |
    |
     --------
""" , """
  --------
  |       |
  |       o
  |        |
  |
  |
  |
  ----------

""",


"""
   -----------
   |          |
   |          o
   |         /|
   |
   |
   -----------

""",
"""
  --------
  |       |
  |       

"""
          ]
words = ["apple","banana","grab","orange","kiwi","mango","peach"]
choosen_word= random.choice(words)
word_display= ["__" for _ in choosen_word]
guess_latters=[]
lives= len(stages)-1
print("welcome to Hang main")
print("guess the word letter by letter")
while True:
    print(''.join(word_display))
    guess= input("guess a latter :").lower()
    if not guess.isalpha() or len(guess)!= 1:
        print("please inter a valid latter")
        continue
    if guess in guess_latters:
        print("you all ready guess the latter try again")
        continue
    guess_latters.append(guess)
    if guess in choosen_word :
        print(f"good guess ' {guess}' is in the world ")
        for index, latter in enumerate(choosen_word):
         if latter == guess:
            word_display[index]= guess
    else :
       print(f"sorry, '{guess}'is not in the word")
       print(stages[len(stages)-lives-1])
       lives-= 1
       print(f"you have {lives} lives lefta")
       if lives== 0:
          print(stages[lives])
          print(f"you lose the word was ' {choosen_word} '")
          break
       

