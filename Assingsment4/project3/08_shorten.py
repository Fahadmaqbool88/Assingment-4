max_lenth:int=3
def shorten(lst):
    while len(lst)> max_lenth:
        last_elem=lst.pop()
        print(last_elem)
def get_lst():
    """promps the user to inter one element of the list at a time and returns the resulting list"""
    lst=[]
    elem= input("please inter an element of the list or press inter to stop ")
    while elem!="":
        lst.append(elem)
        elem= input("plese inter an element of list or pree inter to stop")
    return lst
def main():
    lst= get_lst()
    shorten(lst)
if __name__=="__main__":
    main()
