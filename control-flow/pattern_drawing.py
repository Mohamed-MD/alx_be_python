size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use a while loop to control the rows
while row < size:
    # Use a for loop to print asterisks in each row
    for col in range(size):
        print("*", end="")  # print without newline
    print()  # move to the next line after each row
    row += 1