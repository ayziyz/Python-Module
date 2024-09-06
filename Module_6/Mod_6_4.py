def sum_of_list(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

def main():
    my_list = [10, 20, 30, 40, 55]

    result = sum_of_list(my_list)

    print(f"The sum of the list is: {result}")

if __name__ == "__main__":
    main()