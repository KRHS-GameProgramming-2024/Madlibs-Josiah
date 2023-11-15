from getters import*

def Story1 (debug = False):
    if debug: print ("story1 function")
    print("Begin")
    place=getWord("enter a bad place: ", debug)
    person=getWord("enter the name of person you dont like: ")
    position=getWord("enter the title of as position at work,boss,supervisor,ect: ")
    gender=getWord("he or she: ")
    trauma=getWord("name a traumatic or emberasing experience: ")
    activity=getWord("enter an enjoyable activity you do at work: ")
    car=getWord("name a vehicle: ")
    carrer=getWord("enter a lifelong carrer: ")
    age=getWord("enter your age")
    
    
    
    
    
    out=""
    out+="one day, I woke up early and went to " +place
    out+=" I do not like this place in the slightest because of one particular person. their name is " +person
    out+=" This person is my " +position
    out+=" and " +gender
    out+=" does not like anything that has to do with happiness because in elementry school he " +trauma
    out+=" the last person got fired just for " +activity
    out+=" I want to quit, but its the only place within walking distance because I dont have a car."
    out+=" I'm trying to get a " +vehicle 
    out+=" so I can leave this place so I can achive my dream of being a " +carrer
    out+=" But I cant because im stuck here and have no way to leave " 
    out+=" I can't take this kind of stress and torement for a " +age
    out+=" year old. I hope im able to get out of here soon."
    
    
    
    return out
    
