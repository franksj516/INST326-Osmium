# Virtual Pet Final Project

This repository contains three key files essential for running the pet simulation game:

- **`customization_options.json`**: Provides a range of customization options for pets.
- **`pet.py`**: The main program script that implements pet interactions and gameplay mechanics.
- **`tricks.txt`**: Contains a list of tricks and the required happiness points needed for a pet to learn each trick.

## Running the Program

To run the game, use the following command in your terminal:

`python pet.py`

## Gameplay Instructions

After initiating the program, follow these steps to interact with your pet:

1. **Choose a Pet**:
   - You will be prompted to choose from a list of pet types (e.g., dog, cat, etc.). Type the number corresponding to the pet.

2. **Name Your Pet**:
   - After selecting a type, you will need to give your pet a name.

### Main Menu Options

Once your pet is set up, you will be brought to the main menu, which offers the following options:

- **Feed the Pet**:
  - Increases the pet's health.

- **Play with the Pet**:
  - Boosts the pet's happiness.

- **Teach or Perform a Trick**:
  - Allows the pet to learn and perform new tricks such as 'roll over' or 'fight'.

- **Show Pet Status**:
  - Displays detailed information on the pet's health, happiness, level, skills, and customizations.

- **Exit Game**:
  - Ends the program.

You navigate this menu, once again, by typing the number corresponding to the menu option.

### Leveling Up and Prizes

- As you engage with your pet a number of times through various activities including playing and feeding, it will level up.
- Leveling up unlocks opportunities to play mini-games where you can win prizes for your pet, such as new accessories, changes to the habitat, or even altering the pet's color.

### Feedback and Error Handling

- After each interaction, you will receive feedback reflecting the outcome of your actions.
- Should you use an invalid input during gameplay, a message will be displayed that prompts you to make a correct choice, such as "Invalid choice. Please try again."

## ATTRIBUTION

| Method/function   | Primary author | Techniques demonstrated       |
|-------------------|----------------|-------------------------------|
| check_level_up    | Justin Fargnoli| f-strings containing expressions|
| feed              | Justin Fargnoli| Conditional expressions       |
| customize_pet     | Joseph Franks           | json.load()                   |
| choose_activity   | Joseph Franks            | Sequence unpacking            |
