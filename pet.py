import random
import json
import sys

class Pet:
    def __init__(self, name, pet_type, level=1):
        self.name = name
        self.pet_type = pet_type
        self.level = level
        self.health = 25  # Starting health at 25%
        self.happiness = 10  # Starting happiness at 10 points
        self.skills = []  # List to store learned tricks
        self.activity_count = 0 # count of instances of feeding and playing
        self.level_up_threshold = 5 #num activities req to level up initially
        self.prize_range = 10  # Range of numbers for the mini-game
        self.prize_attempts = 5  # Number of attempts for the mini-game
        self.customizations = {}

    def teach_trick(self, trick_name, past_tense, required_happiness):
        if self.happiness >= required_happiness:
            if trick_name not in self.skills:
                self.skills.append(trick_name)
                print(f"{self.name} has learned the trick: {trick_name}!")
        else:
            print(f"{self.name} is not happy enough to learn {trick_name}.")

    def feed(self):
        if self.health < 100:
            self.health += 20
            self.health = min(self.health, 100)
            self.activity_count += 1
            print(f"{self.name} was fed and looks healthier!")
            self.check_level_up()
        else:
            print(f"{self.name} is already well-fed.")


    def play(self):
        if self.happiness < 100:
            self.happiness += 5
            self.happiness = min(self.happiness, 300)
            self.activity_count += 1
            print(f"{self.name} played and looks happier!")
            self.health -= 10
            if self.health <= 15:           
                print(f"Feed your pet! It's health is almost depleted")
            self.check_level_up()
        else:
            print(f"{self.name} is already very happy.")

    def check_level_up(self):
            if self.activity_count >= self.level_up_threshold:
                self.level += 1
                self.level_up_threshold += 2  # Increase the threshold for the next level
                self.activity_count = 0  # Reset the activity count
                print(f"{self.name} has leveled up to level {self.level}!")
                print("Let's play a mini-game for a prize.")
                target_number = random.randint(1, self.prize_range)
                print(f"I'm thinking of a number between 1 and {self.prize_range}. Guess it!")
                for attempt in range(self.prize_attempts):
                    guess = int(input(f"Attempt {attempt+1}/{self.prize_attempts}: Enter your guess: "))
                    if guess == target_number:
                        print("Congratulations! You guessed the correct number!")
                        # Give the pet a prize or perform any other action
                        self.customize_pet()
                        break
                    elif guess < target_number:
                        print("Too low! Try a higher number.")
                    else:
                        print("Too high! Try a lower number.")
                else:
                    print(f"Sorry, you've run out of attempts. The number was {target_number}. Better luck next time!")


    def customize_pet(self):
        with open("customization_options.json", "r") as file:
            customization_options = json.load(file)["customization_options"]

        print("Choose a category to customize your pet:")
        for index, category in enumerate(customization_options.keys(), start=1):
            print(f"{index}. {category}")

        category_choice = int(input("Enter the number for the category you want to choose: "))
        selected_category = list(customization_options.keys())[category_choice - 1]

        # Check if the category already has a customization
        if selected_category in self.customizations:
            del self.customizations[selected_category]  # Remove the previous customization

        print(f"Choose an option from the {selected_category} category:")
        for index, option in enumerate(customization_options[selected_category], start=1):
            print(f"{index}. {option}")

        option_choice = int(input("Enter the number for the option you want to choose: "))
        selected_option = customization_options[selected_category][option_choice - 1]

        # Add the new customization to the list
        self.customizations[selected_category] = selected_option

        print(f"{self.name} has been customized with a/an {selected_option}!")


def choose_pet():
    print("Choose your Pet!")
    pet_list = ["dog", "cat", "bird", "fish", "lizard", "snake"]
    print("Choose a pet from the following list:")
    for index, type in enumerate(pet_list, start=1):
        print(f"{index}. {type}")
    choice = int(input("Enter the number to the pet of your choosing: "))
    if choice < 1 or choice > len(pet_list):
        print("This choice is invalid and out of range. Please try again.")
        return choose_pet()
    name = input("Now that you've chosen your pet type, please name your pet: ")
    pet = Pet(name, pet_list[choice - 1])
    return pet

def choose_activity(pet):
    print("Choose an action for your pet:")
    with open("tricks.txt", "r") as file:
        tricks = [line.strip().split(", ") for line in file if line.strip()]
    for index, (present, past, happiness) in enumerate(tricks, start=1):
        required_happiness = int(happiness)  # Declare required_happiness here
        print(f"{index}. {present} (requires {required_happiness} happiness points)")
    choice = int(input("Enter the number for the action you want to perform: "))
    if 1 <= choice <= len(tricks):
        present_action, past_action, required_happiness = tricks[choice - 1]
        required_happiness = int(required_happiness)
        if pet.happiness >= required_happiness:
            pet.teach_trick(present_action, past_action, required_happiness)
            print(f"{pet.name} {past_action}.")
        else:
            print(f"{pet.name} is not happy enough to learn {present_action}.")
    else:
        print("Invalid choice. Please try again.")








def show_pet_status(pet):
    print(f"{pet.name}'s Status:")
    print(f"Health: {pet.health}%")
    print(f"Happiness: {pet.happiness} Points")
    print(f"Level: {pet.level}")
    print(f"Skills: {', '.join(pet.skills)}")
    if pet.customizations:
        print("Customizations:")
        for category, option in pet.customizations.items():
            print(f"{category}: {option}")


