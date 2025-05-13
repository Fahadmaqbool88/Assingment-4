def mad_libs():
    print("lets play made libs fill in the blanks with your onwords")
    name=input("give me a name :")
    place=input("give me a place")
    funny_adg=input("give me a funny adjective")
    random_object=input("give me a random object")
    animal=input("give me an animal")
    action_verb=input("give me an action verb")
    funy_exclamation=input("give me a funny exclamation")
    story=f''' ones upon a time there was aperson named {name} who lived in {place}.
    one day found a {funny_adg} {random_object} that belong to a {animal}
    the {animal} was very upset and started to {action_verb} around 
    {name} codn'nt help but laugh and shouted "{funy_exclamation}" '''
    print("/n here is your mad libs story")
    print(story)
if __name__=="__main__":

    mad_libs()