# Say "Hello, World!" With Python
if __name__ == '__main__':
    print("Hello, World!")  # Print "Hello, World!" to the console

# Print Function
if __name__ == '__main__':
    n = int(input())  # Read an integer input n
for i in range(1, n + 1):  # Loop from 1 to n (inclusive)
    print(i, end='')  # Print numbers from 1 to n on the same line without spaces

# Write a function
def is_leap(year):
    # Determine if a year is a leap year
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True  # Return True if leap year
    else:
        return False  # Return False otherwise

# Python If-Else
#!/bin/python3
import math
import os
import random
import re
import sys

n = int(input())  # Read an integer input n
if n % 2 != 0:  # Check if n is odd
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:  # Check if n is even and in range [2, 5]
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:  # Check if n is even and in range [6, 20]
    print("Weird")
elif n % 2 == 0 and n > 20:  # Check if n is even and greater than 20
    print("Not Weird")

# Loops
if __name__ == '__main__':
    n = int(input())  # Read an integer input n
    i = 0
while 1 <= n <= 20 and i < n:  # Loop from 0 to n-1
    print((i)**2)  # Print the square of the current value of i
    i += 1

# Arithmetic Operators
if __name__ == '__main__':
    x = int(input())  # Read an integer input x
    y = int(input())  # Read an integer input y
    print(x+y)  # Print the sum of x and y
    print(x-y)  # Print the difference of x and y
    print(x*y)  # Print the product of x and y

# Python: Division
if __name__ == '__main__':
    x = int(input())  # Read an integer input x
    y = int(input())  # Read an integer input y
    print(x//y)  # Print the integer division of x by y
    print(x/y)  # Print the float division of x by y

# Find the Runner-Up Score!
r = int(input())  # Read the number of scores
scores = list(map(int, input().split()))  # Convert input to list of scores
unique_scores = list(set(scores))  # Remove duplicate scores
unique_scores.sort()  # Sort the unique scores
print(unique_scores[-2])  # Print the second highest score

# Nested Lists
r = int(input())  # Read the number of students
students = []  # Initialize an empty list to store student records
for _ in range(r):
    name = input()  # Read student name
    grade = float(input())  # Read student grade
    students.append([name, grade])  # Append student record to the list
# Find the second lowest grade
grades = sorted(set([grade for name, grade in students]))  # Get unique grades and sort them
second_lowest_grade = grades[1]  # The second lowest grade
# Find the students who have the second lowest grade
second_lowest_students = [name for name, grade in students if grade == second_lowest_grade]
# Sort names alphabetically
second_lowest_students.sort()
# Print the names of students with the second lowest grade
for name in second_lowest_students:
    print(name)

# Finding the percentage
if __name__ == "__main__":
    r = int(input())  # Read number of students
    student_marks = {}  # Dictionary to store student names and their marks
    for _ in range(r):
        name, *line = input().split()  # Read student name and scores
        scores = list(map(float, line))  # Convert scores to float
        student_marks[name] = scores  # Store scores in the dictionary
    query_name = input()  # Read the name to query
    avg_score = sum(student_marks[query_name]) / len(student_marks[query_name])  # Calculate average score
    print(f"{avg_score:.2f}")  # Print average score rounded to 2 decimal places

# Lists
lst = []  # Initialize an empty list
r = int(input())  # Read the number of commands
for _ in range(r):
    command = input().split()  # Read the command
    if command[0] == "insert":
        lst.insert(int(command[1]), int(command[2]))  # Insert value at specified index
    elif command[0] == "print":
        print(lst)  # Print the list
    elif command[0] == "remove":
        lst.remove(int(command[1]))  # Remove first occurrence of the value
    elif command[0] == "append":
        lst.append(int(command[1]))  # Append value to the list
    elif command[0] == "sort":
        lst.sort()  # Sort the list
    elif command[0] == "pop":
        lst.pop()  # Pop the last element
    elif command[0] == "reverse":
        lst.reverse()  # Reverse the list

# Tuples
length = int(input())  # Read the number of elements
tokens = input().split()  # Read the elements as strings
data = list(map(int, tokens))  # Convert elements to integers
t = tuple(data)  # Create a tuple from the list
print(hash(t))  # Print the hash value of the tuple

# List Comprehensions
x = int(input())  # Read input x
y = int(input())  # Read input y
z = int(input())  # Read input z
n = int(input())  # Read input n
# List comprehension to generate 3D coordinates
coordinates = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
# Print the resulting list
print(coordinates)

# What's Your Name?
# Function to print full name with greeting
def print_full_name(r, y):
    print(f"Hello {r} {y}! You just delved into python.")

# String Split and Join
def split_and_join(line):
    words = line.split()  # Split the string into words by whitespace
    result = "-".join(words)  # Join the words with hyphen as separator
    return result
input_string = input()  # Read the input string
print(split_and_join(input_string))  # Print the joined string

# Mutations
def mutate_string(string, position, character):
    chars = list(string)  # Convert string to list of characters
    chars[position] = character  # Change character at the given position
    return "".join(chars)  # Convert list back to string and return

# Find a string
def count_substring(string, sub_string):
    # Count occurrences of sub_string in string
    return sum(
        string[i : i + len(sub_string)] == sub_string
        for i in range(len(string) - len(sub_string) + 1) )

# String Validators
if __name__ == '__main__':
    a = input()  # Read input string
    print(any(c.isalnum() for c in a))  # Check if any character is alphanumeric
    print(any(c.isalpha() for c in a))  # Check if any character is alphabetic
    print(any(c.isdigit() for c in a))  # Check if any character is a digit
    print(any(c.islower() for c in a))  # Check if any character is lowercase
    print(any(c.isupper() for c in a))  # Check if any character is uppercase

# Text Alignment
thickness = int(input())  # Read thickness value (must be odd)
c = 'H'
for i in range(thickness):
    # Print the top cone
    print((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))
for i in range(thickness + 1):
    # Print the top pillars
    print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))
