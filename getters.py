def getMainMenuoption(debug = False):
    if debug: print("getMainMenueoption Function")
    
    goodinput = False
    
    while not goodinput:
        option = input("please select an option ")
        option.lower()
        if option == "q" or option == "quit" or option == "exit":
            option= "q"
            goodinput = True
            
        elif (option == "1" or
            option == "one" or
            option == "story 1" or
            option == "story1"):
                option = "1"
                goodinput = True
        
         elif (option == "2" or
            option == "two" or
            option == "story 2" or
            option == "story2"):
                option = "2"
                goodinput = True
        
        elif (option == "upupdowndownleftrightleftrightbastart"):
             print ("congrats youve unlocked the easter egg")
        
        else:
            print("please make a valid choice")
            
    return option

def getWord(prompt, debug = False):
    if debug: print("getMenueoption Function")
    
    goodinput = False
    
    while not goodinput:
        word = input(prompt)
        goodinput = True
        if isSwear (word):
            goodinput = False
            print ("DONT USE THAT *$%@#&% LANGUAGE")
      
      
    return word

        
        

def isSwear(word, debug = False): 
    if debug: print("isSwear Function")
    if word.lower()in swearlist:
        return True
    else:
        return False
        
swearlist = ["poop",
             "pee",
             "piss",
             "cunt",
             "shit",
             "fuck",
             "chink",
             "nigga",
             "nigger",
             "jap",
             "bimbo",
             "jew",
             "sex",
             "dick",
             "penis",
             "vagina",
             "coochie"
             "pussy",
             "dildo",
             "fleshlight",
             "pedophile",
             "prostitute",
             "molest",
             "beaner",
             "satan",
             "demon",
             "devil",
             "666",
             "999",
             "terrorist",
             "lgbtq",
             "bisexual",
             "gay",
             "lesbian",
             "rapist",
             "racist",
             "hell",
             "they",
             "them",
             "ze",
             "zer",
             "stripper",
             ]
