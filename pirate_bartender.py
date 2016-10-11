import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}
 
ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}
 
def askquestions():
    """asks what type of drink a customer likes"""
    print("Yaarrr matey! Welcome to thee barrr!")
    likes = {}
    for flavor in questions:
        answer = input(questions[flavor])
        if answer == "yes" or answer == "y":
            likes[flavor] = "true"
        else:
            likes[flavor] = "false"
    return likes

def createdrink(likes):
    """creates the drink"""
    drink = []
    for flavor in likes:
        if likes[flavor] == "true":
            drink.append(random.choice(ingredients[flavor]))
    return drink   
    
def cocktailname():
    """names the cocktail"""
     
    adjectives = ["Tasty", "Sweet", "Nasty", "Epic", "Spectacular"]
    noun = ["Cobra", "Stinger", "Gunslinger", "Tarantula", "Dude"]
    print((random.choice(adjectives)), (random.choice(noun)))
        
if __name__ == '__main__': 
    """pirate asks questions, creates the drink, and then tells customer the ingredients"""
    likes = askquestions() 
    drink = createdrink(likes)
    print("Ok, I know exactly what you'd like. In this drink, I used a {}".format(drink))
    print("I call this drink the...") 
    cocktailname()
    drinking = True
    while drinking:
        another = input("Would you like another drink? ")
        if another == "yes" or another == "y":
            likes = askquestions()
            drink = createdrink(likes)
            print("Ok, I think you will enjoy this. In this drink, I used a {}".format(drink))
            print("I call this drink the...") 
            cocktailname()
        else:
            drinking = False
            
    print("Alright, have a good night!")
       
   