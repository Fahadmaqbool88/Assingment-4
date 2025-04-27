def temp():
    print("this code for converting forhenite to celsius")
    forhenite_digree = float(input("inter your forhenite digree"))
    celsius_digree = (forhenite_digree-32)* 5.0/9.0
    print(f'temreture {forhenite_digree} = {celsius_digree}')
if __name__ == "__main__":
    temp()