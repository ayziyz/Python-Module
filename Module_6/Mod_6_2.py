import random

def roll_dice(sides):
    return random.randint(1, sides)


def main():

    sides = int(input("Enter the number of sides on the dice: "))
    target = int(input(f"Enter the target number (1 to {sides}): "))

    if target < 1 or target > sides:
        print("Target number must be within the range of the dice sides.")
        return

    roll_result = 0
    while roll_result != target:
        roll_result = roll_dice(sides)
        print(f"Rolled: {roll_result}")

    print(f"Rolled a {target}! Game over.")

if __name__ == "__main__":
    main()