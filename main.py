class Pet():
    def __init__(self, pet_name):
        self.name = pet_name
        self.age = 0
        self.hunger = 5
        self.boredom = 3
        self.sleepiness = 3
        self.dead = False
        
    def __str__(self):
        string = f"""Name: {self.name}
        Age: {self.age}
        Hunger: {self.hunger}
        Boredom: {self.boredom}
        Sleepiness: {self.sleepiness}
        Dead? {self.dead}
        """
        return string

    def feed(self):
        #check if the pet is dead, if it is, return nothing
        if self.dead:
            return
        #reduce hunger by 3 but not below zero
        self.hunger = self.hunger - 3
        if self.hunger < 0:
            self.hunger = 0

#sleep
    def sleep(self):
        #check if the pet is dead, if it is, return nothing
        if self.dead:
            return
        #reduce sleepiness by 3 but not below zero
        self.sleepiness = self.sleepiness - 3
        if self.sleepiness < 0:
            self.sleepiness = 0
#play
    def play(self):
        #check if the pet is dead, if it is, return nothing
        if self.dead:
            return
        #reduce boredom by 3 but not below zero
        self.boredom = self.boredom - 3
        if self.boredom < 0:
            self.boredom = 0

#wait (increases age and hunger, boredom and sleepiness. must happen when another action happens.)
    def wait(self):
        #check if the pet is dead, if it is, return nothing
        if self.dead:
            return
        #increase age by 1
        self.age = self.age + 1
        self.hunger = self.hunger + 1
        self.boredom = self.boredom + 1
        self.sleepiness = self.sleepiness + 1

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

    if pet1.is_dead():

    name = input("What do you want your pet to be called?")
    pet = Pet(name)
    print(pet)
    action = input("What do you want to do with your pet? ")
while action != "":
if action == "feed":
#feed the pet
pet.feed()
#make time pass
pet.wait()
#fill in the if statement for the rest of the actions with elifs
if action == "play":
#play
if action == "sleep":
#sleep, wait
#wait
else:
print("You can only choose to feed, play, sleep or wait. ")
print("-----------------------------------------------------")
print(pet)
print("-----------------------------------------------------")
action = input("What do you want to do with your pet? ")
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