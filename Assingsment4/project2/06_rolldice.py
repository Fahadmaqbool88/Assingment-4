import random 
num_sides:int =6
def main():
    die1:int = random.randint(1,num_sides)
    die2:int = random.randint(1,num_sides)
    total:int= die1 + die2
    print("dice have ", num_sides,"sides each ")
    print("first die ",die1)
    print("second die ", die2,)
    print("total of two die ", total)
if __name__ == "__main__":
    main()