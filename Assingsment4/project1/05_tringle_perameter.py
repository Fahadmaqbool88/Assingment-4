def tringle():
    print("this code about sum of tringle sides")
    side1:float = float(input("inter your first side no off tringle"))
    side2:float = float(input("inter your second side no off tringle"))
    side3:float = float(input("inter your third side no off tringle"))
    total:float = float(side1+side2+side3)
    print(f'the sum of {side1},{side2} and {side3} is {total}')
if __name__ == "__main__":
    tringle()