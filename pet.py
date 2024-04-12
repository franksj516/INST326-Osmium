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
    #
    for index, type in enumerate(pet_list, start=1):
        print(f"{index}. {type}")
    choice = int(input("Enter the number to the pet of your choosing: "))
    if choice <1 or choice > len(pet_list):
        print("This choice is invalid and out of range. Please try again.")
        return choose_pet()
    name=input("Now that you've chosen your pet type, please name your pet: ")
    return Pet(name, pet_list[choice-1])

pet = choose_pet()
print(f"Congrats! You have a pet! You have chosen a {pet.pet_type} named {pet.name}.")
print(f"Your pet is currently at Level: {pet.level} and Health: {pet.health}.")