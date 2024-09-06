def remove_odd_numbers(numbers):
    even_numbers = [number for number in numbers if number % 2 == 0]
    return even_numbers

def main():
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    even_list = remove_odd_numbers(list)

    print(f"Initial list: {list}")
    print(f"List with odd numbers removed: {even_list}")


if __name__ == "__main__":
    main()