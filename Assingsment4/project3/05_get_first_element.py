def get_first_element(lst):
    """prints the first element of a provided list"""
    print(lst[0])
def get_list():
    """promps the user to inter one element of the list at a time and returns the resulting list"""
    lst=[]
    elem:str=input("please inter and element of list or press inter to stop")
    while elem !="":
        lst.append(elem)
        elem=input("please inter and element of the list are press inter to stop")
    return lst
def main():
    lst = get_list()
    get_first_element(lst)
if __name__=="__main__":
    main()

