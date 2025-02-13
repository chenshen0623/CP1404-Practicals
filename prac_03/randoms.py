import random

print(random.randint(5, 20))  # line 1
#The number you see each time may be different.
# The smallest number that may appear is 5 and the largest number is 20.
print(random.randrange(3, 10, 2))  # line 2
#The smallest possible number is 3, and the largest number is 9.
# It is impossible for the number 4 to appear because there is no 4 in the sequence.
print(random.uniform(2.5, 5.5))  # line 3
#The possible minimum value is 2.5 and the maximum value is 5.5.
print(random.randint(1, 100))
