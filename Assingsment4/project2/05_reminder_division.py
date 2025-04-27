def main():
    dividend: int = int(input("please enter an integer to be divided:"))
    divisor: int = int(input("Please Enter an integer to divide by:"))

    qoutient: int = dividend // divisor
    reminder: int = dividend % divisor
    print("The result of this division is " + str(qoutient) + " with a remainder of " + str(reminder))
if __name__ == "__main__":
    main()