import random

dice_num = int(input('How many dice do you want to roll?: '))

total_sum = 0

for _ in range(dice_num):
    roll = random.randint(1,6)
    total_sum += roll
    print(f"Roll {_ + 1}: {roll}")

print(f"The sum of numbers for all the dice rolls: {total_sum}")