def main_menu(pet):
    while True:
        print("\nWhat would you like to do?")
        print("1. Feed Pet")
        print("2. Play with Pet")
        print("3. Teach or Perform a Trick")
        print("4. Show Pet Status")
        print("5. Exit Game")
        choice = input("Enter your choice: ")
        if choice == '1':
            pet.feed()
        elif choice == '2':
            pet.play()
        elif choice == '3':
            choose_activity(pet)
        elif choice == '4':
            show_pet_status(pet)
        elif choice == '5':
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice, please enter a number between 1 and 5.")

# Start the game
pet = choose_pet()
print(f"Congrats! You have a pet! You have chosen a {pet.pet_type} named {pet.name}.")
print(f"Your pet is currently at Level: {pet.level}.")
main_menu(pet)

"""
class Pet:
    def __init__(self, name, pet_type, level=1):
        self.name = name
        self.pet_type = pet_type
        self.level = level

        self.daily_activities = set()




    # Method to teach a trick to the pet
    def teach_trick(self, trick_name, tricks):
        # Check if the trick is in the tricks file
        if trick_name in tricks:
            # Check if the pet meets the required level to learn the trick
            if self.level >= tricks[trick_name]:
                # Add the trick to the pet's skills
                self.skills.add(trick_name)
                print(f"{self.name} has learned the trick: {trick_name}!")
                # Increase pet's happiness level or perform other actions
            else:
                # Inform the player that the pet needs a higher level to learn the trick
                required_level = tricks[trick_name]
                print(f"{self.name} needs to be level {required_level} to learn {trick_name}.")
        else:
            # Inform the player that the trick is not available
            print(f"The trick {trick_name} is not available.")

    # Method to level up the pet
    def level_up(self, attention_points, level_requirements):
        # Increase the pet's level based on attention points
        level_threshold = 7
        while attention_points >= level_threshold:
            self.level += 1
            print(f"Congratulations! {self.name} has leveled up to level {self.level}!")
            # Check if the pet can learn a new trick at this level
            if self.level <= len(level_requirements):
                new_trick = list(level_requirements.keys())[self.level - 1]
                self.teach_trick(new_trick, level_requirements)
            attention_points -= level_threshold
        print(f"{self.name} needs {level_threshold - attention_points} more attention to level up.")






# This is Erick's function
def choose_pet():
    print("Choose your Pet!")
    pet_list = ["dog", "cat", "bird", "fish", "lizard", "snake"]
    print("Choose a pet from the following list:")
    for index, type in enumerate(pet_list, start=1):
        print(f"{index}. {type}")
    choice = int(input("Enter the number to the pet of your choosing: "))
    if choice < 1 or choice > len(pet_list):
        print("This choice is invalid and out of range. Please try again.")
        return choose_pet()
    name = input("Now that you've chosen your pet type, please name your pet: ")
    pet = Pet(name, pet_list[choice - 1])

    # Load available tricks from the test.txt file
    level_requirements = {}
    with open("test.txt", "r") as file:
        for line in file:
            elements = line.strip().split(", ")
            present_tense = elements[0]
            past_tense = elements[1] if len(elements) > 1 else elements[0]
            level = int(elements[2])
            level_requirements[present_tense] = (past_tense, level)

    return pet, level_requirements


    #perform_activity and reset_daily_activities dded by Justin 4/29, discuss with group
def perform_activity(self, activity):
    with open("activities.txt", "r") as file:
        available_activities = [line.strip() for line in file]        
    if activity in available_activities - self.daily_activities:
        self.daily_activities.add(activity)
        print(f"{self.name} has done {activity} today.")
    else:
        print(f"{self.name} has already done {activity} today or it is not available.")

def choose_activity(pet, level_requirements):
    while True:
        print("Choose an action for your pet:")
        for index, action in enumerate(level_requirements.keys(), start=1):
            present_action, past_action = action, level_requirements[action][0]
            print(f"{index}. {present_action}")
        choice = int(input("Enter the number for the action you want to perform: "))
        
        if 1 <= choice <= len(level_requirements):
            chosen_action = list(level_requirements.keys())[choice - 1]
            past_action, level_requirement = level_requirements[chosen_action]
            
            if pet.level >= level_requirement:
                print(f"{pet.name} {past_action}.")
                # Increment attention level (assuming attention level is stored elsewhere)
                break  # Exit the loop if the action is performed successfully
            else:
                print(f"{pet.name} needs to be level {level_requirement} to perform {chosen_action}.")
        else:
            print("Invalid choice. Please try again.")
    return pet



    #We may need to make the player reset the day manually like so:
def reset_daily_activities(self):
    self.daily_activities.clear()
    print(f"Daily activities for {self.name} have been reset.")
    #or we can figure out a way to auto reset based on system time

# Choose a pet
pet, available_tricks = choose_pet()
print(f"Congrats! You have a pet! You have chosen a {pet.pet_type} named {pet.name}.")
print(f"Your pet is currently at Level: {pet.level}.")
pet = choose_activity(pet, available_tricks)




#project description
"""


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

Joseph Franks: level up method
Function/Method to Implement: level_up()
Information Needed: the level-up method will take one parameter, 
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