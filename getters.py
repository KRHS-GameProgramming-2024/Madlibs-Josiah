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
            goodinput = false
            print ("DONT USE THAT *$%@#&% LANGUAGE WITH ME YOUNG MAN!, do something else")
      
      
    return word
    
def isSwear(word, debug = False): 
    if debug: print ("isSwear Function")
    if word in swearlist:
        return True
    else:
        swearlist = ["poop",
                     "pee"]
        
        

def isSwear(word, debug = False): 
    if debug: print("isSwear Function")
    if word.lower()is swearlist:
        return True
        