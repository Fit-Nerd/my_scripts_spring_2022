# Designing and Debugging
# My own choose your own adventure game

from sys import exit

def lobby():
    print("You are standing inside a gym lobby.")
    print("There are paths to the left and to the right.")
    print("There is also a set of stairs leading to the cardio equipment.")
    print("Which way do you go: left, right, or upstairs?")
    
    warm_up = input("> ")
    
    if warm_up == "left":
        weight_room()
    elif warm_up == "right":
        sports()
    elif warm_up == "upstairs":
        cardio()
    else:
        dead("Sufferring from decision fatigue, your muscles atrophy, you find a corner, and assume the fetal position.")

def dead(why):
    print(why, "Good job!")
    print("Do you want to stay in the gym or leave?")
    
    stay_leave = input("> ")
    
    if "stay" in stay_leave:
        print("Back to the lobby with you!")
        lobby()
    else:
        print("Roger that. We are outta here. Enjoy your day!")
        exit(0)
    
def weight_room():
    print("You walk into the weight room.")
    print("There are machines, dumbbells, and squat racks.")
    print("Which do you choose first?")
    
    weights = input("> ")
    
    if weights == "machines":
        print("Ahh, the machines...Are you sure you even lift, bro?")
        print("Maybe you should start in the cardio room.")
        cardio()
    elif weights == "dumbbells":
        print("Oh the glorious land of dumbbells.")
        print("What's the heaviest dumbbell you'll use today?")
        
        DBs = int(input("> "))
        
        if DBs > 50:
            print("Oooohh, lifting with the big boys, eh?")
            print("Maybe you should go to the athletic area afterwards")
            print("You can partake in all the sports.")
            sports()
        else:
            print("Is that it?")
            print("Let's hang out in the weight room until you get stronger")
            weight_room()
    elif "squat" in weights:
        print("Now we're talking!!")
        print("You know what they say...")
        print("Winners always squat, squatters always win.")
        exit(0) 
    else: 
        print("Something's off...would you like the machines, dumbbells, or the squat rack?")
        weight_room()

def sports():
    print("There's all kinds of room for activities over here!")
    print("Would you like to swim, play basketball, or hit the sauna?")
    
    activity = input("> ")
    
    if activity == "swim":
        print("Get your Michael Phelps on!!")
        dead("Grab your goggles and your bathing suit!")
    elif "basketball" in activity:
        print("Lace 'em up and let's run 'em!")
        dead("You play for 6 hours, go undefeated, and are the new King/Queen of the court!")
    elif "sauna" in activity:
        print("Make sure you stay hydrated.")
        print("After all that heat, it'll be nice to lift some weights.")
        weight_room()
    else:
        print("Not the sports type, eh?")
        print("We can always go upstairs to the cardio room.")
        cardio()

def cardio():
    print("You stumble upon a golden room filled with dozens of cardio machines.")
    print("Do you choose the treadmill, stairs, bike, or rower?")
    
    sweaty = input("> ")
    
    if "treadmill" in sweaty:
        dead("Run, Forrest, Run!!")
    elif "stairs" in sweaty:
        print("Stairs...the only REAL form of cardio.")
        print("We should hit the weight room afterwards to get strong legs.")
        weight_room()
    elif "bike" in sweaty:
        print("Let's make Lance Armstrong proud.")
        print("Wait, he was caught fibbing to Oprah.")
        dead("You're asked to leave the gym for impersonating a (successful) liar.")
    elif "rower" in sweaty:
        print("The rower is one torturous device.")
        print("Maybe now you want to go the sports area!")
        sports()
    else:
        print("Hmm, don't see what you like, huh?")
        print("Let's go back to the lobby and revisit our choices.")
        lobby()

lobby()
