import random
import string
def generate_password(lenth):
    character= string.ascii_letters + string.digits + string.punctuation
    password="".join(random.choice(character)for _ in range(lenth))
    return password
lenth=int(input("inter the desired password lenth"))
if __name__=="__main__":
  print("generated password:", generate_password(lenth))  