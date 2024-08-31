smallest = None
largest = None
while True:
    input_value = int(input("Enter the numbers or Press Enter to Quit: "))

    if input_value == "":
        break

    if smallest is None and largest is None:
        smallest = input_value
        largest = input_value
    else:
        if input_value < smallest:
            smallest = input_value
        if input_value > largest:
            largest = input_value
if smallest is not None and largest is not None:
    print(f"The smallest number entered is: {smallest}")
    print(f"The largest number entered is: {largest}")
else:
    print("No numbers were entered.")