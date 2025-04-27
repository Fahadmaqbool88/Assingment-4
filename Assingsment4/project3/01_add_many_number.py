def add_many_numbers(numbers)-> int:
    """takes in a list of numbers and return the sum of those number"""
    total_so_for:int = 0 
    for number in numbers :
        total_so_for += number
    return total_so_for
def main():
    numbers:list[int]=[1,2,3,4,5]
    sum_of_numbers: int= add_many_numbers(numbers)
    print(sum_of_numbers)
if __name__ == "__main__":
    main()
