inch_to_cm = 2.54
while True:
    inch = float(input('Enter a value in Inches: '))
    if inch <0:
        print('Negative value Encountered. Program Terminated.')
        break
    centimeters = inch_to_cm * inch
    print(f"{inch} inches is equal to {centimeters:2f} centimeters")