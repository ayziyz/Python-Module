import random
import math
random_points = int(input ("How many random points to be generated? "))
inside_points = 0
i = 0
while i < random_points:
    x = random.uniform(-1,1.)
    y = random.uniform (-1,1.)
    if x**2 +y**2 < 1:
        inside_points +=1
    i += 1
pi = 4 * inside_points / random_points
print(f" Pi estimation is {pi}. the difference with math pi is: {math.pi - pi}")