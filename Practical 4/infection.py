# 1. Initialise the number of infected students (n) with the starting value (5).
# 2. Initialise a day counter (d) to 0.
# 3. While the number of infected students is less than the total class size (91):
#       Calculate the new number of infected students after one day using the growth rate (40% increase).
#       Increment the day counter by 1.
#       Display the number of infected students for this day.
# 4. Once all students are infected, print the total number of days taken.

# Create variables
# current number of infected students
n = 5   
# day counter (number of days passed)       
d = 0          
# While loop & print infected students each day
while n < 91 :
    # growth rate of 40% per day
    n = 1.4 * n    
    # move to the next day  
    d = d + 1        
    # show infected count for this day
    print(n)         
# Print days taken
print(d, " days were taken to infect all")