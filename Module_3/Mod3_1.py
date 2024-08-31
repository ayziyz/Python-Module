zander_length = int(input('Please enter the length of Zander in centimeters: '))
size_limit = 42
if zander_length >= size_limit:
    print('Great Catch')
else:
    below_limit = size_limit - zander_length
    print(f'Please release the fish back to the see because it is smaller by {below_limit} cm.')
