def main():
    print("this programe adds two numbers.")
    num1 : str = input("enter first number:")
    num1 : int = int(num1)
    num2 : str = input("enter second number:")
    num2 : int = int(num2)
    total : int = num1 + num2
    print("the total is " + str(total)+ ".")


if __name__ == '__main__':
    main()
    