for i in range((thickness + 1) // 2):
    # Print the middle belt
    print((c * thickness * 5).center(thickness * 6))
for i in range(thickness + 1):
    # Print the bottom pillars
    print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))
for i in range(thickness):
    # Print the bottom cone
    print(((c * (thickness - i - 1)).rjust(thickness) + c + (c * (thickness - i - 1)).ljust(thickness)).rjust(thickness * 6))

# Text Wrap
def wrap(string, max_width):
    # Wrap text to a given width
    return textwrap.fill(string, max_width)

# Designer Door Mat
A, B = map(int, input().split())  # Read dimensions of the mat
for i in range(1, A, 2):
    # Print the top pattern
    print(int((B - 3 * i) / 2) * "-" + (i * ".|.") + int((B - 3 * i) / 2) * "-")
print(int((B - 7) / 2) * "-" + "WELCOME" + int((B - 7) / 2) * "-")  # Print the welcome line
for i in range(A - 2, -1, -2):
    # Print the bottom pattern
    print(int((B - 3 * i) / 2) * "-" + (i * ".|.") + int((B - 3 * i) / 2) * "-")

# String Formatting
def print_formatted(number):
    # Print the formatted numbers
    width = len(bin(number)) - 2
    for i in range(1, number + 1):
        print(str(i).rjust(width),      # Print decimal representation
              oct(i)[2:].rjust(width),  # Print octal representation
              hex(i)[2:].upper().rjust(width),  # Print hexadecimal representation (in uppercase)
              bin(i)[2:].rjust(width))  # Print binary representation

# Alphabet Rangoli
def print_rangoli(size):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    lines = []  # List to store each line of the rangoli
    for i in range(size):
        # Generate the line with characters in descending and ascending order
        s = '-'.join(alphabet[size-1:i:-1] + alphabet[i:size])
        lines.append(s.center(4*size
