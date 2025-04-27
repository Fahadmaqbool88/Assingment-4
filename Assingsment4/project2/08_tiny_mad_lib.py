sentence_start:str="panavesity is fun i learn to programe and used python to make my "
def main():
    adjective:str= input("plese type an adjective and press inter ")
    noun:str= input("plese type an noun and press inter ")
    verb:str= input("plese type an verb and press inter ")
    print(sentence_start + adjective + " " + noun + " " + verb + " !")
if __name__ =="__main__":
    main()