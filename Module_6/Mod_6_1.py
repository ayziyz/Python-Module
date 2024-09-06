import random

def roll_dice():
    return random.randint(1, 6)
def main():
    roll_result = 0
    while roll_result != 6:
        roll_result = roll_dice()
        print(f"Rolled: {roll_result}")

    print("Rolled a 6! Game over.")

if __name__ == "__main__":
    main()