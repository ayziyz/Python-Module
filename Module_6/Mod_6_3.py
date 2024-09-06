def gallons_to_liters(gallons):
    return gallons * 3.78541


def main():
    while True:
        user_input = input("Enter the volume in gallons (or a negative value to quit): ")

        if user_input.lstrip('-').replace('.', '', 1).isdigit():
            gallons = float(user_input)

            if gallons < 0:
                print("Negative value entered. Exiting.")
                break

            liters = gallons_to_liters(gallons)
            print(f"{gallons} gallons is equal to {liters:.2f} liters.")
        else:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()