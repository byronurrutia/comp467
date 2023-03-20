# Start learning Python and let's do a job interview question:
# Write a script that dumps 20 random numbers in an array then finds the largest
# number.
# Turn in your code and output result (Show array and the largest number to output)(copy/paste is fine)
import random;

numbers = [random.randint(1,1000)];
for i in range(20):
    numbers.append(random.randint(1,1000));
    print("Element #" + str(i + 1) + "; Generated Number: " + str(numbers[i]));
numbers.sort();
print("Largest element is: " + str(numbers[-1]))
