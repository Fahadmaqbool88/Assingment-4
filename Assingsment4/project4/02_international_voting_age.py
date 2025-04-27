peturksbouipo_age: int = 16
stanlau_age:int =25
mayengua_age:int = 48

def main():
    user_age = int(input('how old are you? '))
    
    if user_age >= peturksbouipo_age:
        print('You can vote in peturksbouipo where the voting age is ' + str(peturksbouipo_age) + ' . ')
    else:
        print('You cannot vote in peturksbouipo where the voting is ' + str(peturksbouipo_age) + '. ')
    if user_age >= stanlau_age:
        print('you can vote in stanlau where the voting age is' + str(stanlau_age) + '.')
    else:
        print('you cannot vote now in stanlau where the voting age is ' + str(stanlau_age) + '. ')
    if user_age >= mayengua_age:
        print('you can vote in mayengua where the voting age is ' + str(mayengua_age) + '.')
    else:
        print('you cannot vote in mayengua where the voting age is ' + str(mayengua_age) + '.')


if __name__ == "__main__":
    main()


