from datetime import datetime
import random

def coinflip():
    r = random.randint(1,2)

    if r == 1:
        return "heads"
    elif r == 2:
        return "tails"

def cdate():
    date_time = datetime.now()
    return date_time

def randnumb():
    #generates a random number from 1, 100
    e = random.randint(1,100)
    return(e)

def mMessage():
    ee = random.randint(1,3)
    
    if ee == 1:
        return "Never give up on your passion!"
    elif ee == 2:
        return "Never quit!"
    elif ee == 3:
        return "Be persistent and never give up!"
