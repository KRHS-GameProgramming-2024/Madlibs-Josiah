from screens import*
from getters import*
from story1 import*
from story2 import*

def madlibs (debug = False):
    
    if debug: print("welcome to debug")
   
    print (Titlescreen(debug))
    try:
        input ("press enter to continue ")
    except:
        pass
    
    done = False
    
    while not done:
        print (MainMenu(debug))
        choice = getMainMenuoption(debug)
        
        if choice == "q":
            exit(); 
        elif choice == "1":
            print(Story1())
            print("/n")
            input("press enter to continue ")
        elif choice=="2"
        print (Story2())




madlibs(True)
