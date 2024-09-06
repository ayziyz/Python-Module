
user_input = input("Enter an integer to check if it is a prime number: ")

if user_input.lstrip('-').isdigit():
    number = int(user_input)
    int(user_input)
    if number ==2:
        print('The number is a prime number')
    elif number % 2 == 0:
        print('The number is not a prime')
    else:
        is_prime = True
        i = 3
        while i * i <= number:
            if number % i == 0:
                is_prime = False
                break
            i += 2

        if is_prime:
            print(f"{number} is a prime number.")
        else:
            print(f"{number} is not a prime number.")
else:
        print("Please enter a valid integer.")
