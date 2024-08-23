
talents = float(input("Enter the talents: "))
pounds = float(input("Enter the pounds: "))
lots = float(input("Enter the lots: "))

kilograms = ((talents*20+pounds)*32 + lots)*0.0133
grams = 1000.0 *(kilograms - int(kilograms))

print(f"The weight in modern units:\n{int (kilograms)} kilograms and {grams: .2f} grams")

