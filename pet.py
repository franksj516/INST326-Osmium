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
            self.health += 20 if self.health <= 80 else 100 - self.health
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

        print(f"{self.name} now has a {selected_option}!")


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