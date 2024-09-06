numbers = []

while True:
    user_input = input('Enter a number or Press Enter to Quit: ')

    if user_input == "":
        break
    try: # Convert the input to a int and add it to the list
        number = int(user_input)
        numbers.append(number)
    except ValueError:         # Handle non-numeric input
        print("Please enter a valid number.")

numbers.sort(reverse=True)

print('The 5 greatest number are: ')
for i in range(min(5, len(numbers))):
    print(numbers[i])