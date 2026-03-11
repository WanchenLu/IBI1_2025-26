# What does this piece of code do?
# Answer: the code generates 11 intergers between [1,10] randomly and outputs their summary

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

# Create two variables
total_rand = 0
progress=0
# After a loop, progress increases by 1, total_rand increases by [1,10] randomly, and the loop carries on until progress becomes 10
while progress<=10:
	progress+=1
	n = randint(1,10)
	total_rand+=n

# After 11 loops, it displays total_rand at the end
print(total_rand)

