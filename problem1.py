print("Problem 01 ~ Assignment 4".center(42, "="))
print("\033[94m=" * 42)
print("\033[91mCMPE-103-MODULE-2-FILE-HANDLING-IN-PYTHON")
print("\033[94m=" * 42)

# write a python program that reads a text file, then the program will classify the even and odd numbers
# into separate text files extracted from the main text file

# pseudocode
# create a text file named "numbers.txt" that will contain 20 integers
# open, read, and split the file for it to be ready on creating the main goal of the program
with open("numbers.txt", "r") as problem_one_numbers_file:
    numbers_data = problem_one_numbers_file.read().split()
# generate two empty list that will serve as a holder of even and odd numbers
even_data = []
odd_data = []
# construct the loop that will identify between even and odd numbers
for number in numbers_data:
    if int(number) % 2 == 0:
        even_data.append(number)
    else:
        odd_data.append(number)
# open the file and transfer the classified even numbers to designated text file named "even.txt"
# open the file and transfer the classified even numbers to designated text file named "odd.txt"
# check the newly created text files and if the problem is solved.