largest = 0
smallest = 0

number = input("Enter your number: ")
if number != "":
    smallest = largest = int(number)
    while number != "":
        numberAsInt = int(number)
        if numberAsInt < smallest:
            smallest = numberAsInt
        elif numberAsInt > largest:
            largest = numberAsInt
        number = input("Enter your number: ")
    else:
        print(f"largest number is: {largest}")
        print(f"And smallest number is: {smallest}")