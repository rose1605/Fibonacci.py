def generate_fibonacci(num_terms):
    # Check if the input is valid
    if num_terms <= 0:
        print("Please enter a positive integer.")
        return

    # Initialize the first two terms
    fibonacci_sequence = [0, 1]

    # Generate the sequence up to the specified number of terms
    for i in range(2, num_terms):
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)

    # Display the sequence up to the specified number of terms
    print("Fibonacci sequence:")
    print(fibonacci_sequence[:num_terms])


# Example usage
try:
    num_terms = int(input("Enter the number of terms: "))
    generate_fibonacci(num_terms)
except ValueError:
    print("Please enter a valid integer.")
