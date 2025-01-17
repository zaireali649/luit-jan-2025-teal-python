import random
import math
import os
from datetime import datetime
import matplotlib.pyplot as plt
import hello_world 

# Generate a random integer between 0 and 100
random_number = random.randint(0, 100)
print(f"Random number between 0 and 100: {random_number}")

# Calculate the square root of the random number
square_root = math.sqrt(random_number)
print(f"Square root of {random_number}: {square_root:.2f}")

# List all files in the current directory
current_directory = os.getcwd()
files = os.listdir(current_directory)
print("\nFiles in the current directory:")
for file in files:
    print(f"- {file}")

# Get the current date and time
current_time = datetime.now()
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
print(f"\nCurrent date and time: {formatted_time}")

# Generate a random floating-point number between 0 and 1
random_float = random.random()
print(f"Random floating-point number between 0 and 1: {random_float:.4f}")

# Calculate the cosine of a random angle (in radians)
random_angle = random.uniform(0, math.pi * 2)  # Random angle between 0 and 2*pi
cosine_value = math.cos(random_angle)
print(f"Cosine of angle {random_angle:.2f} radians: {cosine_value:.4f}")

# Plotting with matplotlib
x_values = list(range(0, 10))
y_values = [random.randint(0, 100) for _ in x_values]

plt.plot(x_values, y_values, marker='o', linestyle='-', color='b', label='Random Data')
plt.title('Random Data Plot')
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.legend()
plt.grid(True)
plt.show()

hello_world.hello_world()