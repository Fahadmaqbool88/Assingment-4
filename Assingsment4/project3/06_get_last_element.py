def get_last_element():
    """promps the user to inter one element of the list at a time and return the resulting list"""
    lst=[]
    elem=input("please inter and element of the list are press inter to stop")
    while elem !="":
        lst.append(elem)
        elem=input("please inter and element of the list are press inter to stop")
    return elem
def main():
    lst=get_last_element()
    get_last_element(lst)
if __name__=="__main__":
    main()