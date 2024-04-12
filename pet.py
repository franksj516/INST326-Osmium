
#division of functions
"""

Erick Rivadeneira: Pet Selection and Initialization
Function/Method to Implement: choose_pet()
Information Needed: This method will prompt the player to 
choose a pet type and its characteristics (e.g., breed, name) 
through command-line input or selection from a predefined list.
Outcome: It returns an instance of the Pet class with the chosen 
attributes, initializing the pet's state, including name, type, 
level, and health status.

Joseph Franks: level up Function
Function/Method to Implement: level_up()
Information Needed: the level-up functions will take one parameter, 
which will be attention_level (int). This number will reflect how many 
actions the pet has gone through. 
Outcome: The outcome of this function enables the user to have a pet 
that can do more than just be petted and fed. There are all sorts of 
different actions that we may be able to teach the pet, but it can only 
happen when the pet levels up. Attention_level will be a number that 
reflects how many times a specific action has been done. This will be 
used inside of a while statement. While attention_level is less than the 
required amount of attention the pet needs to level up, the pet will not 
level up.

Justin Fargnoli: Pet Activity Function
Function/Method to Implement: teach_trick(trick_name)
Information Needed: The teach_trick function will take the following parameters: 
the trick_name (str) which is the name of the trick to be taught, passed as an argument 
to the method, pet (pet object), an instance of the pet class representing the player’s 
pet, and tricks_file_path (str), the path to the text file containing the tricks and the 
corresponding required levels. This file acts as an external database that the method will 
read to determine if a trick is available and what level the pet needs to be to learn it.
Outcome:  If the trick is in the text file and the pet meets the required level, the pet's 
skills are updated to include the new trick, and its happiness level may increase. 
The function returns a success message indicating the pet has learned the trick.
If the trick is not in the text file, it prints a message to the user stating 
that the trick is not available. This provides immediate feedback and guides the 
player to select from the available tricks.
If the trick is available but the pet does not meet the required level, the method 
returns a message indicating the required level and that the pet cannot learn the trick yet.

"""


class Pet:
    def __init__(self, name, pet_type, level=1, health="Healthy"):
        self.name = name
        self.pet_type = pet_type
        self.level = level
        self.health = health



# This is Erick's function
def choose_pet():
    print("Choose your Pet!")
    #Defining a pre-defined list of pet-types
    pet_list=["dog", "cat", "bird", "fish", "lizard", "snake"]
    print("Choose a pet from the following list:")
    # printing out the listed options that player can choose from for their pet breed
    for index, type in enumerate(pet_list, start=1):
        print(f"{index}. {type}")
    choice = int(input("Enter the number to the pet of your choosing: "))
    # validation of whether or not the input falls under the indexed range
    if choice <1 or choice > len(pet_list):
        print("This choice is invalid and out of range. Please try again.")
        return choose_pet()
    # input name of pet
    name=input("Now that you've chosen your pet type, please name your pet: ")
    # creating an instance of the inputted pet name and chosen breed
    return Pet(name, pet_list[choice-1])

pet = choose_pet()
print(f"Congrats! You have a pet! You have chosen a {pet.pet_type} named {pet.name}.")
print(f"Your pet is currently at Level: {pet.level} and Health: {pet.health}.")



#This is Justin's function
def teach_trick(trick_name):
    #read the tricks from a file and build a dictionary of trick: required_level
    tricks = {}
    with open ("tricks.txt", "r") as file:
        for line in file:
            trick, level = line.strip().split(", ")
            tricks[trick] = int(level)

    #check if trick is in the file
    if trick_name in tricks:

    #assuming we have a previously defined pet instance
        if pet.level >= tricks[trick_name]:
            pet.learn_trick(trick_name)
        else :
            required_level = tricks[trick_name]
            print(f"Your pet needs to be level {required_level} to learn {trick_name}.")
    else:
         print("This trick is not available.")



#joseph's method
def level_up(self, attention_points):
    #define the threshold for leveling up
    level_threshold = 15  
    #check if the attention_points meet the threshold for leveling up
    while attention_points >= level_threshold:
        #increases the pet's level
        self.level += 1
        #updates attention_points after leveling up
        attention_points -= level_threshold
        #prints a message that the pet has leveled up
        print(f"Congratulations! {self.name} has leveled up to level {self.level}!")
    #print a message indicating the remaining attention needed to level up
    print(f"{self.name} needs {level_threshold - attention_points} more attention to level up.")



#project description
""""

Our group decided to choose a virtual pet simulation for our final project. 
In this simulation, the user will be prompted to adopt, care for, and train a virtual pet. 
To start, the user will get to choose a type of pet, anywhere from a dog or a cat, 
to a snake or a hedgehog. They will also be able to customize different characteristics 
that the pet has, including its name, breed, and color. The gameplay centers around the 
\player-pet interaction within a simulated environment, where the player must attend to the 
pet’s needs (feeding, grooming) and can engage in activities (walking, teaching tricks) to 
enhance the pet’s skills and happiness level. The pet progresses through levels based on the 
frequency of these interactions, unlocking new activities and tricks with each level. This 
also gives the user more excitement, as you can only start out by feeding and petting the 
cat, and can end up with multiple different actions. 

Regarding the code itself, the primary class, Player, will encapsulate the player's actions 
and decisions, maintaining the state of the pet and the game environment. This class 
will manage the game flow, including the execution of actions like feeding, playing, and 
training, reflecting changes in the pet's status in response to these actions. Our project 
will demonstrate class definition and method implementation, and other features such as 
conditional expressions, comprehensions, command-line arguments for performing specific 
actions such as selecting a pet, different modules such as the argparse module to handle 
command-line arguments, exception raising (ex: if pet cannot yet learn trick), and reading 
from a text file for possible tricks that the pet can learn.

"""