# Given
talents_to_pounds = 20
pounds_to_lots = 32
lots_to_grams = 13.3

talents = float(input("Enter the talents: "))
pounds = float(input("Enter the pounds: "))
lots = float(input("Enter the lots: "))

total_pounds = (talents_to_pounds * talents) + pounds
total_lots = (pounds_to_lots * pounds) + lots
total_grams = total_lots * lots_to_grams

kilograms = total_grams // 1000
grams = total_grams % 1000

print(f"{kilograms} kilograms and {grams} grams")

