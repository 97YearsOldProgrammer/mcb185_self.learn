import random
import sys
import math



import random

# Simulation parameters (using values from the user's code)
trials = 10000  # Number of trials
days = 365      # Number of days in a year
people = 23     # Number of people in the room

# Function to create and reset the calendar
def bd_creator(n):
    return [0] * n

# List to count the number of trials with shared birthdays
ps = []

# Running the simulation
for j in range(trials):
    # Reset calendar to all zeros
    bds = bd_creator(days)
    z = 0
    
    for _ in range(people):
        # Generate random birthday
        x = random.randint(0, days - 1)
        
        # Check if someone already has this birthday
        if bds[x] > 0:
            z = 1
            break
        else:
            bds[x] += 1
    
    # If there's a shared birthday, append to ps
    if z == 1:
        ps.append(1)

# Calculating the probability
probability = len(ps) / trials
print(probability)
