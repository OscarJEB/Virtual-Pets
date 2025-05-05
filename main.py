class Pet():
    def __init__(self, pet_name):
        self.name = pet_name
        self.age = 0
        self.hunger = 5
        self.boredom = 3
        self.sleepiness = 3
        self.dead = False
    def pretty_print(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Hunger: {self.hunger}")
        print(f"Boredom: {self.boredom}")
        print(f"Sleepiness: {self.sleepiness}")
        print(f"Death? {self.dead}")

def feed(self):
    #check if the pet is dead, if it is, return nothing
    if self.dead:
        return
    #reduce hunger by 3 but not below zero
    self.hunger = self.hunger - 3
    if self.hunger < 0:
        self.hunger = 0

def check_death(self):
    if self.boredom >=10:
        self.dead = True

    if self.age >= randint(15,20):
        self.dead = True

    if self.hunger >=10:
        self.dead = True

    if self.sleepiness >=10:
        self.dead = True

def is_dead(self):
    #just return the value stored in the dead attribute 
    return self.dead

pet1 = Pet("John Dog")
pet1.pretty_print()

####----Task 1----####
#Set up your pet with the following attributes:
#name (make this mandatory), age (default:0), hunger (default: 5), boredom (default:3), sleepiness(default:3)
#completed
####----Task 2----####
#instantiate your pet object with the name of your choice
#completed
####----Task 3----#### 
# We need to add the following methods to our Virtual Pet:
# 1. Feed - which will reduce hunger by 3
# use a selection to make sure if hunger goes below zero it gets reset to 0 (we don’t want any negative numbers.)
# 2. Play - which will reduce boredom by 3
# 3. Sleep - which will reduce sleepiness by 5
# 4. Wait - which will increase age, and increase hunger, boredom and sleepiness
# 5. Is_dead - which will check to see if the Pet has hit the thresholds we have set as the
# maximum possible hunger, boredom and sleepiness
#completed
###----Task 4----####
# Make a new method called check_death() that checks when a pet dies.
# These are the conditions I have chosen to use to determine if the pet should be dead.
# (Note: you can change these to make your pet harder or easier to keep alive)
    # ● Boredom is at 10
    # ● Sleepiness is at 10
    # ● Hunger is at 10
    # ● Age is at a random age between 15 and 20 or more
#completed

#Go to page 9 of the tutorial to learn how to make the mainline (https://classroom.google.com/w/NzE2NTQ0NzA2MTYx/t/all)

#guide pdf drive link: https://drive.google.com/file/d/1PSriUM6QVDamoWhjDcGgMrF0at5lYVXT/view