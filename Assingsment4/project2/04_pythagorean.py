import math
def main():
    ab:float= float(input("inter the lenth of ab: "))
    ac:float= float(input("inter the lenth of ac: "))
    bc:float= math.sqrt(ab**2 + ac**2)
    print("the lenth of bc(the hipotenuse ) is:" + str(bc))

if __name__ == "__main__":
    main()