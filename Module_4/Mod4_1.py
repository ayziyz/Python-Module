number = 1
count = 0
while number <=1000:
    if number % 3 ==0:
        print(number)
        count +=1
    number += 1
print(f'The total numbers which were divisible by 3 were: {count}')
