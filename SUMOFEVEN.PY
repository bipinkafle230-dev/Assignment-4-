# Main function to start the program
def added():
    calculate_sum()

# Function to calculate the sum of even numbers from 1 to n
def calculate_sum():
    # Asking user for a positive integer
    n = int(input("Enter the positive integer: "))

    # Initializing the variable to store the sum of even numbers
    SqSum = 0

    # Looping through numbers from 1 to n (inclusive)
    for i in range(1, n + 1):
        if i % 2 == 0:  # Checking if the number is even
            SqSum += i  # Adding even number to the sum

    # Printing the final result
    print(f"Sum of even numbers from 1 to {n}: {SqSum}")

# Calling the main function to run the program
added()
  