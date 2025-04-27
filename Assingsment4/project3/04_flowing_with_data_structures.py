def add_three_copies(my_list,data):
   for i in range(9):
    my_list.append(data)
def main():
  message=input("inter a message to copy")
  my_list=[]
  print("list before:",my_list)
  add_three_copies(my_list,message)
  print("list after :",my_list)
if __name__=="__main__":
  main()