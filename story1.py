from getters import*

def Story1 (debug = False):
    if debug: print ("story1 function")
    print("/n")
    place1=getWord("enter a bad place", debug)
    person1=getWord("enter the name of person you dont like:")
    gender1=getWord("he/she")
    activity1=getWord("enter an enjoyable activity you do at work")
    out=""
    out+= "one day, I woke up early and went to:" + place1
    out+="I do not like this place in the slightest because of one particular person. their name is"+person1
    out+="This person is my"+position1 
    out+="and"+gender1
    out+="does not like anything that has to do with happiness because of his very established work ethic"
    out+= "the last person got fired just for"+activity1
    
    
    
    return out
    
